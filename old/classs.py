
class Class:
	nr = 0
	name = ''
	students =[]
	def __init__(self,nr, name):
		self.nr = nr
		self.name = name

	def __str__(self):
		return "Class:  "+self.name

	def addStudent(student):
		students.append(student)
	def getClassAverage():
		result = 0.0
		for i in students:
			result = result + i.getAverage()

		return result/students.count()
