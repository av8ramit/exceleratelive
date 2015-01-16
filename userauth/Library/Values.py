import os
import shutil
import random

#License Information
USER_LIMIT = 25
#Year/Month/Day
EXPIRATION_DATE = '2015/12/15'
date_of_expiration = '12/15/2015'

def date_converter(datestring):
  datestring = datestring.split('/')
  if len(datestring[2]) == 2:
    datestring[2] = '20' + datestring[2]
  return (datestring[2] + '-' + datestring[0] + '-' + datestring[1])

def datetime_converter(datestring):
  year = 0
  month = 1
  day = 2
  datestring = datestring.split('-')
  return datestring[month] + '/' + datestring[day] + '/' + datestring[year]

#Question Value
PARSED_ARRAY_SIZE = 6

NUMBER_INDEX = 0
ANSWER_INDEX = 1
DIFFICULTY_INDEX = 2
RANGE_INDEX = 3
TYPE_INDEX = 4
PAGE_INDEX = 5

#Section Value
ESSAY_SECTION_INDEX = 1
LABEL_VECTOR = ['Number', 'Answer', 'Difficulty', 'Range', 'Type', 'Page']
READING_TYPE = 0
WRITING_TYPE = 1
MATH_TYPE = 2
ESSAY_TYPE = 3
TRIAL_TYPE = 4
SECTION_COUNT = 10
READING_SIZE = 67
MATH_SIZE = 54
WRITING_SIZE = 49

#Grading Value
GRADED_ARRAY_SIZE = 5
SECTION_ID_INDEX = 0
CA_INDEX = 1
IA_INDEX = 2
DIFF_INDEX = 3
QTYPE_INDEX = 4

#ID Value
FIELD_SEP = '_'

#Report Value
SECTION_SEP = "----------------------------------------------------------------------------------------------------"

#File Extensions
CSV = ".csv"
TXT = ".txt"

endl = "\n"

#Directory Values
DIR_SEP = "/"
PAR_DIR = ".."

#File Value
KEY_VECTOR = ['Section:', 'Type:', 'Size:']
KEYFILE = "key.csv"
SCOREFILE = "score.csv"
MATH_SCOREFILE = "math.csv"
WRITING_SCOREFILE = "writing.csv"
READING_SCOREFILE = "reading.csv"
KEY_INDEX = 0
KEY_TYPE = 1
KEY_SIZE = 2
ANSWER_VECTOR = ['Number:', 'Answer:']
SCORE_VECTOR = ['Raw Score:', 'Writing', 'Math', 'Reading']

#CHARACTER VALUES
SPACE = ' '

#CONSOLE VALUES
COMMAND_INDEX = 0
LAUNCH_STATE = 0
CLASS_STATE = 1
USER_STATE = 2
PROMPT = ">>> "


TYPE_ARRAY = [WRITING_TYPE, MATH_TYPE, READING_TYPE]

#QUESTION TYPE VALUES

#WRITING
WRITING_TYPES = 3
WRITING_SUB_TYPES = 22

WRITING_TYPE_1 = "W1"
WRITING_TYPE_11 = "W11"
WRITING_TYPE_12 = "W12"
WRITING_TYPE_13 = "W13"
WRITING_TYPE_14 = "W14"
WRITING_TYPE_15 = "W15"
WRITING_TYPE_16 = "W16"
WRITING_TYPE_17 = "W17"
WRITING_TYPE_18 = "W18"
WRITING_TYPE_19 = "W19"


WRITING_TYPE_2 = "W2"
WRITING_TYPE_21 = "W21"
WRITING_TYPE_22 = "W22"
WRITING_TYPE_23 = "W23"
WRITING_TYPE_24 = "W24"
WRITING_TYPE_25 = "W25"
WRITING_TYPE_26 = "W26"
WRITING_TYPE_27 = "W27"
WRITING_TYPE_28 = "W28"
WRITING_TYPE_29 = "W29"


WRITING_TYPE_3 = "W3"
WRITING_TYPE_31 = "W31"
WRITING_TYPE_32 = "W32"
WRITING_TYPE_33 = "W33"
WRITING_TYPE_34 = "W34"

