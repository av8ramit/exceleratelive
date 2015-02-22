####################################################################################################################################################  
#                                                                                                                                                  #
# This file has been generated by Amit Patankar:                                                                                                   #
#     Created by              : amit.patankar                                                                                                      #    
#     Created on              : 08-08-2013                                                                                                         #
#     Directory               : /Desktop/                                                                                                          #
#     Purpose                 : This file holds all the command functions.                                                                         #
#                                                                                                                                                  #
#################################################################################################################################################### 

import csv
from Values import *
from Key import *
from Answer import *
from User import *
from Class import *
from Scored import *
import datetime
from random import randrange

def clear(n):
    for i in range(0,n):
        print (n)



def class_missed_qs_array(classname):
    X = []
    classnm = classname
    classwritingqs = []
    classreadingqs = []
    classmathqs = []
    section = []


    for name in classnm.students:
        filename = user_filename(name, classnm.name)
        u = load_user(name, filename, classnm.name)
        index = 0
        wqs = []
        rqs = []
        mqs = []
        del CLASS_MISSED_WRITING[:]
        del CLASS_MISSED_READING[:]
        del CLASS_MISSED_MATH[:]
        for test in u.tests_taken:
            wqs.append(test.missed_questions[WRITING_TYPE])
            rqs.append(test.missed_questions[READING_TYPE])
            mqs.append(test.missed_questions[MATH_TYPE])

            index = index + 1
        for q in (wqs[index-1]):
            question, answer = q
            classwritingqs.append(question) #add missed question object to class list
        
            
        for q in (rqs[index-1]):
            question, answer = q
            classreadingqs.append(question) #add missed question object to class list
            #print("r: " + question)
        for q in (mqs[index-1]):
            question, answer = q
            classmathqs.append(question) #add missed question object to class list    
            #print("m: " + question)

    for question in classwritingqs:
        frequency = classwritingqs.count(question)
        #print(str(frequency) + " writing " + question)
        if question in CLASS_MISSED_WRITING:
            pass
        else:
            CLASS_MISSED_WRITING.append(Class_Question(question,frequency)) 
        for i in range(frequency):
            classwritingqs.remove(question)
            

    for question in classreadingqs:
        frequency = classreadingqs.count(question)
        #print(str(frequency) + " r " + question)
        if question in CLASS_MISSED_READING:
            pass
        else:
            CLASS_MISSED_READING.append(Class_Question(question,frequency))
        for i in range(frequency):
            classreadingqs.remove(question)
            

    for question in classmathqs:
        frequency = classmathqs.count(question)
        #print(str(frequency) + " m " + question) 
        if question in CLASS_MISSED_MATH:
            pass
        else:
            CLASS_MISSED_MATH.append(Class_Question(question,frequency))
        for i in range(frequency):
            classmathqs.remove(question)
            


    CLASS_MISSED_WRITING.sort(key=lambda question: question.frequency, reverse = True)
    CLASS_MISSED_READING.sort(key=lambda question: question.frequency, reverse = True)
    CLASS_MISSED_MATH.sort(key=lambda question: question.frequency, reverse = True)

    '''
    for item in missedwriting:

        print(str(item.question) + " Frequency: " + str(item.frequency))

    print()
    for item in missedreading:

        print(str(item.question) +  " Frequency: " + str(item.frequency))
    print()
    for item in missedmath:

        print(str(item.question) + " Frequency: " + str(item.frequency))
    '''
def new_class(name):   #new class function creates a new class object with no students in it
    c = Class(name)      #instantiate class object 
    mkdir(class_directory(name))
    return c             #return class object - used in Console.py 

def load_class(name):   #load class function creates a new class object and then loads all applicable students
    c = Class(name)    #instantiate class object
    c.students = list_users_array(name) # assign array of student names as strings to class object's 'students' attribute
    return c            #return class object with all applicable users - used in Console.py


def new_user(name, c):    # new user function creates a user object and builds it
    #directory = user_directory(name, c)     
    #disable deleting old directory to make a new one
    #if (file_exists(directory)):
    #    rmdir(directory)
    
    u = User(name, c)   #instantiate a user object with parameters username and user's classname  
    u.build()        #call user object method build() from User.py
    return u           # return built user object - used in Console.py 


def load_user(name, filename, classname):   #load user function creates a user object and recreates user data
    u = User(name, classname)       #instantiate a user object with parameters username and user's classname 
    u.name = name         #assign user object 'name' attribute the username
    u.recreate_user(filename)  #call user object method recreate_user() from User.py
    return u                  #return recreated user object - used in Console.py 


