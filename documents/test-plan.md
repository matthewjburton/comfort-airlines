# Test Plan

**Team Name:** Cloud Nine  
**Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher

Before merging any changes into the main branch, new code must be tested to prevent the introduction of bugs. Cloud Nine's test plan includes three parts:

1. Unit testing
2. Module testing
3. Integration testing

## Who Conducts Tests?

As the author, it is expected that you have tested your code with at a basic level before passing it to the formal testers. Formal tests must be **conducted by members of the team that did not author the code**.

## Where are Tests Stored?

### /documents/tests

Test data is stored in the _/documents/tests_ directory. Each module will have its own sub-directory within the _/tests_ directory.

#### documents/tests/module

Testers must create a new directory **named after the module** to store all of the test data
  
##### documents/tests/module/inputs

A sub directory named _/inputs_ can be used to contain a set of input files, each file containing one test.

Test sets should include all of the following:

  1. An example from each equivalence case
  2. Additional tests around the boundaries of each equivalence case range
  3. An input of an incorrect data type

##### documents/tests/module/outputs

If testing requires an input set, a sub-directory named _/outputs_ must contain the set of expected values from each input test.

#### Scripts

If a test requires a script, the script should also be stored in the _/documents/tests/module_ directory.

The results from each test should be listed in a results.txt files stored in the _documents/tests/module_ directory.

Each test must be listed including its input, expected output, PASS/FAIL and in the event of a failed test the actual output generated.

## Unit Tests

Unit tests ensure that each individual method within a module works as expected.

Develop tests that exercise each module and ensure the methods behave as defined in the functional specification document.

If each method works as intended, continue on to module testing. If there is an issue with one or more methods, report the issue(s) to the author and track the issue(s) in the defect log.

## Module Tests

Module tests are isolated tests where new code is tested independent of its connections to other classes/modules.

Now exercise the entire module, not just individual methods.

If the entire module behaves as described by the functional specification document, move on to integration testing. If there is an issue with the module as a whole, notify the author and track the issue in the defect log.

## Integration Tests

Finally, test the entire project and esnure that it behaves in the manner outlined by the requirements document. If the project still performs as intended, the module is ready to be merged into the main branch. If an issue is found upon integrating the module into the project, report the issue to the author and track the bug in the defect log.

## Finding a Balance

Cloud Nine's test plan is designed to reduce the overall number of bugs entered into our main codebase while maximizing the amount of time we have to develop new features. We recognize the benefit of having more team members test each module, but we also acknowledge our limited development time and as such have decided to keep the number of testers to a minimum. Generally, we can expect that all code that is ready to be tested will undergo inspection through GitHub's pull request system, and ideally they will go through the testing listed above. This level of testing is not necessarily cost effective for simple modules, however we will make sure to exercise this plan for more complicated and frequently used systems as they are developed.

With more time, or for a more performance critical project we would be sure to exercise black box testing, glass box testing, and inspections by a multitude of team members as we recognize the value those strategies provide when tryinng to reduce bugs. However, with time as another pressing factor our testing may be less robust than that of a larger software company.
