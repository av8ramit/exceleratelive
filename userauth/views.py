from models import Student, MyUserManager

from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from Library.Console import *
from Library.Values import *
from Library.AWSConnector import *
from operator import itemgetter
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.core.mail import send_mail

from .forms import UploadFileForm
import csv

import re


def home(request):
    """
    Goes to home page - checks to see if it is sent a post (from postregister page) with the username. If it was, then pre-fill the username field
    """
    if request.POST:
        c = {}
        c.update(csrf(request))
        u_name = request.POST.get('username')
        return render(request, 'userauth/login.html', { 'username': u_name })
    else:
        return render(request, 'userauth/login.html')

def register(request):
    """
    Simply sends user to the register page
    """
    return render(request, 'userauth/register.html')

def fields_check(u_name, p_word, fname, lname, school, email, studentid):
    """
    Check if fields are valid. Returns None if valid. Else will return
    a string describing the error
    """
    error_message = ""
    if not (u_name and p_word and fname and lname and email):
        error_message += "Required field was left blank\n"

    names = [u_name, fname, lname]
    for char in u_name:
        if char in '/ !@#$%^&*(),.<>/?"{[}]|':
            error_message = "Please refrain from using spaces or special characters in your username.\n"


    for name in names:
        if len(name) > 30:
            if name == u_name:
                error_message += "Username must be less than 30 characters\n"
            elif name == fname:
                error_message += "First name must be less than 30 characters\n"
            else:
                error_message += "Last name must be less than 30 characters\n"

    school_check = type(school) == str and len(school) <= 50
    if len(school) > 50:
        error_message += "School must be less than 50 characters\n"
    if studentid:
        if not str(studentid).isdigit():
            error_message += "Please provide a numeric student id\n"

    reg = re.compile(".+@.+\\..+")
    email_check = False
    if not reg.match(email) or len(email) > 100:
        error_message += "Email incorrectly formatted. Please use valid email format that is under 100 characters."
    if error_message == "":
        return None
    else:
        return error_message


def send(request):
    """
    Called after submitting a register form
    Collects all the post information, checks for matching passwords, and does one of two things:
    1. If passwords do not match, reload register form with error message and pre-filled fields
    2. If everything is valid, create user object and send to postregister page with username variable
    """ 
    u_name = p_word = ''
    if request.POST:
        c = {}
        c.update(csrf(request))
        u_name = request.POST.get('username')
        p_word = request.POST.get('password')
        re_pass = request.POST.get('retypepassword')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        school = request.POST.get('school')
        email = request.POST.get('email')
        studentid = request.POST.get('studentid')

        error_fields = fields_check(u_name, p_word, fname, lname, school, email, studentid)

        if not p_word == re_pass:
            error_message = "Passwords do not match"
            return render(request, 'userauth/register.html', {
                'username': u_name, 'fname':fname, 'lname':lname, 'school':school, 'email':email, 'studentid':studentid, 'errormsg':error_message
                })
        if error_fields:
            error_message = error_fields
            return render(request, 'userauth/register.html', {
                'username': u_name, 'fname':fname, 'lname':lname, 'school':school, 'email':email, 'studentid':studentid, 'errormsg':error_message
                })

        # regex = re.compile(".+?@.+?\..+")
        # if not regex.search(email):
        #   error_message = "Incorrect Email Format"
        #   context = #bitchs
        # if not studentid.isdigit():
        #   error_message = "Please put a valid student id"
        #   context = #peace

        try:
            user = Student.objects.create_user(username=u_name, password=p_word,
                                    first_name=fname, last_name=lname,
                                    school_name=school, email=email,
                                    student_id=studentid)
        except:
            error_message = "Something went wrong. Most likely that username or email already exists. Please try and use another username."
            return render(request, 'userauth/register.html', {
                'username': u_name, 'fname':fname, 'lname':lname, 'school':school, 'email':email, 'studentid':studentid, 'errormsg':error_message
                })

        user.save()
        console = Console()
        console.process_commands("load_class web")
        console.process_commands("new_student " + u_name)
        bucket = call_bucket()
        userdumpkey = get_key_userdump(bucket)
        userdumpkey.get_contents_to_filename('Users/web/userdump.txt')
        add_user(u_name, fname, lname, email, school)
        userdumpkey.set_contents_from_filename('Users/web/userdump.txt')
        k = get_key(bucket, u_name)
        k.set_contents_from_filename(user_filename(u_name, 'web'))
        return render(request, 'userauth/postregister_base.html', {'username':u_name})
    else:
        return HttpResponse("Sorry something went wrong")

