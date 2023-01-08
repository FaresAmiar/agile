Feature: Saiyan Attaque 
En tant que Saiyan
Je veux pouvoir attaquer un autre Saiyan
Afin qu'il perde de la Health

#Scenario: Kamehameha de Goku
#Given Un saiyan Goku
#When j'utilise kamehameha
#Then elle perd de la vie

Scenario Outline: Kamehameha de Saiyan
Given Un saiyan de <ki1> ki et <health1> vie et Un saiyan de <ki2> ki et <health2> vie
When j'utilise kamehameha
Then elle perd <quantite> de vie 

Examples: Saiyans
|   health2 |   ki1     |   ki2   |   health1 |   quantite    |
|   100     |   100     |   100   |    100    |     70        |

