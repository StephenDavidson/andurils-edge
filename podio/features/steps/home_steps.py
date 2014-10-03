from podio.common.user_generator.generator import User
from podio.page_objects.home_page import HomePage
from behave import step
from behaving.web.steps import *

@step('I enter a status post')
def enter_status(context):
    home_page = HomePage(context.browser)
    user = context.user
    home_page['status'].click()
    home_page['status'].fill(user['sentence'])

@step('I submit the status post')
def submit_status(context):
    home_page = HomePage(context.browser)
    home_page['status_submit'].click()
    home_page['default_workspace'].click()

@step('I should see the status post')
def should_see_status(context):
    home_page = HomePage(context.browser)
    user = context.user
    home_page.wait_for_stream(user['sentence'])
    assert(user['sentence'] in home_page['first_steam_post_title'].text)