# shouldn't need this - handled in home now
# def postregister(request):
#   if request.POST:
#       c = {}
#       c.update(csrf(request))
#       u_name = request.POST.get('username')
#       return render(request, 'userauth/login_post.html', { 'username': u_name })

def login_user(request):
    """
    Called from login page
    Authenticates username and password
    Loads user page or displays appropriate error
    """
    u_name = p_word = ''
    if request.POST:
        
        
        u_name = request.POST.get('username')
        p_word = request.POST.get('password')
        remember = request.POST.get('remember-me', False)
        user = authenticate(username=u_name, password=p_word)
        if user is not None:
            # adding user cookie getting ERROR when I try to store this cookie
            # request.session['user'] = user 
            # the password verified
            if user.is_active:
                login(request, user) #use this for sessions (built in)
                #S3 Load
                if not (file_exists(user_directory(u_name, 'web'))):
                    bucket = call_bucket()
                    key = get_key(bucket, u_name)
                    mkdir(user_directory(u_name, 'web'))
                    key.get_contents_to_filename(user_filename(u_name, 'web'))
                console = Console()
                console.process_commands("load_class web")
                console.process_commands("load_student " + u_name)
                test_list_c = console.process_commands("list_tests c")
                test_list_k = console.process_commands("list_tests k")
                tests = console.process_commands("list_tests_taken")
                scores = console.user.recent_scores()
                request.session[TEST_MODE] = FULL_TEST
                date = console.user.get_intended_date()
                goal = console.user.intended_score


                #test_list = ["GE29", "GE30", "GE31", "GE32"]
                return render(request, 'userauth/userpage.html', {'user':user, 'test_list_k':test_list_k,  'test_list_c':test_list_c, 'scores':scores, 'date':date, 'goal':goal ,'tests':tests, 'user_name':u_name})
            else:
                # User account has been disabled
                error_message = "Sorry, this user has been disabled"
                return render(request, 'userauth/login.html', {'errormsg':error_message})
        else:
            # Username and password combination was not verified
            error_message = "Incorrect username or password"
            return render(request, 'userauth/login.html', {'errormsg':error_message})

