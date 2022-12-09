class Potara:
	def __init__(self,Saiyan s = None):
		self.__s = s
	
	def improveKamehameha(self,Saiyan s2):
		self.__s.setKi(self.__s.getKi()*1.1);
		self.__s.kamehameha(s2)
