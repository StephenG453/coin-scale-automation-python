Feature: locating a fake weight inside the React App

    Scenario: test functionality of locating a fake weight inside the React App
      Given React Application is loaded and home page is visible
      When user adds coin 0 to first cell in the left grid
      When user adds coin 1 to second cell in the left grid
      When user adds coin 2 to third cell in the left grid
      When user adds coin 3 to first cell in the right grid
      When user adds coin 4 to second cell in the right grid
      When user adds coin 5 to third cell in the right grid
      When user presses weigh button
      When user checks latest weight result
      When user clears right grid
      When user adds coin 6 to first cell in the right grid
      When user adds coin 7 to second cell in the right grid
      When user adds coin 8 to third cell in the right grid
      When user presses weigh button
      When user checks latest weight result
      When user determines group with fake weight
      Then user finds fake weight