import pytest
import math
import Saiyan
import Potara
		
class Test:
	def __init__(self):
		self.Goku = Saiyan()
		self.Vegeta = Saiyan()
		self.potara = Potara(self.Vegeta)
	
	def kamehamehaTest(self):
		gokuKi = self.Goku.getKi()
		vegetaHealth = self.Vegeta.getHealth()
		assert self.Goku.getKi() == gokuKi - self.Goku.KAMEHAMEHA_ATTACK
		
	def saiyanPotaraTest(self):
		vegetaKi = self.Vegeta.getKi()
		gokuHealth = self.Goku.getHealth()
        self.potara.improveKamehameha(self.Goku)
        assert self.Vegeta.getKi() == math.floor((vegetaKi*1.1) - Goku.KAMEHAMEHA_ATTACK)
        assert self.Goku.getHealth() == gokuHealth- Vegeta.KAMEHAMEHA_ATTACK
