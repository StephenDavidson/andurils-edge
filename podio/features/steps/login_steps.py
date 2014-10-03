from behave import step
from behaving.web.steps import *
from podio.page_objects.login_page import LoginPage


@step('I have valid credentials')
def set_valid_credentials(context):
    context.user['email'] = context.accounts['email']
    context.user['password'] = context.accounts['password']

@step('I fill in the login form')
def fill_login_form(context):
    page = LoginPage(context.browser)
    user = context.user
    page['email'].fill(user['email'])
    page['password'].fill(user['password'])

@step('I submit the login form')
def submit(context):
    LoginPage(context.browser)['submit'].click()