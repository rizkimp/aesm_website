Feature: contact us
    Scenario: contact us
        Given visit aesmwebsite
        Then click button contact us
        And enter first name
        And enter last name
        And enter email
        And enter company name
        And enter job title
        And enter country
        And enter enquiry
        And enter message
        And select checkbox
        When click button submit 
        Then success contact us
