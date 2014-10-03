import errno
import logging
import json
import os
import re
import time
from behaving.web import environment as benv
from behaving.web.steps import browser
import config



def before_all(context):
    benv.before_all(context)
    environment = os.environ.get('ENV', 'production').lower()
    context.accounts = config.accounts[environment]
    context.sites = config.sites[environment]
    context.default_browser = os.environ.get('BROWSER', 'chrome')


def after_all(context):
    context.default_browser = ''
    benv.after_all(context)


def before_scenario(context, scenario):
    benv.before_scenario(context, scenario)


def after_scenario(context, scenario):
    if context.failed:
        capture_step_failure(context, scenario)
    benv.after_scenario(context, scenario)


def create_step_failure_directory(scenario, step):
    feature_dir = re.sub(r'[^a-zA-Z]', '_', scenario.feature.name)
    step_dir = re.sub(r'[^a-zA-Z]', '_', step.name)

    reports_dir = os.path.realpath(os.path.join(os.path.dirname(config.__file__), '..', 'reports'))

    try:
        os.makedirs(os.path.join(reports_dir, 'failures', feature_dir))
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    try:
        os.makedirs(os.path.join(reports_dir, 'failures', feature_dir, step_dir))
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    return os.path.join(reports_dir, 'failures', feature_dir, step_dir)


def capture_step_failure(context, scenario):
    basename = time.strftime("%Y-%m-%d-%H%M%S", time.gmtime(time.time()))
    for step in scenario.steps:
        if step.status == 'failed':
            directory = create_step_failure_directory(scenario, step)
            try:
                if context.log_data:
                    with open(os.path.join(directory, basename + '.json'), 'w+') as log_data:
                        json.dump(context.log_data, log_data)
            except AttributeError:
                pass
            filename = os.path.join(directory, basename)
            context.browser.screenshot(filename)
            context.screenshots_dir = ''

