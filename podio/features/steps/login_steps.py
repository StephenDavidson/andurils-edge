from behave import step
from behaving.web.steps import *
from podio.page_objects.login_page import LoginPage


@step('I have valid credentials')
def set_valid_credentials(context):
    context.user['email'] = context.accounts['email']
    context.user['password'] = context.accounts['password']

@step('I fill in the login form')
def fill_login_form(context):
    page = context.page
    user = context.user
    page['email'].fill(user['email'])
    page['password'].fill(user['password'])

@step('I should receive a login warning message')
def should_see_warning(context):
    login_page = context.page
    warning = login_page['warning']
    assert(warning.visible and warning.text)