WRITING_TYPE_DICT = {}
WRITING_TYPE_DICT[WRITING_TYPE_1] = "Sentence Revision"
WRITING_TYPE_DICT[WRITING_TYPE_11] = "Analogous Phrases"
WRITING_TYPE_DICT[WRITING_TYPE_12] = "Conjunctions and Compound Sentences"
WRITING_TYPE_DICT[WRITING_TYPE_13] = "Noun-Pronoun-Possessive Noun Agreement"
WRITING_TYPE_DICT[WRITING_TYPE_14] = "Indirect and Direct Objects"
WRITING_TYPE_DICT[WRITING_TYPE_15] = "Noun Singular vs Plural Agreement"
WRITING_TYPE_DICT[WRITING_TYPE_16] = "Verb Tense Agreement"
WRITING_TYPE_DICT[WRITING_TYPE_17] = "Adjectives and Adverbs"
WRITING_TYPE_DICT[WRITING_TYPE_18] = "Clauses and Prepositional Phrases"
WRITING_TYPE_DICT[WRITING_TYPE_19] = "No Error"

WRITING_TYPE_DICT[WRITING_TYPE_2] = "Spot the Error"
WRITING_TYPE_DICT[WRITING_TYPE_21] = "No Error"
WRITING_TYPE_DICT[WRITING_TYPE_22] = "Analogous Phrases"
WRITING_TYPE_DICT[WRITING_TYPE_23] = "Conjunctions and Compound Sentences"
WRITING_TYPE_DICT[WRITING_TYPE_24] = "Noun-Pronoun-Possessive Noun Agreement"
WRITING_TYPE_DICT[WRITING_TYPE_25] = "Indirect and Direct Objects"
WRITING_TYPE_DICT[WRITING_TYPE_26] = "Noun Singular vs Plural Agreement"
WRITING_TYPE_DICT[WRITING_TYPE_27] = "Verb Tense Agreement"
WRITING_TYPE_DICT[WRITING_TYPE_28] = "Adjectives and Adverbs"
WRITING_TYPE_DICT[WRITING_TYPE_29] = "Clauses and Prepositional Phrases"

WRITING_TYPE_DICT[WRITING_TYPE_3] = "Paragraph Revision"
WRITING_TYPE_DICT[WRITING_TYPE_31] = "Best Reproduced Sentence"
WRITING_TYPE_DICT[WRITING_TYPE_32] = "Revise and Combine"
WRITING_TYPE_DICT[WRITING_TYPE_33] = "Context Revision"
WRITING_TYPE_DICT[WRITING_TYPE_34] = "Purpose of Context"

#MATH
MATH_TYPES = 4
MATH_SUB_TYPES = 52

MATH_TYPE_1 = "M1"
MATH_TYPE_11 = "M11"
MATH_TYPE_12 = "M12"
MATH_TYPE_13 = "M13"
MATH_TYPE_14 = "M14"
MATH_TYPE_15 = "M15"
MATH_TYPE_16 = "M16"
MATH_TYPE_17 = "M17"
MATH_TYPE_18 = "M18"
MATH_TYPE_19 = "M19"
MATH_TYPE_1A = "M1A"
MATH_TYPE_1B = "M1B"
MATH_TYPE_1C = "M1C"
MATH_TYPE_1D = "M1D"
MATH_TYPE_1E = "M1E"

MATH_TYPE_2 = "M2"
MATH_TYPE_21 = "M21"
MATH_TYPE_22 = "M22"
MATH_TYPE_23 = "M23"
MATH_TYPE_24 = "M24"
MATH_TYPE_25 = "M25"
MATH_TYPE_26 = "M26"
MATH_TYPE_27 = "M27"
MATH_TYPE_28 = "M28"
MATH_TYPE_29 = "M29"
MATH_TYPE_2A = "M2A"
MATH_TYPE_2B = "M2B"
MATH_TYPE_2C = "M2C"
MATH_TYPE_2D = "M2D"
MATH_TYPE_2E = "M2E"
MATH_TYPE_2F = "M2F"

