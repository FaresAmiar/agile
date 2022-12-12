import math
import Saiyan
import Potara
import Fusion
		
class Test:
	def __init__(self):
		self.Goku = Saiyan.Saiyan(10,10)
		self.Vegeta = Saiyan.Saiyan(10,10)
		self.Saiyans = [self.Vegeta,self.Goku]
		self.fusion = Fusion.Fusion(self.Saiyans)
	def fusionTest(self):
		assert (self.fusion.getSaiyan().getKi() == (100 ))
def main():
	Test().fusionTest()

if __name__ == '__main__':
	main()
    