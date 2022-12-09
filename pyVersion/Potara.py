import Saiyan

class Potara:
	def __init__(self, saiyan = None):
		self.__s = saiyan
	
	def improveKamehameha(self,s2):
		self.__s.setKi(self.__s.getKi()*1.1);
		self.__s.kamehameha(s2)