MATH_TYPE_3 = "M3"
MATH_TYPE_31 = "M31"
MATH_TYPE_32 = "M32"
MATH_TYPE_33 = "M33"
MATH_TYPE_34 = "M34"
MATH_TYPE_35 = "M35"
MATH_TYPE_36 = "M36"
MATH_TYPE_37 = "M37"
MATH_TYPE_38 = "M38"
MATH_TYPE_39 = "M39"
MATH_TYPE_3A = "M3A"
MATH_TYPE_3B = "M3B"
MATH_TYPE_3C = "M3C"
MATH_TYPE_3D = "M3D"
MATH_TYPE_3E = "M3E"
MATH_TYPE_3F = "M3F"
MATH_TYPE_3G = "M3G"
MATH_TYPE_3H = "M3H"

MATH_TYPE_4 = "M4"
MATH_TYPE_41 = "M41"
MATH_TYPE_42 = "M42"
MATH_TYPE_43 = "M43"
MATH_TYPE_44 = "M44"
MATH_TYPE_45 = "M45"
MATH_TYPE_46 = "M46"


MATH_TYPE_DICT = {}
MATH_TYPE_DICT[MATH_TYPE_1] = "Numbers and Operations"
MATH_TYPE_DICT[MATH_TYPE_11] = "Integers"
MATH_TYPE_DICT[MATH_TYPE_12] = "Fractions"
MATH_TYPE_DICT[MATH_TYPE_13] = "Decimals"
MATH_TYPE_DICT[MATH_TYPE_14] = "Percents"
MATH_TYPE_DICT[MATH_TYPE_15] = "Addition"
MATH_TYPE_DICT[MATH_TYPE_16] = "Multiplication"
MATH_TYPE_DICT[MATH_TYPE_17] = "Number Lines"
MATH_TYPE_DICT[MATH_TYPE_18] = "Multiples"
MATH_TYPE_DICT[MATH_TYPE_19] = "Prime Numbers"
MATH_TYPE_DICT[MATH_TYPE_1A] = "Conversions"
MATH_TYPE_DICT[MATH_TYPE_1B] = "Determining Quantities with Ratios"
MATH_TYPE_DICT[MATH_TYPE_1C] = "Sequences"
MATH_TYPE_DICT[MATH_TYPE_1D] = "Sets"
MATH_TYPE_DICT[MATH_TYPE_1E] = "Counting Problems"

MATH_TYPE_DICT[MATH_TYPE_2] = "Algebra and Functions"
MATH_TYPE_DICT[MATH_TYPE_21] = "Solving Basic Algebra Equations"
MATH_TYPE_DICT[MATH_TYPE_22] = "Distributing Terms"
MATH_TYPE_DICT[MATH_TYPE_23] = "Factoring"
MATH_TYPE_DICT[MATH_TYPE_24] = "Slope of a Line"
MATH_TYPE_DICT[MATH_TYPE_25] = "Slope Formula"
MATH_TYPE_DICT[MATH_TYPE_26] = "X and Y Intercepts"
MATH_TYPE_DICT[MATH_TYPE_27] = "Solving Quadratic Equations"
MATH_TYPE_DICT[MATH_TYPE_28] = "Solving Absolute Value Equations"
MATH_TYPE_DICT[MATH_TYPE_29] = "Solving Inequalities"
MATH_TYPE_DICT[MATH_TYPE_2A] = "Systems of Equations"
MATH_TYPE_DICT[MATH_TYPE_2B] = "Exponents"
MATH_TYPE_DICT[MATH_TYPE_2C] = "Roots"
MATH_TYPE_DICT[MATH_TYPE_2D] = "Direct/Indirect Variation"
MATH_TYPE_DICT[MATH_TYPE_2E] = "Solving Word Problems"
MATH_TYPE_DICT[MATH_TYPE_2F] = "Functions"

