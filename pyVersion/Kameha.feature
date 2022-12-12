Feature: Saiyan Attaque 
En tant que Saiyan
Je veux pouvoir attaquer un autre Saiyan
Afin qu'il perde de la Health

#Scenario: Kamehameha de Goku
#Given Un saiyan Goku
#When j'utilise kamehameha
#Then elle perd de la vie 

Scenario Outline: Kamehameha de Saiyan
Given Un saiyan <saiyan> de <ki1> ki et <health1> vie
and Un saiyan <saiyan2> de <ki2> ki et <health2> vie
When j'utilise kamehameha
Then elle perd <quantite> de vie 
| saiyan | quantite |
| Goku   | 70 |

