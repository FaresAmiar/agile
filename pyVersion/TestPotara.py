#import pytest
import math
import Saiyan
import Potara
		
class Test:
	def __init__(self):
		self.Goku = Saiyan.Saiyan()
		self.Vegeta = Saiyan.Saiyan()
		self.potara = Potara.Potara(self.Vegeta)
	
	def kamehamehaTest(self):
		gokuKi = self.Goku.getKi()
		vegetaHealth = self.Vegeta.getHealth()
		self.Goku.kamehameha(self.Vegeta)
		assert (self.Goku.getKi() == (gokuKi - self.Goku.KAMEHAMEHA_ATTACK ))

	def saiyanPotaraTest(self):
		vegetaKi = self.Vegeta.getKi()
		gokuHealth = self.Goku.getHealth()
		self.potara.improveKamehameha(self.Goku)
		assert self.Vegeta.getKi() - math.floor((vegetaKi*1.1) - self.Goku.KAMEHAMEHA_ATTACK) < 0.01
		assert self.Goku.getHealth() == gokuHealth - self.Vegeta.KAMEHAMEHA_ATTACK

def main():
	Test().kamehamehaTest()
	Test().saiyanPotaraTest()

if __name__ == '__main__':
	main()