MATH_TYPE_DICT[MATH_TYPE_3] = "Geometry and Measurement"
MATH_TYPE_DICT[MATH_TYPE_31] = "Points on Lines"
MATH_TYPE_DICT[MATH_TYPE_32] = "Lines and Angles"
MATH_TYPE_DICT[MATH_TYPE_33] = "Angles from Parallel and Intersecting Lines"
MATH_TYPE_DICT[MATH_TYPE_34] = "Interior Angles in Triangles and Other Polygons"
MATH_TYPE_DICT[MATH_TYPE_35] = "Types of Triangles based on Angles"
MATH_TYPE_DICT[MATH_TYPE_36] = "Types of Triangles based on Sides"
MATH_TYPE_DICT[MATH_TYPE_37] = "Isosceles, Scalene, and Equilateral Triangles"
MATH_TYPE_DICT[MATH_TYPE_38] = "Congruent and Similar Triangles"
MATH_TYPE_DICT[MATH_TYPE_39] = "Special Triangle Rules"
MATH_TYPE_DICT[MATH_TYPE_3A] = "Perimeter and Area"
MATH_TYPE_DICT[MATH_TYPE_3B] = "Volume"
MATH_TYPE_DICT[MATH_TYPE_3C] = "Arc Lengths and Areas for Sectors"
MATH_TYPE_DICT[MATH_TYPE_3D] = "Coordinate Geometry"
MATH_TYPE_DICT[MATH_TYPE_3E] = "Midpoint Formula"
MATH_TYPE_DICT[MATH_TYPE_3F] = "Distance Formula"
MATH_TYPE_DICT[MATH_TYPE_3G] = "Polygon Properties"
MATH_TYPE_DICT[MATH_TYPE_3H] = "Logic"

MATH_TYPE_DICT[MATH_TYPE_4] = "Data Analysis, Statistics, and Probability"
MATH_TYPE_DICT[MATH_TYPE_41] = "Data Analysis"
MATH_TYPE_DICT[MATH_TYPE_42] = "Average"
MATH_TYPE_DICT[MATH_TYPE_43] = "Median"
MATH_TYPE_DICT[MATH_TYPE_44] = "Mode"
MATH_TYPE_DICT[MATH_TYPE_45] = "Probability"
MATH_TYPE_DICT[MATH_TYPE_46] = "Geometric Probability"



#READING
READING_TYPES = 2
READING_SUB_TYPES = 10

READING_TYPE_1 = "R1"
READING_TYPE_11 = "R11"
READING_TYPE_12 = "R12"
READING_TYPE_13 = "R13"

READING_TYPE_2 = "R2"
READING_TYPE_21 = "R21"
READING_TYPE_22 = "R22"
READING_TYPE_23 = "R23"
READING_TYPE_24 = "R24"
READING_TYPE_25 = "R25"
READING_TYPE_26 = "R26"
READING_TYPE_27 = "R27"

READING_TYPE_DICT = {}
READING_TYPE_DICT[READING_TYPE_1] = "Sentence Completion"
READING_TYPE_DICT[READING_TYPE_11] = "Context Single Word Replacement"
READING_TYPE_DICT[READING_TYPE_12] = "Synonymous Double Word Replacement"
READING_TYPE_DICT[READING_TYPE_13] = "Inference Double Word Replacement"

READING_TYPE_DICT[READING_TYPE_2] = "Reading Comprehension"
READING_TYPE_DICT[READING_TYPE_21] = "Main Idea"
READING_TYPE_DICT[READING_TYPE_22] = "Direct Comprehension"
READING_TYPE_DICT[READING_TYPE_23] = "Purpose/Rhetorical Strategy"
READING_TYPE_DICT[READING_TYPE_24] = "Inference"
READING_TYPE_DICT[READING_TYPE_25] = "Comparison"
READING_TYPE_DICT[READING_TYPE_26] = "Tone and Style"
READING_TYPE_DICT[READING_TYPE_27] = "Vocabulary in Context"

#Main Type Lists
MAIN_TYPE_SIZE_ARRAY = {}
MAIN_TYPE_SIZE_ARRAY[WRITING_TYPE] = WRITING_TYPES
MAIN_TYPE_SIZE_ARRAY[READING_TYPE] = READING_TYPES
MAIN_TYPE_SIZE_ARRAY[MATH_TYPE] = MATH_TYPES


#Sub Type Lists
SUB_TYPE_LIST = {}