def forgot(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        np = request.POST.get('npassword')
        cnp = request.POST.get('cnpassword')
        u = Student.objects.get(username=username)
        if u != None:
            if u.email == email:
                if np == cnp:
                    u.set_password(np)
                    u.save()
                    context = {"message" : "Successfully Changed Password!", "rurl" : "/"}
                    return render(request, 'userauth/forgot_response.html', context)
        context = {"message" : "Something went wrong!", "rurl" : "/forgot/"}
        return HttpResponse("Something went wrong!", context)

    else:
        return render(request, 'userauth/forgot.html', {})

def formtest2(request):
    """
    Successfully using the form to input commands as if they were entered through the shell
    """
    if request.POST:
        context = {}
        context.update(csrf(request))
        cmd = request.POST.get('cmd')
        # try to get the cookie
        # if 'user' in request.session:
        #   user = request.session['user']
        user = request.user
        print('printing school name')
        print(user.school_name)
        console = Console()
        try:
            console.process_commands(str(cmd))
            if (cmd == 'simple_report'):
                return render(request, 'web/' + user.username + '/simple_report.html')
            if (cmd == 'advanced_report'):
                return render(request, 'web/' + user.username + '/advanced_report.html')        
            if console.error != None:
                response = console.error
            else:
                response = "Successfully called excelerate function: " + cmd
            return render(request, 'userauth/userpage.html', {'response':response, 'user':user})
        except Exception as e:
            response = 'Something went wrong with command:' + cmd + ". Exception outputted: "
            return render(request, 'userauth/userpage.html', {'response':response, 'message':e, 'user':user})
    else:
        response = 'Something wrong with post'
        return render(request, 'userauth/userpage.html', {'response':response, 'user':user})

def recover_password_page(request):
    return render(request, 'userauth/resetpassword.html')


def recover_password(request):
    if request.POST:
        emailAddr = request.POST.get('email')
        exists = Student.objects.filter(email=emailAddr).count()
        if exists == 1:
            user_password = Student.objects.get(email=emailAddr).password
            from_addr = 'exceleratetestprep@gmail.com'
            from_password = 'letsmakeitbig' # set
            email_message = 'Your password is "' + user_password + '"'
            send_mail(subject="Password Recovery", message=email_message, from_email=from_addr,
                        recipient_list=[emailAddr], auth_user=from_addr, auth_password=from_password)
            return HttpResponse("Success")
        elif exists == 0:
            error_message = "Sorry, we don't have your email in our system"
            return HttpResponse(error_message)
        else:
            error_message = "Unhandled Error."
            return HttpResponse(error_message)




############### Bubble Sheet Form 


def handle_uploaded_file(user, f):
    with open('Users/web/' + user.username + '/' + f.name, 'wb+') as dest:
        for chunk in f.chunks():
            dest.write(chunk)

def update_test_mode(request):
    if request.session[TEST_MODE] == FULL_TEST:
        request.session[TEST_MODE] = QUICK_SECTIONS
    else:
        request.session[TEST_MODE] = FULL_TEST
    print(request.session[TEST_MODE])
    return HttpResponse()

def upload_file(request):
    if request.method == 'POST':
        data = {'title':"data title"}
        # form = UploadFileForm(request.POST, request.FILES)
        form = UploadFileForm(data, request.FILES)
        if form.is_valid():
            console = Console()
            console.process_commands("load_class web")
            console.process_commands("load_student " + request.user.username)
            handle_uploaded_file(request.user, request.FILES['file'])
            console.process_commands('grade ' + request.FILES['file'].name)
            if console.error != None:
                #print console.error
                return HttpResponse('There was an issue grading your CSV file. Your essay might not be a valid value. Please ensure you followed the instructions on our "How it Works" page and try again. Click <a href="javascript:history.go(-1)">here</a> return to the dashboard page.')
            else:
                console.process_commands('save')
                bucket = call_bucket()
                k = get_key(bucket, request.user.username)
                k.set_contents_from_filename(user_filename(request.user.username, 'web'))
                return render(request, 'web/' + request.user.username + '/grade.html')
        else:
            form = UploadFileForm()
        return response

def download_file(request):
    with open('Users/web/' + request.user.username + '/uploaded_file.csv', 'rb') as f:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="downloaded_file.csv"'
        reader = csv.reader(f, delimiter=',')
        writer = csv.writer(response)
        for row in reader:
            writer.writerow(row)
        return response
    return HttpResponse('File did not open')

def download_test(request):
    if request.POST:
        console = Console()
        test_number = request.POST.get('test')
        cmd = "answer_sheet " + test_number
        console.process_commands("load_class web")
        console.process_commands("load_student " + request.user.username)
        console.process_commands(cmd)
    with open('Users/web/' + request.user.username + '/' + test_number + '.csv', 'rb') as f:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=' + test_number + '.csv'
        reader = csv.reader(f, delimiter=',')
        writer = csv.writer(response)
        for row in reader:
            writer.writerow(row)
        return response
    return HttpResponse('File did not open')

#function to collect bubblesheet form data, manipulate it, and pass it to a csv answer sheet maker function, then grade test

def grade_save_bubblesheet(request):
    if request.POST:
        '''
        webdata = [] # hold form data
        swebdata = []
        bubbledata = []  # filtered form data
        webdata = sorted(request.POST) # get all test form answers
        swebdata = sorted(webdata, key = itemgetter(0,1))
        print(str(webdata))
        for item in webdata:   
            bubbledata.append(request.POST.get(item))
        '''    


        filename = request.POST.get('test')
    
        lines = []
        label_vector = "Number:,Answer:" + endl
        lines.append(filename + " Answer Sheet" + endl)
        lines.append("Name:," + request.user.username + endl)
        lines.append("Date:," + datetime_converter(str(datetime.date.today())) + endl)
        lines.append("Type:," +  str(request.session[TEST_MODE]) + endl)
        lines.append("Essay:,"+ str(request.POST.get('Essay')) + endl)
        lines.append(label_vector)
        with open(test_directory(filename) + DIR_SEP + KEYFILE, 'rU') as f:
            reader = csv.reader(f)
            for row in reader:
                if row != KEY_VECTOR:
                    lines.append("Section " + str(row[0]) + ":" + endl)
                    for j in range(1,int(row[2]) + 1):
                        lines.append(str(j) + "," + str(request.POST.get("Section " + str(row[0]) + "  Question " + str(j))))
                        lines.append(endl)
        FILE = open(user_directory(request.user.username, 'web') + DIR_SEP + filename + ".csv", "w")
        FILE.writelines(lines)
        FILE.close()
        console = Console()
        console.process_commands("load_class web")
        console.process_commands("load_student " + request.user.username)
        console.process_commands('grade ' + str(filename) + '.csv')
        if console.error != None:

            #print console.error
            return HttpResponse('There was an issue grading your CSV file. Please ensure you followed the instructions on our "How it Works" page and try again. Click <a href="javascript:history.go(-1)">here</a> return to the bubblesheet page.')
        else:

            console.process_commands('save')
            bucket = call_bucket()
            k = get_key(bucket, request.user.username)
            k.set_contents_from_filename(user_filename(request.user.username, 'web'))
            return render(request, 'web/' + request.user.username + '/grade.html')

def bubblesheet_omit(request):
    test_number = request.session[TEST_SELECTED]
    request.session[TEST_MODE] = QUICK_SECTIONS
    console = Console()
    cmd = "bubble_sheet_omit " + test_number
    console.process_commands("load_class web")
    console.process_commands("load_student " + request.user.username)
    console.process_commands(cmd)
    return render(request, 'web/' + request.user.username + '/' + str(test_number)  + '.html')

def bubblesheet(request):
    test_number = request.session[TEST_SELECTED]
    request.session[TEST_MODE] = FULL_TEST
    console = Console()
    cmd = "bubble_sheet " + test_number
    console.process_commands("load_class web")
    console.process_commands("load_student " + request.user.username)
    console.process_commands(cmd)
    return render(request, 'web/' + request.user.username + '/' + str(test_number)  + '.html')

def simple_report(request):
    console = Console()
    console.process_commands("load_class web")
    console.process_commands("load_student " + request.user.username)
    if len(console.user.tests_taken) == 111110:
        return HttpResponse('Please take tests before opening reports. Click <a href="javascript:history.go(-1)">here</a> return to the dashboard page.')
    else:
        console.process_commands("simple_report")
        print console.error
        return render(request, 'web/' + request.user.username + '/simple_report.html')


def advanced_report(request):
    console = Console()
    console.process_commands("load_class web")
    console.process_commands("load_student " + request.user.username)
    if len(console.user.tests_taken) == 1110:
        return HttpResponse('Please take tests before opening reports. Click <a href="javascript:history.go(-1)">here</a> return to the dashboard page.')
    else:
        console.process_commands("advanced_report")
        return render(request, 'web/' + request.user.username + '/advanced_report.html')

def math_report(request):
    console = Console()
    console.process_commands("load_class web")
    console.process_commands("load_student " + request.user.username)
    if len(console.user.tests_taken) == 1110:
        return HttpResponse('Please take tests before opening reports. Click <a href="javascript:history.go(-1)">here</a> return to the dashboard page.')
    else:
        console.process_commands("section_report")
        return render(request, 'web/' + request.user.username + '/math_report.html')    

def writing_report(request):
    console = Console()
    console.process_commands("load_class web")
    console.process_commands("load_student " + request.user.username)
    if len(console.user.tests_taken) == 1110:
        return HttpResponse('Please take tests before opening reports. Click <a href="javascript:history.go(-1)">here</a> return to the dashboard page.')
    else:
        console.process_commands("section_report")
        return render(request, 'web/' + request.user.username + '/writing_report.html')  

def reading_report(request):
    console = Console()
    console.process_commands("load_class web")
    console.process_commands("load_student " + request.user.username)
    if len(console.user.tests_taken) == 1110:
        return HttpResponse('Please take tests before opening reports. Click <a href="javascript:history.go(-1)">here</a> return to the dashboard page.')
    else:
        console.process_commands("section_report")
        return render(request, 'web/' + request.user.username + '/reading_report.html')  


def quicktips(request):
    #return render(request, 'mysite/index_base.html')
    return render(request, 'userauth/quicktips.html')

def testportal(request):
    #return render(request, 'mysite/index_base.html')
    if request.POST:
        console = Console()
        request.session[TEST_SELECTED] = request.POST.get('test')
    return render(request, 'userauth/testportal_base.html', {'user':request.user, 'test':TEST_LIB_DICT[request.session[TEST_SELECTED]]})

def save_info(request):
    if request.POST:
        console = Console()
        u_name = request.user.username
        console.process_commands("load_class web")
        console.process_commands("load_student " + u_name)
        test_list_c = console.process_commands("list_tests c")
        test_list_k = console.process_commands("list_tests k")
        tests = console.process_commands("list_tests_taken")
        scores = console.user.recent_scores()
        request.session[TEST_MODE] = FULL_TEST
        try:
            date = request.POST.get('date_')
            score = request.POST.get('score_')
            if score != None:
                console.process_commands('update_score ' + score)
            if date != None:
                console.process_commands('update_date ' + date)
            console.process_commands('save')
            date = console.user.get_intended_date()
            goal = console.user.intended_score
            bucket = call_bucket()
            k = get_key(bucket, request.user.username)
            k.set_contents_from_filename(user_filename(request.user.username, 'web'))
        except:
            pass
    return HttpResponseRedirect('/login/dashboard/')

def test_review(request):
    if request.POST:
        console = Console()
        console.process_commands("load_class web")
        console.process_commands("load_student " + request.user.username)
        console.process_commands('test_review ' + request.POST.get('test').split('.')[0])
        return render(request, 'web/' + request.user.username + '/grade.html')

def delete_test(request):
    if request.POST:
        console = Console()
        console.process_commands("load_class web")
        console.process_commands("load_student " + request.user.username)
        if (request.POST.get('delete') != None):
            #delete the test here
            test_to_delete = request.POST.get('delete')
            data = test_to_delete.split('.')[1].split("|")
            cleaned_test_to_delete = data[0][1:].rstrip()
            test_to_delete_date = data[1][9:].rstrip()
            test_to_delete_id = TEST_LIB_DICT_R[cleaned_test_to_delete]
            test_data = test_to_delete_id + "," + test_to_delete_date + "," + request.POST.get('delete').split('.')[0]
            console.process_commands("delete_test " + request.user.username + " " + test_data)
            bucket = call_bucket()
            k = get_key(bucket, request.user.username)
            k.set_contents_from_filename(user_filename(request.user.username, 'web'))
            return HttpResponseRedirect('/login/dashboard/')

def dashboard(request):
    user = request.user
    u_name = user.username
    console = Console()
    console.process_commands("load_class web")
    console.process_commands("load_student " + u_name)
    test_list_c = console.process_commands("list_tests c")
    test_list_k = console.process_commands("list_tests k")
    tests = console.process_commands("list_tests_taken")
    scores = console.user.recent_scores()
    request.session[TEST_MODE] = FULL_TEST
    date = console.user.get_intended_date()
    goal = console.user.intended_score


    #test_list = ["GE29", "GE30", "GE31", "GE32"]
    return render(request, 'userauth/userpage.html', {'user':user, 'test_list_k':test_list_k,  'test_list_c':test_list_c, 'scores':scores, 'date':date, 'goal':goal ,'tests':tests, 'user_name':u_name})




