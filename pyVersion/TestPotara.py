import pytest
import math
		
class Test:
	def __init__(self):
		self.Goku = Saiyan()
		self.Vegeta = Saiyan()
		self.potara = Potara(Vegeta)
	
	def kamehamehaTest(self):
		gokuKi = Goku.getKi()
		vegetaHealth = Vegeta.getHealth()
		assert self.Goku.getKi() == gokuKi - self.Goku.KAMEHAMEHA_ATTACK
	def saiyanPotaraTest(self):
		vegetaKi = Vegeta.getKi()
		gokuHealth = Goku.getHealth()
        self.potara.improveKamehameha(Goku)
        assert Vegeta.getKi() == math.floor((vegetaKi*1.1) - Goku.KAMEHAMEHA_ATTACK)
        assert Goku.getHealth() == gokuHealth- Vegeta.KAMEHAMEHA_ATTACK