SUB_TYPE_LIST[WRITING_TYPE_1] = [WRITING_TYPE_11, WRITING_TYPE_12, WRITING_TYPE_13, WRITING_TYPE_14, WRITING_TYPE_15, WRITING_TYPE_16, WRITING_TYPE_17, WRITING_TYPE_18, WRITING_TYPE_19]
SUB_TYPE_LIST[WRITING_TYPE_2] = [WRITING_TYPE_21, WRITING_TYPE_22, WRITING_TYPE_23, WRITING_TYPE_24, WRITING_TYPE_25, WRITING_TYPE_26, WRITING_TYPE_27, WRITING_TYPE_28, WRITING_TYPE_29]
SUB_TYPE_LIST[WRITING_TYPE_3] = [WRITING_TYPE_31, WRITING_TYPE_32, WRITING_TYPE_33, WRITING_TYPE_34]

SUB_TYPE_LIST[MATH_TYPE_1] = [MATH_TYPE_11, MATH_TYPE_12, MATH_TYPE_13, MATH_TYPE_14, MATH_TYPE_15, MATH_TYPE_16, MATH_TYPE_17, MATH_TYPE_18, MATH_TYPE_19, MATH_TYPE_1A, MATH_TYPE_1B, MATH_TYPE_1C, MATH_TYPE_1D, MATH_TYPE_1E]
SUB_TYPE_LIST[MATH_TYPE_2] = [MATH_TYPE_21, MATH_TYPE_22, MATH_TYPE_23, MATH_TYPE_24, MATH_TYPE_25, MATH_TYPE_26, MATH_TYPE_27, MATH_TYPE_28, MATH_TYPE_29, MATH_TYPE_2A, MATH_TYPE_2B, MATH_TYPE_2C, MATH_TYPE_2D, MATH_TYPE_2E, MATH_TYPE_2F]
SUB_TYPE_LIST[MATH_TYPE_3] = [MATH_TYPE_31, MATH_TYPE_32, MATH_TYPE_33, MATH_TYPE_34, MATH_TYPE_35, MATH_TYPE_36, MATH_TYPE_37, MATH_TYPE_38, MATH_TYPE_39, MATH_TYPE_3A, MATH_TYPE_3B, MATH_TYPE_3C, MATH_TYPE_3D, MATH_TYPE_3E, MATH_TYPE_3F, MATH_TYPE_3G, MATH_TYPE_3H]
SUB_TYPE_LIST[MATH_TYPE_4] = [MATH_TYPE_41, MATH_TYPE_42, MATH_TYPE_43, MATH_TYPE_44, MATH_TYPE_45, MATH_TYPE_46]

SUB_TYPE_LIST[READING_TYPE_1] = [READING_TYPE_11, READING_TYPE_12, READING_TYPE_13]
SUB_TYPE_LIST[READING_TYPE_2] = [READING_TYPE_21, READING_TYPE_22, READING_TYPE_23, READING_TYPE_24, READING_TYPE_25, READING_TYPE_26, READING_TYPE_27]



def return_main_type(subtype):
  return subtype[:-1]

#Take ['M12','M34'] and return ['M1','M3']
def return_main_types(subtype_list):
  array = []
  for element in subtype_list:
    main_type = return_main_type(element)
    if main_type not in array:
      array.append(main_type)
  return array

assert( return_main_types(['M12','M34','M31']) == ['M1','M3'] )




#CLASS ANALYTICS  

CLASS_MISSED_WRITING =[]
CLASS_MISSED_READING =[]
CLASS_MISSED_MATH =[]

QUESTION_TYPE = []

def section_type_dict(section_type):
  if section_type == WRITING_TYPE:
    return WRITING_TYPE_DICT
  elif section_type == READING_TYPE:
    return READING_TYPE_DICT
  elif section_type == MATH_TYPE:
    return MATH_TYPE_DICT
  else:
    return {}

#HTML
paropen = '<p>'
parclose = '</p>'


#Advice

#Colors
RED = "red"
YELLOW = "blue"
GREEN = "00CC00"
#RED = "purple"
#YELLOW = "blue"
#GREEN = "pink"

#positive
pa1 = "Good Job!"
pa2 = "Fantastic! Well done."
pa3 = "You are performing well."
pa4 = "Great work."
pa5 = "Great progress."
positive = [pa1, pa2, pa3, pa4, pa5]
p_thresh = 0.8

