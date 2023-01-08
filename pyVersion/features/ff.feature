Feature: La FFF veut faire un recensement et connaître le nom de tous les coach en Ligue1

  Scenario Outline: Trouver le nom du coach d'une équipe
    Given Le nom d'une équipe <equipe> et d'un coach <coach>
    When je lui demande le nom de son entraîneur
    Then elle me répond par le nom de son coach <coach>
    Examples:
      | equipe  | coach     |
      | PSG     | Galtier   |
      | Barca   | Xavi      |
      | Maroc   | Walid     |
      | Algerie | Djamel    |