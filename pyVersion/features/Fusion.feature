Feature: Fusion
En tant que Fusion
Je veux pouvoir fusionner avec un Saiyan qui n'a plus de vie
Afin que je reste en vie

Scenario: Fusion avec un mort
Given Un saiyan de 100 ki et 100 vie, Un saiyan de 100 ki et 100 vie et un autre Saiyan de 0 ki et 0 vie
When ils fusionnent
Then la fusion est encore en vie