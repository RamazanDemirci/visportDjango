Feature: Leagues
    
    Scenario: Add Legue record
        Given I set POST league service api endpoint
        And I set the following league Item to request HEADER:
            | name          | alias             | country   | country_code  |
            | seriea        | Seria             | Italy     | IT            |
        When Send a POST HTTP request
        # There are at least one record at the table
        Then I receive valid response
        
    Scenario: Update Legue record
        Given I set the following PUT league service api endpoint
        And I set the following league Item to request HEADER:
            | name          | country   | country_code  |
            | seriea        | Italia     | ITL            |
        When Send a PUT HTTP request
        # There are at least one record at the table
        Then I receive valid response


    todo: tables not ready for bdd relation and scenario. i postponed bdd. 