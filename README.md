# Requirements

* Python 2.7 or greater
* Virtualenv
* Pip

## Install

Linux/Mac
```bash
virtualenv ENV
source ENV/bin/activate
cd to the git project
pip install -r requirements.txt
export PYTHONPATH=$(pwd)
```

Windows (cmd.exe)
```bash
virtualenv ENV
cd ENV\Scripts
activate.bat
cd to the git project
pip install -r requirements.txt
```

## Package Overview

Some of the packages installed via pip

* [selenium](https://selenium.googlecode.com/git/docs/api/py/api.html) - For interacting with the browser
* [splinter](http://splinter.cobrateam.info/) - An abstraction layer on top of selenium, underlying driver for behaving
* [behave](https://github.com/behave/behave) - Behavior Driven Development (BDD) framework for creating non-technical feature and scenario tests using Gherkin syntax to execute steps
* [behaving](https://github.com/ggozad/behaving) - Predefined steps in behave which are used for controlling the browser
* [fake-factory](https://github.com/joke2k/faker) - Used to generate random data


## Running Tests

As long as you set a proper `PYTHONPATH` to the root directory, you can run tests from within any directory. See behave documentation on how to add tags for running one test of many.
Linux/Mac

```bash
$ # Run single test
$ behave podio/features/login.feature
$ # Alternatively, run all files in features directory
$ behave podio/features
```

Windows
```bash
$ cd <root_directory_path>
$ # Run single test
$ behave podio\features\login.feature
$ # Alternatively, run all files in features directory
$ behave podio\features

## Environment settings

These environment variables influence settings and data drawn from [sites.yaml]

### ENV

Defaults to *production*

`export ENV=production`

### BROWSER

Defaults to *firefox*

`export BROWSER=chrome`

`Note: changing to the browser under test to chrome may require installing chromedriver:
http://chromedriver.storage.googleapis.com/index.html`