def delete_user(name, c):   #delete user function removes the users directory
    rmdir(user_directory(name, c))            #removes directory

def grade(u, filename):  
    pa = parse_answers(filename)
    u.grade(pa)

def list_classes(): # function that returns an array of class names - used in GUI.py dropdown button
    array = []               
    a = os.listdir(class_directory(''))   # a is all classes in class directory
    for i in a:                            # for each class in all class directories 
        if i[0] == '.':
            continue
        if file_exists(class_directory(i)):  # if class exists 
            array.append(i)                    # add to array 
    return array                     #return array of class names 

def list_tests():
    #a = os.listdir(test_directory(''))
    #array = []
    #print ("Here are the available test_ids:")
    #for i in a:
    #    if valid_test_id(i):
    #        #print (i)
    #        if "CB" in i:
    #            array.append(i)
    #        elif "DiagK" in i:
    #            array.append(i)
    #        elif "K" in i:
    #            array.append(i)
    return ["CB1", "CB2", "CB3", "CB4", "CB5", "CB6", "CB7", "CB8", "CB9", "CB10", "DiagK", "K1", "K2", "K3"]


def cram():
    #directory = os.path.dirname(__file__)
    test_dir = os.listdir(test_directory(''))
    avoid = ['key.csv', 'math.csv', 'reading.csv', 'writing.csv']
    tests = ["CB1", "CB2", "CB3", "CB4", "CB5", "CB6", "CB7", "CB8", "CB9", "CB10", "DiagK", "K1", "K2", "K3"]
    #taken = []
    pool = []
    result = []
    num_mtypes = len(missed_types)

    #extra code for excluding tests that the user took already

    #gets which tests the user haven't taken yet
    #user_txt = os.path.join(directory, u_name + '.txt')
    #f = open(user_txt, 'r')
    #for line in f:
    #   if "TEST_ID:" in line:
    #       taken.append(line[9:].strip("\n"))
    #f.close()

    #removes taken tests from pool of viable tests
    #for tt in taken:
    #   tests.remove(tt)

    for x in tests:
        folder = os.path.join(test_dir, x)
        avail = os.listdir(folder)
        for y in avoid:
            avail.remove(y)
        for z in avail:
            section = os.path.join(folder, z)
            with open(section, 'rU') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[4] in missed_types:
                        pool.append([x + '_' + z.strip('Section ').strip('.csv') + '_' + row[0], row[5]])
    for i in range(10):
        rand = randrange(0,len(pool))
        result.append(pool[rand])
    return result


def list_users(c):
    array = []
    a = os.listdir(class_directory(c))
    return str(a)

def list_users_array(c):
    array = []
    a = os.listdir(class_directory(c))
    for i in a:
        if file_exists(user_filename(i, c)):
            array.append(i)
    return array

