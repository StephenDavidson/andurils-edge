# Requirements

* Python 2.7 or greater
* Virtualenv
* Pip

## Install

```bash
virtualenv ENV
source ENV/bin/activate
pip install -r requirements.txt
export PYTHONPATH=$(pwd)
```

## Package Overview

Some of the packages installed via pip

* [selenium](https://selenium.googlecode.com/git/docs/api/py/api.html) - For interacting with the browser
* [splinter](http://splinter.cobrateam.info/) - An abstraction layer on top of selenium, underlying driver for behaving
* [behave](https://github.com/behave/behave) - Behavior Driven Development (BDD) framework for creating non-technical feature and scenario tests using Gherkin syntax to execute steps
* [behaving](https://github.com/ggozad/behaving) - Predefined steps in behave which are used for controlling the browser
* [requests](http://docs.python-requests.org/en/latest/) - Used to communicate with APIs
* [fake-factory](https://github.com/joke2k/faker) - Used to generate random data
* [epydoc](http://epydoc.sourceforge.net/) - Documentation generator


## Running Tests

As long as you set a proper `PYTHONPATH` to the root directory, you can run tests from within any directory. See behave documentation on how to add tags for running one test of many.
```bash
$ # Run single test
$ behave lib/testrepo/behaving/features/demo.feature
$ # Alternatively, run all files in features directory
$ behave lib/testrepo/behaving/features
```

## Environment settings

These environment variables influence settings and data drawn from [app.yaml](https://github.rackspace.com/rswebteam/qe/blob/master/config/app.yaml)

### ENV

Defaults to *staging*

`export ENV=qe`

### BROWSER

Defaults to *firefox*

`export BROWSER=chrome`

`Note: changing to the browser under test to chrome may require installing chromedriver:
http://chromedriver.storage.googleapis.com/index.html`

