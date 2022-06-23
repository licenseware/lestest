# Lestest
<img src="./coverage.svg">


Generate boilerplate unittests from given package. Ensures each class or function has a corespondent test. 



## Generate boilerplate tests

From the command line to generate unittest with pytest and tox type:
```bash

$ lestest generate

```

The above command will search in the current folder python packages from which it will generate boilerplate tests in the `tests` folder.

The boilerplate test generated will contain the import for the class or function found in the package and the test function which will trigger the test.

Trimmed down version of the boilerplate test file:
```py
# test_function_name.py
import pytest
from package.module import function_name


def test_function_name():

    function_name()

```

Package `lestest` will try to generate some mock parameters based on the function/class parameters and provide a default assertion based on the response type.

> *Try to use types as much as posible, this way you will have less work to do in the test.*

If you create new functions just run `lestest generate` and those will have a new coresponded test case.


## Run tests

Tests can be triggered with `tox tests/test_*`. 
After the test completes you will get also the test coverage.


## Update boilerplate templates

In the terminal type:
```bash

$ lestest boilerplate

```

The above command will generate `lestest_templates` directory which will contain all jinja templates used in generation of tests. You can update with your own fixtures, common imports and so on. The updated templates will be used to create new tests.



## Extend `lestest`

You can import and extend or modify `lestest` package functionality. Create a module named `lestest_extended.py` in which you can do the following:

```py

from lestest import Lestest


class ExtendedLestest(Lestest):

    def generate(self):
        pass

    # etc    

```

This way you can alter functionality in any way you want.


## Developing

- clone the repository;
- install virtualenv: `pip3 install virtualenv`;
- create virtualenv: `virtualenv ./`;
- activate virtualenv: `source ./bin/activate`;
- install dependencies: `pip3 install -r requirements.txt`;
- run tests: `python3 -m unittest tests/test_*`;
- run tests with coverage: `coverage run --source=lestest -m unittest tests/test_*`;
- generate html files to see coverage details: `coverage html`;
- see coverage details in the terminal: `coverage report -m`; 
- create coverage badge from coverage created: `coverage-badge -o coverage.svg`;