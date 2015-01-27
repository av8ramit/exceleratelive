####################################################################################################################################################  
#                                                                                                                                                  #
# This file has been generated by Amit Patankar:                                                                                                   #
#     Created by              : amit.patankar                                                                                                      #    
#     Created on              : 11-07-2013                                                                                                         #
#     Directory               : /Desktop/                                                                                                          #
#     Purpose                 : This structure holds the attributes of each section in a text.                                                     #
#                                                                                                                                                  #
#################################################################################################################################################### 

import csv
from Values import *
from Answer import *
from Summary import *

class Test(object):

    #This is the default constructor takes an id and constructs the test from a valid folder.
    def __init__(self, test_id):

        assert(file_exists(test_directory(test_id)))

        self.test_id = test_id
        self.sections = {}

        key = {}
        with open(test_directory(test_id) + DIR_SEP + KEYFILE, 'rU') as f:
            reader = csv.reader(f)
            for row in reader:
                if row != KEY_VECTOR:
                    key[row[0]] = (row[KEY_TYPE],row[KEY_SIZE])
        for number in key.keys():
            if number == '1': #essay
                es = Essay_Section(self)
                self.add_section(es)
            elif key[number][1] == '0': #trial
                ts = Trial_Section(self, int(number))
                self.add_section(ts)
            else: #real
                s = Section(self, int(number), int(key[number][0]))
                s.parse_questions(test_directory(test_id) + DIR_SEP + "Section " + number + ".csv")
                self.add_section(s)

    #This returns the selected section.
    def get_section(self, section_number):
        if (section_number > SECTION_COUNT or section_number < 1):
            print ("Error: Invalid section index. Indexes are from 1-10.")
            return
        return self.sections[section_number]

    #This adds a section to the test.
    def add_section(self, section):
        assert(type(section) == Section or type(section) == Trial_Section or type(section) == Essay_Section)
        self.sections[section.section_number] = section

    #This returns the test id.
    def get_id(self):
        return self.test_id

    #This prints an answer sheet that corresponds to the test_id given.
    """def make_answer_sheet(test_id):
        filename = test_id
        lines = []

        label_vector = "Number:,Answer:\n"
        lines.append(test_id + " Answer Sheet\n\n")
        lines.append(label_vector)

        with open(test_directory(test_id) + DIR_SEP + KEYFILE, 'rU') as f:
            reader = csv.reader(f)
            for row in reader:
                if row != KEY_VECTOR:

                    lines.append("Section " + str(row[0]) + ":" + endl)
                    for j in range(1,int(row[2]) + 1):
                        lines.append(str(j) + ",?")
                        lines.append(endl)

        FILE = open(test_id + ".csv", "w")
        FILE.writelines(lines)
        FILE.close()"""
        #moved to Commands

    #This grades a given answer sheet against the test.
    def grade(self, answered_test):
        del MISSED_QUESTIONS_LIST[:]
        #Miss Questions Page Number List
        del MISSED_QUESTIONS_PGNUM_LIST[:]
        #Missed Questions Section Number
        del MISSED_QUESTIONS_SECTION_LIST[:]
        #Missed Question User Answer List
        del MISSED_QUESTIONS_USRANSWER_LIST[:]
        del MISSED_QUESTIONS_TYPE_LIST[:]

        report = Test_Summary(self.get_id())
        assert (answered_test.id == self.get_id())
        self.essay = answered_test.essay
        self.date = answered_test.date
        for i in range(1,11):
            answered_section = answered_test.sections[i]
            answer_key = self.get_section(i)
            current_type = answer_key.type
            if current_type > MATH_TYPE:
                continue
            assert (answered_section.size() == answer_key.size())
            for j in range(1,answered_section.size()+1):
                attempt = answered_section.questions[j].answer
                answer = answer_key.get_question(j).answer
                if attempt == '?':
                    report.get_summary(current_type).add_blank()
                    report.get_summary(current_type).incorrect_questions.append((answer_key.get_question(j).get_id(),attempt))
                    #Missed Questions List
                    MISSED_QUESTIONS_LIST.append(answer_key.get_question(j).number)
                    #Miss Questions Page Number List
                    MISSED_QUESTIONS_PGNUM_LIST.append(answer_key.get_question(j).page)
                    #Missed Questions Section Number
                    MISSED_QUESTIONS_SECTION_LIST.append(answer_key.section_number)
                    #Missed Question User Answer List
                    MISSED_QUESTIONS_USRANSWER_LIST.append([attempt, answer])
                    MISSED_QUESTIONS_TYPE_LIST.append(answer_key.get_question(j).type)
                elif attempt == answer:
                    report.get_summary(current_type).add_answered()
                #range answer
                elif answer_key.get_question(j).range == 'Y' and '(' not in answer and ')' not in answer: #missed grid answers are counted as blanks
                    #assert ((attempt) not in 'ABCDE')
                    report.get_summary(current_type).add_blank()
                    report.get_summary(current_type).incorrect_questions.append((answer_key.get_question(j).get_id(),attempt))
                    #Missed Questions List
                    MISSED_QUESTIONS_LIST.append(answer_key.get_question(j).number)
                    #Miss Questions Page Number List
                    MISSED_QUESTIONS_PGNUM_LIST.append(answer_key.get_question(j).page)
                    #Missed Questions Section Number
                    MISSED_QUESTIONS_SECTION_LIST.append(answer_key.section_number)
                    #Missed Question User Answer List
                    MISSED_QUESTIONS_USRANSWER_LIST.append([attempt, answer])
                    MISSED_QUESTIONS_TYPE_LIST.append(answer_key.get_question(j).type)
                elif '(' in answer and ')' in answer:
                    answer = answer.replace(' ','')
                    answer = answer.replace('(','')
                    answer = answer.replace(')','')
                    lower_limit = float(answer.split(',')[0])
                    upper_limit = float(answer.split(',')[1])
                    try:
                        a = float(attempt)
                        if a <= upper_limit and a >= lower_limit:
                            report.get_summary(current_type).add_answered()
                        else:
                            report.get_summary(current_type).add_blank()
                            #Missed Questions List
                            MISSED_QUESTIONS_LIST.append(answer_key.get_question(j).number)
                            #Miss Questions Page Number List
                            MISSED_QUESTIONS_PGNUM_LIST.append(answer_key.get_question(j).page)
                            #Missed Questions Section Number
                            MISSED_QUESTIONS_SECTION_LIST.append(answer_key.section_number)
                            #Missed Question User Answer List
                            MISSED_QUESTIONS_USRANSWER_LIST.append([attempt, answer])
                            MISSED_QUESTIONS_TYPE_LIST.append(answer_key.get_question(j).type)
                            report.get_summary(current_type).incorrect_questions.append((answer_key.get_question(j).get_id(),attempt))
                    except:
                        report.get_summary(current_type).add_blank()
                        #Missed Questions List
                        MISSED_QUESTIONS_LIST.append(answer_key.get_question(j).number)
                        #Miss Questions Page Number List
                        MISSED_QUESTIONS_PGNUM_LIST.append(answer_key.get_question(j).page)
                        #Missed Questions Section Number
                        MISSED_QUESTIONS_SECTION_LIST.append(answer_key.section_number)
                        #Missed Question User Answer List
                        MISSED_QUESTIONS_USRANSWER_LIST.append([attempt, answer])
                        MISSED_QUESTIONS_TYPE_LIST.append(answer_key.get_question(j).type)
                        report.get_summary(current_type).incorrect_questions.append((answer_key.get_question(j).get_id(),attempt))
                else:
                    report.get_summary(current_type).add_miss()
                    #Missed Questions List
                    MISSED_QUESTIONS_LIST.append(answer_key.get_question(j).number)
                    #Miss Questions Page Number List
                    MISSED_QUESTIONS_PGNUM_LIST.append(answer_key.get_question(j).page)
                    #Missed Questions Section Number
                    MISSED_QUESTIONS_SECTION_LIST.append(answer_key.section_number)
                    #Missed Question User Answer List
                    MISSED_QUESTIONS_USRANSWER_LIST.append([attempt, answer])
                    MISSED_QUESTIONS_TYPE_LIST.append(answer_key.get_question(j).type)
                    report.get_summary(current_type).incorrect_questions.append((answer_key.get_question(j).get_id(),attempt))
        #disable printing report
        #print (report)
        return report

