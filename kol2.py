# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

from functools import reduce
from optparse import OptionParser
import json

option_help = '''choose OPTION: 
			create_course (required course_name)/
			create_student (required coursename fname, lname)/
			add_grade (required course_name , fname, lname, grade)/
			add_presence (required course_name , fname, lname, presence (T/F))/
			get_average (required course_name, optional fname, lname)/
			get_presence (required course_name, fname, lname)'''

def create_course(course_list, course_name):
	course_list[course_name] = {}

def create_student(course_list, course, first_name, last_name):
	course_list[course][first_name+' '+last_name] = {'Grades' : [], 'Presence' : []}
	
def add_grade(course_list, course, student, grade):
	course_list[course][student]['Grades'].append(grade)

def add_presence(course_list, course, student, is_present):
	course_list[course][student]['Presence'].append(is_present)
	
def get_average(course_list, course, student = None):
	result = 0.0
	if student is None:	
		for s in course_list[course].items():
			result += reduce(lambda x, y: x + y, s[1]['Grades']) / len(s[1]['Grades'])
		result /= len(course_list[course])
	else:
		result = reduce(
			lambda x, y: x + y, course_list[course][student]['Grades']
			) / len(course_list[course][student]['Grades']
		)
	return result
	
def get_presence(course_list, course, student):
	return '{:0.0f}%'.format(
		100 * len([x for x in course_list[course][student]['Presence'] if x]) 
		/ len(course_list[course][student]['Presence'])
	)
	
def save(course_list):
	with open('data.json', 'w') as outfile:
		json.dump(course_list, outfile)
		
def load():
	with open('data.json') as data_file:
		course_list = json.load(data_file)
	return course_list
	
def make_parser():
	parser = OptionParser("usage: %prog [options] arg")
	parser.add_option('-c', '--course',dest = 'coursename',help="course COURSENAME")
	parser.add_option('-f', '--firstname',dest = 'firstname',help="student's FIRSTNAME")
	parser.add_option('-l', '--lastname',dest = 'lastname',help="student's LASTNAME")
	parser.add_option('-p', '--presence',dest = 'presence',help="student's PRESENCE (True/False)")
	parser.add_option('-g', '--grade',dest = 'grade',help="student's GRADE")
	parser.add_option('-o', '--option',dest = 'option',help=option_help)			 
	return parser
	
if __name__ == "__main__":
	course_list = load()
	parser = make_parser()
	(options, args) = parser.parse_args()
	if options.option=='create_course':
		create_course(course_list, options.coursename)
	elif options.option=='create_student':
		create_student(
			course_list, options.coursename, 
			options.firstname, options.lastname
		)
	elif options.option=='add_grade':
		add_grade(
			course_list, options.coursename, 
			options.firstname+' '+options.lastname,
			float(options.grade)
		)
	elif options.option=='add_presence':
		add_presence(
			course_list, options.coursename,
			options.firstname+' '+options.lastname, 
			True if options.presence=='T' else False
		)
	elif options.option=='get_presence':
		print get_presence(
			course_list, options.coursename, 
			options.firstname+' '+options.lastname
		) 
	elif options.option=='get_average':
		print get_average(
			course_list, options.coursename, 
			options.firstname+' '+options.lastname if options.firstname is not None else None
		)
	else: 
		parser.error("incorrect number or type of arguments")
		
	save(course_list)
