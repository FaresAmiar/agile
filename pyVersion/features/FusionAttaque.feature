Feature: Fusion Attaque
En tant que Fusion
Je veux pouvoir attaquer un autre Saiyan
Afin qu'il perde de la Health

Scenario: Kamehameha de Vegeto
Given Un saiyan de 100 ki et 100 vie et Un saiyan de 100 ki et 100 vie fusionne et un autre Saiyan de 100 ki et 100 vie
When La fusion utilise kamehameha
Then il reste au saiyan 70 de vie

Scenario Outline: Kamehameha de Fusion
  Given Un saiyan de <ki1> ki et <health1> vie et Un saiyan  de <ki2> ki et <health2> vie fusionne et un autre Saiyan de <ki3> ki et <health3> vie
  When La fusion utilise kamehameha
  Then il reste au saiyan <quantite> de vie
  Examples:
| ki1 | health1 | ki2 | health2 | ki3 | health3 | quantite |
| 100 | 100 | 100  | 100 | 100  | 40 | 10 |
| 100 | 100 | 100  | 100 | 100  | 130 | 100 |