def make_answer_sheet(u, test_id, test_type = FULL_TEST):
    filename = test_id
    lines = []
    label_vector = "Number:,Answer:" + endl
    lines.append(test_id + " Answer Sheet" + endl)
    lines.append("Name:," + u.name + endl)
    lines.append("Date:," + datetime_converter(str(datetime.date.today())) + endl)
    lines.append("Type:," + test_type + endl)
    lines.append("Essay:,7" + endl)
    lines.append(label_vector)
    with open(test_directory(filename) + DIR_SEP + KEYFILE, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            if row != KEY_VECTOR:
                lines.append("Section " + str(row[0]) + ":" + endl)
                for j in range(1,int(row[2]) + 1):
                    if test_type == FULL_TEST:
                        lines.append(str(j) + "," + BLANK_ENTRY)
                    elif test_type == QUICK_SECTIONS:
                        lines.append(str(j) + "," + OMIT_ENTRY)
                    else:
                        #FAILSAFE in case test_type fails
                        assert(False)
                    lines.append(endl)
    FILE = open(user_directory(u.name, u.c) + DIR_SEP + test_id + ".csv", "w")
    FILE.writelines(lines)
    FILE.close()

## function that creates answer sheet csv with bubblesheet data from website
'''
def make_bubble_csv(u, test_id, bbldata):
    filename = test_id
    bubblesheetdata = []
    bubble_True_or_False = bbldata
    lines = []
    dataindex = 0
    label_vector = "Number:,Answer:" + endl
    lines.append(test_id + " Answer Sheet" + endl)
    lines.append("Name:," + u.name + endl)
    lines.append("Date:," + datetime_converter(str(datetime.date.today())) + endl)
    lines.append("Essay:,"+ str(bubblesheetdata.pop()) + endl)
    lines.append(label_vector)
    with open(test_directory(filename) + DIR_SEP + KEYFILE, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            if row != KEY_VECTOR:
                lines.append("Section " + str(row[0]) + ":" + endl)
                for j in range(1,int(row[2]) + 1):
                    lines.append(str(j) + "," + str(bubblesheetdata.pop()))
                    lines.append(endl)
    FILE = open(user_directory(u.name, u.c) + DIR_SEP + test_id + ".csv", "w")
    FILE.writelines(lines)
    FILE.close()

'''

def make_bubble_sheet_omit(u, test_id):
    filename = test_id
    lines = []
    
    lines.append('<!DOCTYPE html>' + endl)
    lines.append('<head>')
    lines.append('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />' + endl)
    lines.append('{% load staticfiles %}' + endl)
    lines.append('<link rel="stylesheet" type="text/css" href=' + '"' + "{% static 'style.css' %}" + '"' + '/>' + endl)
    lines.append('<link rel="stylesheet" href=' + '"' + "{% static 'flipclock.css' %}" + '"' +'/>' + endl)
    lines.append('<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>' + endl)
    lines.append('<script src='+ '"' + "{% static 'flipclock.js' %}" + '"' +'></script>' +endl)
    lines.append('<title>' + str(filename) +  '</title>' + endl)
    lines.append('<br></br>')
    lines.append('</head>' + endl)
    lines.append('<body>' + endl)
    lines.append('<style>' + endl)
    lines.append('html,' + endl)
    lines.append('body {' + endl)
    lines.append('background-image: url("{% static' +  " 'mysite/css/images/overlay.svg' " +  '%}");')
    lines.append('background-size: 100%;' + endl)
    lines.append('}' + endl)
    lines.append('</style>' + endl)  
    lines.append('<div id="page">' + endl)
    lines.append('<div id="header">' + endl)
    lines.append('<img src=' + '"' + "{% static 'ml.png' %}" + '" alt="Excelerate" style="float: right; width: 35%; margin-right: 35%;"/>' +
        '<a href="javascript:history.go(-2)"> <img src=' + '"' + "{% static 'back_rev.png' %}" + '" alt="Home" style="float: left; width: 15%; margin-left: 5%;""> </a>' + endl)
    lines.append('<p style="clear: both;">' + endl)
    lines.append('</div>' + endl)
    lines.append('</div>' + endl)
    lines.append('<div id="content">' + endl)
    lines.append('<div id="container">' + endl)
    lines.append('<div id="main">' + endl)
    lines.append('<div id="menu">' + endl)
    lines.append('<h2 style="text-align:center;">Bubble Answer Sheet</h2>' + endl)
    lines.append('</div>' + endl)
    lines.append('<div id="text">' + endl)
    lines.append('<h1 style = "text-align: center;color: #FF8C00"> Test:  ' + str(filename) + ' </h1>' +endl) 
    lines.append('<p style = "text-align: justify;color: #348cb2"> &nbsp &nbsp &nbsp &nbsp Please set aside a 4 hour time slot to complete this practice exam. Use the optional timers for each section to help you keep track and proctor your exam. Either fill in the bubble answer sheet as you take the test with the built in timers for each section, or fill in the bubble sheet with answers from a test you have already taken. Upon completion, click the "Submit and Grade Test" button at the end of the answer sheet. Practice makes perfect, but also remember to take three, five-minute breaks! Goodluck!</p>' + endl)
    #lines.append('<p style = "text-align: justify;color: #348cb2">Either fill in the bubble answer sheet as you take the test with the built in timers for each section, or fill in the bubble sheet with answers from a test you have already taken.</p>' + endl)
    #lines.append('<p style = "text-align: justify;color: #348cb2">Upon completion, click the "Submit and Grade Test" button at the end of the answer sheet.</p>' + endl)
    #lines.append('<p style = "text-align: justify;color: #348cb2">Practice makes perfect, but also remember to take three, five-minute breaks! <br> Goodluck!</p>' + endl)
    lines.append('<br/>'+ endl)
    lines.append('<br/>'+ endl)
    lines.append('<h3 style="text-align:center;color: #FF8C00">If you begin now, your estimated time of completion is:</h3>' + endl)
    lines.append('<div class="clock" style="margin:1em;"></div>' + endl)
    lines.append('<script type="text/javascript">' + endl)
    lines.append('var clock;' + endl)
    lines.append('$(document).ready(function() {' + endl)
    lines.append('var date = new Date();' + endl)
    lines.append('var hours = date.getHours();' + endl)
    lines.append('var mins = date.getMinutes();' + endl)
    lines.append('date.setHours(hours+3);' + endl)
    lines.append('date.setMinutes(mins+35);' + endl)
    lines.append('clock = $('+ "'" +'.clock' + "'" + ').FlipClock(date, {' + endl)
    lines.append('clockFace: '+ "'" + 'TwelveHourClock' + "'" + endl)
    lines.append('});' + endl)
    lines.append('});' + endl)
    lines.append('</script>' + endl)
    lines.append('<br/>'+ endl)
    lines.append('<br/>'+ endl)
    lines.append('<form style = "text-align: center" role="form" ' + 'action=' + '"' + '{% url ' + "'" + 'login:grade_bubblesheet' + "'" + ' %}' +  '"' +  '" method="post">{% csrf_token %}' + endl)
    lines.append('<input type = "hidden" name = "test" value=' + '"' + str(filename) + '"' +' />' + endl)
    divclk = 1
    with open(test_directory(filename) + DIR_SEP + KEYFILE, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            if row != KEY_VECTOR:
                lines.append('<h2 style = "color: #FF8C00"> Section ' +  str(row[0])  +  ' : </h2>' + endl)
                if(int(row[1]) == ESSAY_TYPE): # if essay type
                    lines += make_section_cntdwnclock(25, divclk)
                    divclk += 1
                    lines.append('<br/>' + endl)
                    lines.append('<br/>' + endl)
                    lines.append('<label style = "color: #348cb2"> Enter Essay Score from 2 to 12 </label>' + endl)
                    lines.append('<br/>' + endl)
                    lines.append('<br/>' + endl)
                    lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
                    lines.append('<input type="text" name=' + '"' + 'Essay' + '"' +  'value="7"/>' + endl)
                    lines.append('<br/>' + endl)
                if(int(row[2]) == 18 and int(row[1]) == READING_TYPE): #college board test 2 18 q reading section mistake clock
                    lines += make_section_cntdwnclock(20, divclk)
                    divclk += 1
                if(int(row[2]) == 25): #college board test 2 25 q reading section mistake clock
                    lines += make_section_cntdwnclock(25, divclk)
                    divclk += 1
                if(int(row[2]) == 18 and int(row[1]) == MATH_TYPE): # special section math 8 MC  10 grid-in s
                    #math 18 question section timer 
                    lines += make_section_cntdwnclock(25, divclk)
                    divclk += 1
                    for i in range(1,int(row[2]) + 1):  
                        if(i <= 8): # Math MC
                            lines+= make_bubble_question_omit('Section ' +  str(row[0]) + '  Question ' + str(i), True)
                        else:
                            lines+= make_bubble_question_omit('Section ' +  str(row[0]) + '  Question ' + str(i), False)
                        if(i == 8):
                            lines.append('<p style = "text-align: center;color: #348cb2"> <br>Math Grid-In <br>For the fill in math answer sheet when given a ratio answer leave it as a decimal and round up to at most 2 decimal places.</p>')
                else: #regular section math, reading, writing MC
                    if (int(row[2])  == 16 or int(row[2]) == 19):  #16q and 19q section, 20 min timer
                        lines += make_section_cntdwnclock(20, divclk)
                        divclk += 1
                    if(int(row[2]) == 35 or int(row[2]) == 24 or int(row[2]) == 20):
                        lines += make_section_cntdwnclock(25, divclk)
                        divclk += 1
                    if(int(row[2]) == 14): 
                        lines += make_section_cntdwnclock(10, divclk)
                        divclk += 1

                    for i in range(1,int(row[2]) + 1):

                        lines+= make_bubble_question_omit('Section ' +  str(row[0]) + '  Question ' + str(i), True) 

    lines.append('<br>' + endl)
    lines.append('<br>' + endl)
    lines.append('<br>' + endl)
    lines.append('<br>' + endl)                    
    lines.append('<input onClick="return confirm(' + "'" + 'Ready to submit test?'  + "'" +');" type = "submit" name = "submit" value = "Submit and Grade Test" />' + endl)          
    #Footer
    lines.append('<br>' + endl)
    lines.append('</div>' + endl)
    lines.append('</div>' + endl)
    lines.append('</div>' + endl)
    lines.append('<div class="clear"></div>' + endl)
    lines.append('<div id="footer">' + endl)
    lines.append('</div>' + endl)
    lines.append('</div>' + endl)
    lines.append('</body>' + endl)
    lines.append('</html>' + endl)
    lines.append(endl)            
    FILE = open(user_directory(u.name, u.c) + DIR_SEP + test_id + ".html", "w")
    FILE.writelines(lines)
    FILE.close()

def make_bubble_question_omit(question_number, bubble_True_or_False):
    lines = []
    qnum = question_number
    bbltf = bubble_True_or_False
    if(not bbltf):
        #math grid in 
        lines.append('<br/>' + endl)
        lines.append('<label style = "color: #348cb2">' + str(qnum) + '</label>' + endl)
        lines.append('<br/>' + endl)
        lines.append('<br/>' + endl)
        lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
        lines.append('<input type="text" name=' + '"' + str(qnum) + '"' +  'value="O"/>' + endl)
        lines.append('<br/>' + endl)
        return(lines)

    else:
        # MC 
        lines.append('<br/>' + endl)
        lines.append('<label style = "color: #348cb2">' + str(qnum) + '</label>' + endl)
        lines.append('<br/>' + endl)
        lines.append('<br/>' + endl)
        lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
        lines.append('<input type="radio" name=' + '"' + str(qnum) + '"' +  'value="A"/>   A' + endl)
        lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
        lines.append('<input type="radio" name=' + '"' + str(qnum) + '"' +  'value="B"/>   B' + endl)
        lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
        lines.append('<input type="radio" name=' + '"' + str(qnum) + '"' +  'value="C"/>   C' + endl)
        lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
        lines.append('<input type="radio" name=' + '"' + str(qnum) + '"' +  'value="D"/>   D' + endl)
        lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
        lines.append('<input type="radio" name=' + '"' + str(qnum) + '"' +  'value="E"/>   E' + endl)
        lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
        lines.append('<input type="radio" name=' + '"' + str(qnum) + '"' +  'value="?"/>   BLANK' + endl)
        lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
        lines.append('<input type="radio" name=' + '"' + str(qnum) + '"' +  'value="O"checked/>   OMIT' + endl)
        lines.append('<br/>' + endl)
        return(lines)



## function that creates HTML page Bubble Sheet to input answers
def make_bubble_sheet(u, test_id):
    filename = test_id
    lines = []
    
    lines.append('<!DOCTYPE html>' + endl)
    lines.append('<head>')
    lines.append('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />' + endl)
    lines.append('{% load staticfiles %}' + endl)
    lines.append('<link rel="stylesheet" type="text/css" href=' + '"' + "{% static 'style.css' %}" + '"' + '/>' + endl)
    lines.append('<link rel="stylesheet" href=' + '"' + "{% static 'flipclock.css' %}" + '"' +'/>' + endl)
    lines.append('<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>' + endl)
    lines.append('<script src='+ '"' + "{% static 'flipclock.js' %}" + '"' +'></script>' +endl)
    lines.append('<title>' + str(filename) +  '</title>' + endl)
    lines.append('<br></br>')
    lines.append('</head>' + endl)
    lines.append('<body>' + endl)
    lines.append('<style>' + endl)
    lines.append('html,' + endl)
    lines.append('body {' + endl)
    lines.append('background-image: url("{% static' +  " 'mysite/css/images/overlay.svg' " +  '%}");')
    lines.append('background-size: 100%;' + endl)
    lines.append('}' + endl)
    lines.append('</style>' + endl)  
    lines.append('<div id="page">' + endl)
    lines.append('<div id="header">' + endl)
    lines.append('<img src=' + '"' + "{% static 'ml.png' %}" + '" alt="Excelerate" style="float: right; width: 35%; margin-right: 35%;"/>' +
        '<a href="javascript:history.go(-1)"> <img src=' + '"' + "{% static 'back_rev.png' %}" + '" alt="Home" style="float: left; width: 15%; margin-left: 5%;""> </a>' + endl)
    lines.append('<p style="clear: both;">' + endl)
    lines.append('</div>' + endl)
    lines.append('</div>' + endl)
    lines.append('<div id="content">' + endl)
    lines.append('<div id="container">' + endl)
    lines.append('<div id="main">' + endl)
    lines.append('<div id="menu">' + endl)
    lines.append('<h2 style="text-align:center;">Bubble Answer Sheet</h2>' + endl)
    lines.append('</div>' + endl)
    lines.append('<div id="text">' + endl)
    lines.append('<h1 style = "text-align: center;color: #FF8C00"> Test:  ' + str(filename) + ' </h1>' +endl) 
    lines.append('<p style = "text-align: justify;color: #348cb2"> &nbsp &nbsp &nbsp &nbsp Please set aside a 4 hour time slot to complete this practice exam. Use the optional timers for each section to help you keep track and proctor your exam. Either fill in the bubble answer sheet as you take the test with the built in timers for each section, or fill in the bubble sheet with answers from a test you have already taken. Upon completion, click the "Submit and Grade Test" button at the end of the answer sheet. Practice makes perfect, but also remember to take three, five-minute breaks! Goodluck!</p>' + endl)
    #lines.append('<p style = "text-align: justify;color: #348cb2">Either fill in the bubble answer sheet as you take the test with the built in timers for each section, or fill in the bubble sheet with answers from a test you have already taken.</p>' + endl)
    #lines.append('<p style = "text-align: justify;color: #348cb2">Upon completion, click the "Submit and Grade Test" button at the end of the answer sheet.</p>' + endl)
    #lines.append('<p style = "text-align: justify;color: #348cb2">Practice makes perfect, but also remember to take three, five-minute breaks! <br> Goodluck!</p>' + endl)
    lines.append('<br/>'+ endl)
    lines.append('<br/>'+ endl)
    lines.append('<h3 style="text-align:center;color: #FF8C00">If you begin now, your estimated time of completion is:</h3>' + endl)
    lines.append('<div class="clock" style="margin:1em;"></div>' + endl)
    lines.append('<script type="text/javascript">' + endl)
    lines.append('var clock;' + endl)
    lines.append('$(document).ready(function() {' + endl)
    lines.append('var date = new Date();' + endl)
    lines.append('var hours = date.getHours();' + endl)
    lines.append('var mins = date.getMinutes();' + endl)
    lines.append('date.setHours(hours+3);' + endl)
    lines.append('date.setMinutes(mins+35);' + endl)
    lines.append('clock = $('+ "'" +'.clock' + "'" + ').FlipClock(date, {' + endl)
    lines.append('clockFace: '+ "'" + 'TwelveHourClock' + "'" + endl)
    lines.append('});' + endl)
    lines.append('});' + endl)
    lines.append('</script>' + endl)
    lines.append('<br/>'+ endl)
    lines.append('<br/>'+ endl)
    lines.append('<form style = "text-align: center" role="form" ' + 'action=' + '"' + '{% url ' + "'" + 'login:grade_bubblesheet' + "'" + ' %}' +  '"' +  '" method="post">{% csrf_token %}' + endl)
    lines.append('<input type = "hidden" name = "test" value=' + '"' + str(filename) + '"' +' />' + endl)
    divclk = 1
    with open(test_directory(filename) + DIR_SEP + KEYFILE, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            if row != KEY_VECTOR:
                lines.append('<h2 style = "color: #FF8C00"> Section ' +  str(row[0])  +  ' : </h2>' + endl)
                if(int(row[1]) == ESSAY_TYPE): # if essay type
                    lines += make_section_cntdwnclock(25, divclk)
                    divclk += 1
                    lines.append('<br/>' + endl)
                    lines.append('<br/>' + endl)
                    lines.append('<label style = "color: #348cb2"> Enter Essay Score from 2 to 12 </label>' + endl)
                    lines.append('<br/>' + endl)
                    lines.append('<br/>' + endl)
                    lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
                    lines.append('<input type="text" name=' + '"' + 'Essay' + '"' +  'value="7"/>' + endl)
                    lines.append('<br/>' + endl)
                if(int(row[2]) == 18 and int(row[1]) == READING_TYPE): #college board test 2 18 q reading section mistake clock
                    lines += make_section_cntdwnclock(20, divclk)
                    divclk += 1
                if(int(row[2]) == 25): #college board test 2 25 q reading section mistake clock
                    lines += make_section_cntdwnclock(25, divclk)
                    divclk += 1
                if(int(row[2]) == 18 and int(row[1]) == MATH_TYPE): # special section math 8 MC  10 grid-in s
                    #math 18 question section timer 
                    lines += make_section_cntdwnclock(25, divclk)
                    divclk += 1
                    for i in range(1,int(row[2]) + 1):  
                        if(i <= 8): # Math MC
                            lines+= make_bubble_question('Section ' +  str(row[0]) + '  Question ' + str(i), True)
                        else: # Math Grid-In
                            lines+= make_bubble_question('Section ' +  str(row[0]) + '  Question ' + str(i), False)
                        if(i == 8):
                            lines.append('<p style = "text-align: center;color: #348cb2"> <br>Math Grid-In <br>For the fill in math answer sheet when given a ratio answer leave it as a decimal and round up to at most 2 decimal places.</p>')
                else: #regular section math, reading, writing MC
                    if (int(row[2])  == 16 or int(row[2]) == 19):  #16q and 19q section, 20 min timer
                        lines += make_section_cntdwnclock(20, divclk)
                        divclk += 1
                    if(int(row[2]) == 35 or int(row[2]) == 24 or int(row[2]) == 20):
                        lines += make_section_cntdwnclock(25, divclk)
                        divclk += 1
                    if(int(row[2]) == 14): 
                        lines += make_section_cntdwnclock(10, divclk)
                        divclk += 1

                    for i in range(1,int(row[2]) + 1):

                        lines+= make_bubble_question('Section ' +  str(row[0]) + '  Question ' + str(i), True) 

    lines.append('<br>' + endl)
    lines.append('<br>' + endl)
    lines.append('<br>' + endl)
    lines.append('<br>' + endl)                    
    lines.append('<input onClick="return confirm(' + "'" + 'Ready to submit test?'  + "'" +');" type = "submit" name = "submit" value = "Submit and Grade Test" />' + endl)          
    #Footer
    lines.append('<br>' + endl)
    lines.append('</div>' + endl)
    lines.append('</div>' + endl)
    lines.append('</div>' + endl)
    lines.append('<div class="clear"></div>' + endl)
    lines.append('<div id="footer">' + endl)
    lines.append('</div>' + endl)
    lines.append('</div>' + endl)
    lines.append('</body>' + endl)
    lines.append('</html>' + endl)
    lines.append(endl)            
    FILE = open(user_directory(u.name, u.c) + DIR_SEP + test_id + ".html", "w")
    FILE.writelines(lines)
    FILE.close()

def make_bubble_question(question_number, bubble_True_or_False):
    lines = []
    qnum = question_number
    bbltf = bubble_True_or_False
    if(not bbltf):
        #math grid in 
        lines.append('<br/>' + endl)
        lines.append('<label style = "color: #348cb2">' + str(qnum) + '</label>' + endl)
        lines.append('<br/>' + endl)
        lines.append('<br/>' + endl)
        lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
        lines.append('<input type="text" name=' + '"' + str(qnum) + '"' +  'value="?"/>' + endl)
        lines.append('<br/>' + endl)
        return(lines)

    else:
        # MC 
        lines.append('<br/>' + endl)
        lines.append('<label style = "color: #348cb2">' + str(qnum) + '</label>' + endl)
        lines.append('<br/>' + endl)
        lines.append('<br/>' + endl)
        lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
        lines.append('<input type="radio" name=' + '"' + str(qnum) + '"' +  'value="A"/>   A' + endl)
        lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
        lines.append('<input type="radio" name=' + '"' + str(qnum) + '"' +  'value="B"/>   B' + endl)
        lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
        lines.append('<input type="radio" name=' + '"' + str(qnum) + '"' +  'value="C"/>   C' + endl)
        lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
        lines.append('<input type="radio" name=' + '"' + str(qnum) + '"' +  'value="D"/>   D' + endl)
        lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
        lines.append('<input type="radio" name=' + '"' + str(qnum) + '"' +  'value="E"/>   E' + endl)
        lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
        lines.append('<input type="radio" name=' + '"' + str(qnum) + '"' +  'value="?" checked />   BLANK' + endl)
        lines.append('<br/>' + endl)
        return(lines)

#countdown clock for sections of the test 
def make_section_cntdwnclock(time_minutes, index):
    timevar = time_minutes * 60
    divindex = index 
    #countdown clock
    lines = []
    lines.append('<br>' + endl)
    lines.append('<br>' + endl)
    lines.append('<label style = "color: #348cb2">Optional timer: To help you keep track of time and/or to proctor your exam</label>' + endl)
    lines.append('<br>' + endl)
    lines.append('<br>' + endl)
    lines.append('<div  style="text-align:right" class="clock' + str(divindex) + '"' + ' style="margin:1em;"></div>' + endl)
    lines.append('<br>' + endl)
    lines.append('<br>' + endl)
    lines.append('<br>' + endl)
    lines.append('<br>' + endl)
    lines.append('<div style = "color: #348cb2" class="message' + str(divindex) + '"></div>' + endl)
    lines.append('<button type = "button" class="start'  + str(divindex) + '">Start Section Timer</button>' + endl)
    lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
    lines.append('<button type = "button" class="stop'  + str(divindex) + '">Stop Section Timer</button>' + endl)
    lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
    lines.append('<button type = "button" class="reset'  + str(divindex) + '">Reset Section Timer</button>' + endl)
    lines.append('&nbsp;&nbsp;&nbsp;&nbsp;' + endl)
    lines.append('<script type="text/javascript">' + endl)
    lines.append('var clock' + str(divindex) + ';' + endl)
    lines.append('$(document).ready(function() {' + endl)
    lines.append('clock' + str(divindex) + ' = $('+ "'" + '.clock' + str(divindex) + "'" + ').FlipClock( ' + str(timevar) + ', {' + endl)
    lines.append('clockFace: ' + "'" + 'MinuteCounter' + "'" + ',' + endl)
    lines.append('countdown: true,' + endl)
    lines.append('autoStart: false,' + endl)
    lines.append('callbacks: {' + endl)
    lines.append('start'+ str(divindex) +': function() {' + endl)
    lines.append('$('+ "'" +'.message' + str(divindex) + "'" + ').html(' + "'" + 'Being the section' + "'" + ')},' + endl)
    lines.append('stop'+ str(divindex) +': function() {' + endl)
    lines.append('$('+ "'" +'.message' + str(divindex) + "'" + ').html(' + "'" + 'The timer has been paused' + "'" + ')},' + endl)
    lines.append('reset'+ str(divindex) +': function() {' + endl)
    lines.append('$('+ "'" +'.message' + str(divindex) + "'" + ').html(' + "'" + 'Being the section!' + "'" + ');' + endl)
    lines.append('}' + endl)
    lines.append('}' + endl)
    lines.append('});' + endl)
    lines.append('$(' + "'" + '.start' + str(divindex)+ "'" +').click(function(e) {' + endl)
    lines.append('clock' + str(divindex) + '.start();' + endl)
    lines.append('});' + endl)
    lines.append('$(' + "'" + '.stop' + str(divindex)+ "'" +').click(function(e) {' + endl)
    lines.append('clock' + str(divindex) + '.stop();' + endl)
    lines.append('});' + endl)
    lines.append('$(' + "'" + '.reset' + str(divindex)+ "'" +').click(function(e) {' + endl)
    lines.append('clock' + str(divindex) + '.stop();' + endl)
    lines.append('clock' + str(divindex) + '.reset();' + endl)
    lines.append('clock' + str(divindex) + '.start();' + endl)
    lines.append('});' + endl)
    lines.append('});' + endl)
    lines.append('</script>' + endl)
    lines.append('<br>' + endl)
    lines.append('<br>' + endl)
    return lines




def parse_answers(filename):
    with open(filename, 'rU') as f:
        reader = csv.reader(f)
        id_set = False
        counter = 1
        test = None
        current_section = None

        for row in reader:
            counter +=1
            if row == ANSWER_VECTOR:
                continue
            elif row == []:
                continue
            elif row[0] == "Name:":
                test.add_name(row[1])
            elif row[0] == "Date:":
                test.add_date(row[1])
            elif row[0] == "Essay:":
                test.add_essay(int(row[1]))
            elif row[0] == "Type:":
                test.add_type(int(row[1]))
                print("TYPE NOW IS:" + str(test.type))
            elif row[0] == "": #blanks
                continue
            elif not id_set:
                test_id = row[0].split(' ')[0]
                id_set = True
                test = Answered_Test(test_id)

            elif len(row) > 0 and row[0].split(' ')[0] == "Section":
                index = row[0].split(' ')[1][:-1]
                if current_section != None:
                    test.add_section(current_section)

                current_section = Answered_Section(int(index))

            elif len(row) != 0:
                q_num = int(row[0])
                answer = row[1]
                q = Answered_Question(q_num, answer)
                current_section.add_question(q)
    test.add_section(current_section)
    return test

def simple_report(u):
    u.simple_HTML()

def advanced_report(u):
    u.advanced_HTML()

def graph_report(u):
    u.graph_HTML()

def section_report(u):
    u.section_HTML(WRITING_TYPE)
    u.section_HTML(READING_TYPE)
    u.section_HTML(MATH_TYPE)

def tests_taken(u):
    array = []
    count = 1
    for test in u.tests_taken:
        array.append(str(count) + ". " + TEST_LIB_DICT[test.test_id] + "   |   Date: " + test.date)
        count += 1
    return array



#def valid_test(filename):
    
