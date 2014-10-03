from podio.common.user_generator.generator import User
from podio.page_objects import pages
from behave import step
from behaving.web.steps import *


@step('I visit the {page_name} page')
def visit(context, page_name):
    context.page = pages[page_name.lower()](context.browser)
    context.browser.visit(context.sites['url'] + context.page.path)

@step('I am on the {page_name} page')
def on_page(context, page_name):
    context.page = pages[page_name.lower()](context.browser)


@step('I click the {element_name} button')
def click_element(context, element_name):
    context.page[element_name].click()

@step('I click the {element_name}')
def click_element(context, element_name):
    context.page[element_name].click()

@step('I should see the {element_name}')
def should_see_error_icon(context, element_name):
    assert context.page[element_name].visible

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
        and I click the submit button
    ''')