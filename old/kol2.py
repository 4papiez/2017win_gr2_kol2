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

from student import Student
from classs import Class


textoption = '''What would you like to do?
1) add student
2) print students
3) get student's scores
4) get student's average
5) get class average'''


if __name__ == "__main__":

	name = raw_input("Class name?")

	c = Class(1,name)


	while True:
		option = raw_input(textoption)
		if option == 1:
			sname = raw_input("Name:")
			ssurname = raw_input("surName:")
			s = Student(1, "Ja","Ja")
			c.addStudent(s)
	
	print s
