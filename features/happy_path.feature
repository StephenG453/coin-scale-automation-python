Feature: locating a fake weight inside the React App

    Scenario: test functionality of locating a fake weight inside the React App
      Given React Application is loaded and home page is visible
      When user adds coin 0 into cell 0 in the left grid
      And user adds coin 1 into cell 1 in the left grid
      * user adds coin 2 into cell 2 in the left grid
      * user adds coin 3 into cell 0 in the right grid
      * user adds coin 4 into cell 1 in the right grid
      * user adds coin 5 into cell 2 in the right grid
      * user presses weigh button
      * user checks latest weight result
      * user clears right grid
      * user adds coin 6 into cell 0 in the right grid
      * user adds coin 7 into cell 1 in the right grid
      * user adds coin 8 into cell 2 in the right grid
      * user presses weigh button
      * user checks latest weight result
      * user determines group with fake weight
      Then user finds fake weight