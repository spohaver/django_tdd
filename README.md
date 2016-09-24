## Notes/Rules Learned through the Python Test Driven Development Book

1. (Chapter 1): Obey the Testing Goat!
  * In TDD, the Testing Goat always bleats "Test first, test first!"
2. (Chapter 2): Use a functional Test to Scope Out a Minimum Viable App
  * Tracks a User Story, also known as an Acceptance Test or End-to-End test
  * Apply a human-readable story that describes the point of the view of the user
    * Use comments first to capture key points in the User Story
  * self.fail('finish the test') is used as an end point as you are going through your TDD User Story
3. (Chapter 3): Unit Tests
  * Unit tests are used to define how we want the code to behave
    * _Each line of production code written should be tested by (at least) one of the unit tests_
    * Once that unit test fails, write the smallest amount of application code to get the test to pass
  * Then run functional test(s) to make sure they pass too
4. (Chapter 4): Dont Test Constants
  * Unit tests are to test the logic, flow control, and configuration in the code
    * _Implement templates_
