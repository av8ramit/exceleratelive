# Testing suite for Analyze.py

from Analyze import *
from Values import *
from Key import *
from Scored import *
from Summary import *
from Data import *
from Graph import *
import csv
import sys

def readCommand(args):
	if (len(args) > 1):
		if (args[1].equals('--debug')):
			return True
		else:
			return False

def runTests(debug):

	analyzeTest = Analyze()
	analyzeTest.setDebug(debug)

	print ("\nRunning Analyze Tests")
	stanDevTestSet = [50, 60, 45, 35, 28, 30, 58, 70, 32, 80,
						90, 85, 75, 70, 50, 60, 70, 80, 35, 45]
	stanDevAns = 19.140010
	stanDevResult = analyzeTest.calculateSD(stanDevTestSet)
	print ("Running Standard Deviation Test. Answer should be %f, received %f" % (stanDevAns, stanDevResult))


def buildTestUser():
	testUser = User("analyzeTestUser")
	recreate_user(User.directory)

if __name__ == '__main__':
		debug = readCommand(sys.argv)   # True if we want to have debugging output printed out
		runTests(debug)