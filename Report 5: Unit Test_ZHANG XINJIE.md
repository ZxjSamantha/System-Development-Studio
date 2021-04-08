# Report 5: Unit Test

## Name: ZHANG XINJIE Student ID Number: 20M14457

---

Exercise 1: Add one unit test to the OSS project. 

Test Case: Test case is the combination of the input and the output, depending on the test objects. For example, the test of a command should include parameters of command line and environment variables. The test of a function should include parameters of function and global variables. 

The output of the test of commands should be exit code, and the output of test of a function can be the return value of the function and global variables. 

The entire test of an OSS project include test for UI (E2E test), service (service and API) and unit (function and class). 

**unittest** is the built-in framewrok for unit test in Python. Here is a simple example for showing the flow of unit test with unittest.

First define a bunch of simple arithmetic functions and name it as `mathfunc.py`:

```
def add(a, b):
    return a+b

def minus(a, b):
    return a-b

def multi(a, b):
    return a*b

def divide(a, b):
    return a/b
```

The unit test can be done in the following flow:

```
import unittest
from mathfunc import *

class TestMathFunc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(1, 2))
    
    def test_minus(self):
        self.assertEqual(1, minus(3, 2))
    
    def test_multi(self):
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))

if __name__ =='__main__':
    unittest.main()
```

The output is as the following:

```
FF..
======================================================================
FAIL: test_add (__main__.TestMathFunc)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/test_mathfunc.py", line 8, in test_add
    self.assertNotEqual(3, add(1, 2))
AssertionError: 3 == 3
======================================================================
FAIL: test_divide (__main__.TestMathFunc)
----------------------------------------------------------------------
Traceback (most recent call last):
File "test_mathfunc.py", line 18, in test_divide
    self.assertEqual(2.5, divide(5, 2))
AssertionError: 2.5 != 2

----------------------------------------------------------------------
Ran 4 tests in 0.003s

FAILED (failures=2)
```

1. The mark is given on four different test case `FF..`. `F` detnotes "Fail", `.` denotes "Success", `E` denotes "Error", and `S` denotes "Skip". 

2. Each test should start with `test`, otherwise it would not be recognized. 

3. The more detailed information can be shown with the argument `verbosity`. `verbosity` is set 1 as default. If `verbosity` is set 0, the execution result will not be output, whereas if `verbosity` is set 2, more detailed information will be output. 

---

Exercise 2: Do the unit test with unit-test framework for OSS project.

Here are two great tutorials 

