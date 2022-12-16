
Feature: Saiyan Attaque
En tant que Saiyan
Je veux pouvoir attaquer un autre Saiyan
Afin qu'il perde de la Health

Scenario: Kamehameha de Goku
Given Un saiyan de 100 ki et 100 vie et Un saiyan de 100 ki et 100 vie
When Goku utilise kamehameha
Then il reste 70 de vie

Scenario Outline: Kamehameha de Saiyan
Given Un saiyan de <ki1> ki et <health1> vie et Un saiyan  de <ki2> ki et <health2> vie
When j'utilise kamehameha
Then il reste <quantite> de vie
  Examples:
| ki1 | health1 | ki2 | health2 | quantite |
| 100 | 130 | 100  | 80 | 50 |
| 100 | 100 | 130  | 130 | 100 |

Scenario: Attaquer un mort
Given Un saiyan de 100 ki et 100 vie et Un saiyan de 10 ki et -5 vie
When Goku utilise kamehameha sur le mort
Then le ki de Goku n'a pas changé



