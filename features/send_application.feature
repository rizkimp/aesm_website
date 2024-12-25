Feature: send appication
    Scenario: send appication
        Given visit aesmwebsite
        Then click button careers
        And enter first name cv
        And enter last name cv
        And enter email cv
        And upload cv
        And select job type
        And enter job position
        And enter remarks
        When click button send application
        Then success send appication
