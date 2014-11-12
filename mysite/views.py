from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Library.Console import *
from Library.Values import *
from django.core.context_processors import csrf

c = Console()

def index(request):
	#return render(request, 'mysite/index_base.html')
	return render(request, 'mysite/index.html')

def extest(request):
	"""
	Test to see if we can call the console and new_class command from console.py in the Library
	"""
	# try:
	# 	c = Console();
	# 	val = c.process_commands("new_class Class")
	# 	if val == False:
	# 		response = c.error
	# 	else:
	# 		response = 'Successfully called excelerate function'
	# 	return render(request, 'mysite/tester.html', {'response': response})
	# except Exception as e:
	# 	response = 'Something went wrong: '
	# 	return render(request, 'mysite/tester.html', {'response':response, 'message':e})


	c = Console();
	val = c.process_commands("new_class Class")
	if val == False:
		response = c.error
	else:
		response = 'Successfully called excelerate function'
	return render(request, 'mysite/tester.html', {'response': response})

def reports(request):
	return render(request, 'web/klin/simple_report.html')

def formtest(request):
	"""
	Successfully using the form to input commands as if they were entered through the shell
	"""
	if request.POST:
		context = {}
		context.update(csrf(request))
		cmd = request.POST.get('cmd')
		print("hello try")
		try:
			print (cmd)
			c.process_commands(str(cmd))
			print "hello final"
			if c.error != None:
				response = "Error:" + c.error
			else:
				response = "Successfully called excelerate function: " + cmd
			return render(request, 'mysite/tester.html', {'response':response})
		except Exception as e:
			response = 'Something went wrong with command:' + cmd + ". Exception outputted: "
			return render(request, 'mysite/tester.html', {'response':response, 'message':e})
	else:
		response = 'Something wrong with post'
		return render(request, 'mysite/tester.html', {'response':response})



