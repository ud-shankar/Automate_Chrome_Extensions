Feature: SDET assignment - Search and switch between tabs using chrome extension (Saka)

    Scenario: Test one of the feature of the extension - Saka
        Given User adds the extension and opens the browser
        When User opens and navigates to multiple pages in multiple tabs
        And User navigates to the popup frame of the extension
        And User enter word and search for the tab opened
        Then User verify the tab has been switched successfully