class Section(object):

    #This is the default constructor with all variables defined.
    def __init__(self, test, index, section_type):
        self.test = test
        self.section_number = index
        self.type = section_type
        self.questions = {}
        self.is_trial = False

    def add_question(self, question):
        assert(type(question) == Question)
        self.questions[question.number] = question

    #This selects the correct section.
    def parse_questions(self, filename):
        with open(filename, 'rU') as f:
            reader = csv.reader(f)
            for row in reader:
                if row != LABEL_VECTOR:
                    q = Question()
                    q.make_by_array(self, row)
                    self.add_question(q)

    #This returns the corresponding question.
    def get_question(self, index):
        if (index <= 0 or index > self.size()):
            print ("Error: Not a valid question number")
            return
        return self.questions[index]

    #This returns the section id.
    def get_id(self):
        return self.test.get_id() + FIELD_SEP + str(self.section_number)
        
    #This returns the size of the section.
    def size(self):
        return len(self.questions)

class Trial_Section(Section):

    #This is the default constructor with all variables defined.
    def __init__(self, test, index):
        self.test = test
        self.section_number = index
        self.is_trial = True
        self.type = TRIAL_TYPE
        self.questions = {}

class Essay_Section(Section):

    #This is the default constructor with all variables defined.
    def __init__(self, test):
        self.test = test
        self.section_number = ESSAY_SECTION_INDEX
        self.type = ESSAY_TYPE
        self.is_trial = False
        self.questions = {}

class Question(object):

    #This is the default constructor with all variables defined.
    def __init__(self):
        self.section = None
        self.number = None
        self.answer = None
        self.difficulty = None
        self.range = None
        self.type = None
        self.page = None

    #This is the default constructor with all variables defined.
    def make_by_array(self, section, array):
        self.section = section
        if len(array) != PARSED_ARRAY_SIZE:
            print ("Error: Invalid line in CSV")
            print (array)
            return

        self.number = int(array[NUMBER_INDEX])
        self.answer = array[ANSWER_INDEX]
        self.difficulty = int(array[DIFFICULTY_INDEX])
        self.range = array[RANGE_INDEX]
        self.type = array[TYPE_INDEX]
        self.page = array[PAGE_INDEX]

    #This returns the question id.
    def get_id(self):
        return self.section.get_id() + FIELD_SEP + str(self.number)
