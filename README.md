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

## Setting Credentials

My preference is git-crypt(https://github.com/AGWA/git-crypt) but I wanted to make sure the project is compatible for windows machines.

The tests will not run without local valid credentials. Perform the following steps:

```
1. Make a copy of accounts.dist in the config folder and name it accounts.yaml
2. Edit the accounts.yaml
3. Add the username and password
4. Save the file
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
```

## Environment settings

These environment variables influence settings and data drawn from [sites.yaml]

### ENV

Defaults to *production*

`export ENV=production`

### BROWSER

Defaults to *chrome*

`export BROWSER=chrome`

`Note: Chrome may require installing chromedriver:
http://chromedriver.storage.googleapis.com/index.html`

`Note: Firefox currently not supported`

