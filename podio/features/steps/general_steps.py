from podio.common.user_generator.generator import User
import podio.page_objects
import podio.features.steps.login_steps
from behave import step
from behaving.web.steps import *


@step('I visit the {page_name} page')
def visit(context, page_name):
    context.browser.visit(context.sites['url'] + page_name)

@step('I should be on the {page_name} page')
def should_be_on_page(context, page_name):
    assert page_name in context.browser.url

@step('I am a "{user_type}" user')
def create_user(context, user_type):
    context.user = User.create(user_type)

@step('I log in')
def log_in(context):
    context.execute_steps(u'''
        given I visit the login page
        and I am a "random" user
        and I have valid credentials
        when I fill in the login form
        and I submit the login form
    ''')