#average
aa1 = "Your performance here is okay. Focus on other weaker areas first."
aa2 = "Your scores in this category are average."
aa3 = "Improve in these areas once you have finished working on your more poor areas."
average = [aa1, aa2, aa3]
a_thresh = 0.30

#negative
na1 = "Uh oh, you need some work in this category."
na2 = "Unfortunately, you are not as strong in this area."
na3 = "You need some improvement here."
na4 = "Here is a great place to improve and score higher."
na5 = "Try focussing more in this area to increase your score."
negative = [na1, na2, na3, na4, na5]

#guessing
ga1 = "Your guesses in this category are often wrong. Consider leaving them blank."
ga2 = "Leave more questions in these catgories blank. You are losing 1/4th a point for each one you miss."
ga3 = "Instead of guessing, leave these questions blank."
ga4 = "Guessing in this category is a much better option and will improve your score."
guess_remove = ""
guess = [guess_remove, guess_remove, guess_remove, guess_remove]
def div(x, y):
  if y == 0:
    return 0
  return float(x) / float(y)

def random_choice(array):
  return array[(int(random.random() * 100) % len(array))]

def get_section_type_size(section_type):
  if section_type == WRITING_TYPE:
    return ("W", WRITING_TYPES)
  elif section_type == MATH_TYPE:
    return ("M", MATH_TYPES)
  elif section_type == READING_TYPE:
    return ("R", READING_TYPES)
  else:
    print ("Error: You are looking for data to an invalid section.")
    return None

#LEVEL TYPES
LEVEL_1 = "L1"
LEVEL_2 = "L2"
LEVEL_3 = "L3"
LEVEL_4 = "L4"
LEVEL_5 = "L5"

"""def round_dec(f, n):
  if isinstance(f, int):
    return f
  f = f * pow(10,n)
  f = f - f%1
  f = f / pow(10,n)
  return f"""

def percentage(decimal):
  decimal *= 100
  output = str(int(decimal)) + "%"
  return output

average_bound1 = 550
average_bound2 = 670

def qualitative_color(score):
  if score < average_bound1:
    return RED
  elif score > average_bound2:
    return GREEN
  else:
    return YELLOW

def qualitative(score):
  if score < average_bound1:
    return "Poor"
  elif score > average_bound2:
    return "Proficient"
  else:
    return "Average"

def overall_qualitative_color(score):
  return qualitative_color(score / 3)

def overall_qualitative(score):
  return qualitative(score / 3)


#round the questions missed deduction down
def round_rem(dec):
  if dec % 1 > 0.5:
    return 1
  return 0

def random_number(n):
  return int(random.random() * 100) % n

def string_to_array(data):
  data = data[1:-1]
  array = []
  data = data.replace(' ', "")
  data = data.replace('(', "")
  data = data.replace(')', "")
  data = data.replace("'", "")
  data = data.split(',')
  i = 0
  for entry in data:
    if i % 2 == 0:
      q_id = entry
    if i % 2 == 1:
      array.append((q_id, entry))
    i+=1
  return array

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def empty(s):
  if isinstance(s, list):
    return s == []
  if isinstance(s, str):
    return s == ""

def file_exists(filename):
  return os.path.exists(filename)

def user_directory(name, c):
  return "Users" + DIR_SEP + c + DIR_SEP + name 

def class_directory(c):
  return "Users" + DIR_SEP + c

def test_directory(test_id):
  return "Tests" + DIR_SEP + test_id

def user_filename(name, c):
  return "Users" + DIR_SEP + c + DIR_SEP + name + DIR_SEP + name + TXT

def valid_test_id(test_id):
  if test_id[0] == '.':
    return False
  if file_exists(test_directory(test_id)):
    array = test_id.split()
    if SPACE not in array:
      return True
  return False

def fuse_id_array(array):
  output = ""
  end = array.pop()
  for element in array:
    output += (element + '_')
  output += end
  return output

def mkdir(dir_name):
  os.mkdir(dir_name)

def rmdir(dir_name):
  shutil.rmtree(dir_name)

def parse_missed(array):
  blank = 0
  incorrect = 0
  for question in array:
    if question[1] == '?':
      blank += 1
    else:
      incorrect+=1
  return (blank, incorrect)

