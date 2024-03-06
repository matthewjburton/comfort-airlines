# Test Plan

**Team Name:** Cloud Nine  
**Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher

Before merging any branches into the main branch of the project, new code must be sufficiently tested to prevent the introduction of bugs into the main codebase. Cloud Nine's test plan includes three parts: unit tests, module tests, and system tests.

## Unit Tests

Unit tests are isolated checks where new code is tested independently, ignoring its interaction with other modules. These tests will be **conducted by members of the team that did not contribute to the code** be evaluated. Test data will be created in the _/documents/tests_ directory.

- A _new directory_ will be created for each new unit test
- In each unit test directory, there will be two sub folders:
  - The first sub directory will be named _/inputs_ and it contains a list of input files, each containing only one set of data
    - The list of inputs will cover all of the equivalence cases relavent to the unit
    - Additional tests will be included around the boundaries of each equivalence case
    - Finally a test will be included with an input of the incorrect data type.  
  - The second sub-directory will be named _/outputs_ and it contains a list of output files with known, expected results.
    - This list corresponds to the list of inputs.

- Code authors have two responnsiblities:
  - Authors must generate the list of inputs and outputs
  - Additionally, authors must write a script to execute the code with each input from the _/inputs_ directory
    - The results of this script will be output into a _results.txt_ file in the unit test directory
      - Each test must be listed with its input, expected output, PASS/FAIL and in the event of a failed test the actual output generated
      - Sort this list with failed tests at the top of the file

- Testers have two resposibilities:
  - Add additional test cases to the _/inputs_ and _/outputs_ directories if necessary
  - Conduct one of the following testing strategies. Coordinate with other testers to ensure each strategy has been exercised:
    - Black box testing - executing the tests and reviewing the  results without viewing the code  
    - Glass box testing - executing the tests and reviewing the results in addition to reviewing the code  
    - Executionless testing - scan the code for errors without executing any tests

## Module Tests

Perform the same testing steps as stated above for unit tests, but now connect the independent unit to its other connected units to test the module.

## System Tests

Test the overall project against the requirements document. If the project still performs as intended, the unit is ready to be merged into the main branch.