[Getting Started with Testing in Python](https://realpython.com/python-testing/)

[Framework of Unit Test](https://docs.python.org/3/library/unittest.html)

`unittest` supports some important concept in an object-oriented way:

`test fixture` : A *test fixture* represents the preparation needed to perform one or more tests, and any associated cleanup actoons.  

`text case`: A *test case* is the individual unit of testing. It checks for a specific response to a particular set of inputs. `unittest` provides a base class, `TestCase`, which may be used to create new test cases.

`text suite`: A *test suite* is a collection of test cases, test suites, or both. It used to aggregate tests that should be executed together.

`text runner`: A *test runner* is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests. 

Here is an example following test in Exercise 1:

```
import unittest
from test_mathfunc import TestMathFunc

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
```

The output is as the following:

```
(base) zhangxinjie@192 python -u "/test_suite.py" 
test_add (test_mathfunc.TestMathFunc) ... FAIL
test_minus (test_mathfunc.TestMathFunc) ... ok
test_divide (test_mathfunc.TestMathFunc) ... FAIL

======================================================================
FAIL: test_add (test_mathfunc.TestMathFunc)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/test_mathfunc.py", line 8, in test_add
    self.assertNotEqual(3, add(1, 2))
AssertionError: 3 == 3

======================================================================
FAIL: test_divide (test_mathfunc.TestMathFunc)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/test_mathfunc.py", line 18, in test_divide
    self.assertEqual(2.5, divide(5, 2))
AssertionError: 2.5 != 2

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=2)

```

The cases were executed with the given order. The results can be output to a file with the following code:

```
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    with open('UnittestTextReport.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)

```

`unittest.skip()` can be used to skip some cases. 

In summary, the flow of `unittest` is as the following:

1. Write TestCase.

2. Load TestCase to TestSuite with `TestLoader`.

3. Run TestSuite with `TextTestRunner`. The result will be kept in `TextTestResult`.

4. A class inherits from unittest.TestCase is a TestCase. 

5. case and suite can be added with `addTest`, `addTests` and `loadTestsFrom()` in `TestLoader`. 

---

Exercise 3: Add functions to the OSS project with the way of test-driven development.

The flow of Test Driven Development is as the following:

1. Determine the specifications of the function you want to create

2. Write a test

3. Run test → compilation fails

4. Write an empty function to implement

5. Run test → test fails

6. Implement the function

7. Run test → test succeeds

In the task 2 in the OSS-project [Task 2: Deterministic Binary Neuron Model](https://github.com/ZxjSamantha/System-Development-Studio/tree/main/OSS-project/task02)

The solution is given that the final state of neurons should be (1, 0, 1, 0) and the final energy of the state should be 0. There should be a function to get the final state and a function to get the energy.  

The test case is as the following:

```
import unittest

class TestBM1(unittest.TestCase):

    def test_finalState(self):
        self.assertEqual([1,0,1,0], update([0, 0, 0, 0]))
        self.assertNotEqual([1,0,1,0], update([0, 0, 0, 0]))
    
    def test_finalEnergy(self):
        self.assertEqual(0, energyFunc(update([0, 0, 0, 0])))
        #self.assertNotEqual(0, energyFunc(update([0, 0, 0, 0])))

if __name__ =='__main__':
    unittest.main()
```

The output is as the following:

```
(BCI) zhangxinjie@zhangxijiedeAir task02 % python -u "~/test_BM1.py"
EE
======================================================================
ERROR: test_finalEnergy (__main__.TestBM1)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "~/test_BM1.py", line 11, in test_finalEnergy
    self.assertEqual(0, energyFunc(update([0, 0, 0, 0])))
NameError: global name 'energyFunc' is not defined

======================================================================
ERROR: test_finalState (__main__.TestBM1)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "~/test_BM1.py", line 7, in test_finalState
    self.assertEqual([1,0,1,0], update([0, 0, 0, 0]))
NameError: global name 'update' is not defined

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (errors=2)
```

The functions should be tested are as the following:

```
import numpy as np
from random import choice 

def energyFunc(states = []):
    length = len(states)
    x = list(range(length))
    for i in range(length):
        x[i] = states[i]
    E = (x[0] - x[1] + x[2] + x[3] -2)**2 + ((-1)*x[0] + 2*x[1] -x[2] -x[3] + 2)**2 + (2*x[0] - x[1] + 2*x[2] + x[3] -4)**2 + ((-1)*x[0] + (-1)*x[1] + x[2] + x[3])**2 
    return E

def statesUpdate(currentStates = []):
    tempStates = currentStates
    neuron = choice(currentStates)
    idx = currentStates.index(neuron)
    tempStates[idx] = 1 - currentStates[idx]
    energyChange = energyFunc(tempStates) - energyFunc(currentStates)
    if energyChange < 0: 
        return tempStates
    else: return currentStates

def update(currentState = []):
    E = energyFunc(currentState)
    while(E > 0):
        currentState = statesUpdate(currentState)
        E = energyFunc(currentState)
    return currentState

if __name__ == "__main__":
    initialStates = [0, 0, 0, 0]
    #initialStates = [1, 1, 1, 1]
    #initialStates = [0,1,0,1]
    currentStates = initialStates
    energy = []
    result = update(initialStates)
```

The output of the current test case is as the following:

```
(BCI) zhangxinjie@zhangxijiedeAir task02 % python -u "～/test_BM1.py"
..
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
```

Update: Leetcode and AtCoder adopts TDD to design the problems. 
