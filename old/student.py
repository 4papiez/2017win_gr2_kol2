
class Student:
	nr = 0
	name = ''
	surname = ''
	scores = []
	def __init__(self,nr, name, surname):
		self.nr = nr
		self.name = name
		self.surname = surname
		
	def addScore(mark):
		self.scores.append(mark)
	def __str__(self):
		return "Nr: " + str(self.nr)+ "\nName: "+self.name+"\nSurname: "+self.surname

	def getScores():
		return scores
	def getAverage():
		result =  0.0
		for i in scores:
			result = result+i
		result = result/scores.count()
		return result
