Feature: Simply Google search

   Make a simply Google search

   Scenario Outline: Make a search
        Given Iam on Google search page
        When I put <text> on the search input
        And I press enter to search
        Then I see if results contains <txtResult>
        Examples:
        | text | txtResult |
        | Nasa | https://www.nasa.gov |
        | ubuntu | Ubuntu: The leading operating system for PCs |