def is_null(n):
  return n == None

def section_size(section_type):
  if section_type == MATH_TYPE:
    return MATH_SIZE
  elif section_type == WRITING_TYPE:
    return WRITING_SIZE
  elif section_type == READING_TYPE:
    return READING_SIZE
  else:
    print ("Error invalid section type.")
    return 0

def section_name(section_type):
  if section_type == MATH_TYPE:
    return "Math"
  elif section_type == WRITING_TYPE:
    return "Writing"
  elif section_type == READING_TYPE:
    return "Reading"
  else:
    print ("Error invalid section type.")
    return 0

def average_array(array):
  average = 0
  for element in array:
    average+=element
  return average // len(array)


def index_exists(dictionary, key):
  return key in dictionary.keys()

def date_after(date1, date2):
  date1 = date1.split('/')
  date2 = date2.split('/')
  if int(date2[2]) > int(date1[2]):
    return True
  if int(date2[0]) > int(date1[0]):
    return True
  if int(date2[1]) > int(date1[1]):
    return True
  return False

assert (date_after('06/25/2014','05/24/2015'))
assert (not date_after('06/25/2016','05/24/2015'))

assert (date_after('05/25/2015','07/23/2015'))
assert (not date_after('08/25/2015','07/23/2015'))

assert (date_after('08/10/2015','08/23/2015'))
assert (not date_after('04/25/2015','04/21/2015'))

#Vars to hold a colleges Overall, Math, Reading, Writing, and Name - passed to graph obj in user.py as args
dict_bgcolor = {'Harvard': 'rgb(255,255,255)', 'UC Berkeley':'rgb(253, 181, 21)', 'MIT':'rgb(138, 139, 140)', 'Stanford':'rgb(140,21,21)', 'UCLA':'rgb(83, 104, 149)', 'Princeton':'rgb(216,100,44)', 'Yale':'rgb(15, 77,146)', 'Caltech':'rgb(255,255,255)', 'Johns Hopkins': 'rgb(28,72,130)', 'USC':'rgb(153,0,0)', 'Carnegie Mellon':'rgb(153,0,0)' }
dict_colors ={'Harvard': 'rgb(165,28,48)', 'UC Berkeley':'rgb(0,50,98)', 'MIT':'rgb(161, 31, 52)', 'Stanford':'rgb(243,239,215)', 'UCLA':'rgb(255, 215, 0)', 'Princeton':'rgb(46,42,43)', 'Yale':'rgb(255, 255, 255)', 'Caltech':'rgb(255,102,0)', 'Johns Hopkins': 'rgb(207,181,59)', 'USC':'rgb(255,204,0)', 'Carnegie Mellon':'rgb(212,212,212)' }
#Dictionary for 50th percentile Math
dict_math = {'Harvard': 750, 'UC Berkeley': 720, 'MIT': 780, 'Stanford': 750, 'UCLA': 700, 'Princeton': 760, 'Yale': 750, 'Caltech': 780, 'Johns Hopkins': 720, 'USC': 710, 'Carnegie Mellon': 740}


#Dictionary for 50th percentile Reading
dict_read = {'Harvard': 750, 'UC Berkeley': 690, 'MIT': 740, 'Stanford': 730, 'UCLA': 680, 'Princeton': 760, 'Yale': 760, 'Caltech': 740, 'Johns Hopkins': 690, 'USC': 670, 'Carnegie Mellon': 680}

#Dictionary for 50th percentile Writing
dict_write = {'Harvard': 750, 'UC Berkeley': 700, 'MIT': 750, 'Stanford': 740, 'UCLA': 700, 'Princeton': 760, 'Yale': 760, 'Caltech': 740, 'Johns Hopkins': 700, 'USC': 690, 'Carnegie Mellon': 700}

#Dictionary for 50th percentile Overall
dict_overall = {'Harvard': 2250, 'UC Berkeley': 2110, 'MIT': 2270, 'Stanford':2220, 'UCLA': 2080, 'Princeton': 2280, 'Yale': 2270, 'Caltech' : 2260, 'Johns Hopkins': 2110, 'USC': 2070, 'Carnegie Mellon': 2120}


