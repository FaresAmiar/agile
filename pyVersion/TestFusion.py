import math
import Saiyan
import Potara
import Fusion
		
class Test:
	def __init__(self):
		self.Goku = Saiyan.Saiyan(10,10)
		self.Vegeta = Saiyan.Saiyan(10,10)
		self.Trunks = Saiyan.Saiyan(100,100)
		self.Saiyans = [self.Vegeta,self.Goku,self.Trunks]
		self.fusion = Fusion.Fusion(self.Saiyans)
#Test si la classe test crée bien un saiyan avec les valeurs de Ki et de Health souhaité
	def fusionTest(self):
		assert (self.fusion.getSaiyan().getKi() == (10000))
		assert (self.fusion.getSaiyan().getHealth() == (10000))
def main():
	Test().fusionTest()

if __name__ == '__main__':
	main()
    