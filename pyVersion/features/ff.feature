Feature: La FFF veut faire un recensement et connaître le nom de tous les coach en Ligue1

  Scenario Outline: Trouver le nom du coach d'une équipe
    Given Le nom d'une <equipe> et d'un <coach>
    When je lui demande le nom de son entraîneur
    Then elle me répond par le nom de son <coach>
    Examples:
      | equipe  | coach     |
      | PSG     | Galtier   |
      | Barca   | Xavi      |
      | Maroc   | Walid     |
      | Algerie | Djamel    |