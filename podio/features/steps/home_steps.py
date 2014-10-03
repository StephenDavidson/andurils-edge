from podio.common.user_generator.generator import User
from podio.page_objects.home_page import HomePage
from behave import step
from behaving.web.steps import *

@step('I enter a status post')
def enter_status(context):
    home_page = HomePage(context.browser)
    user = context.user
    home_page['status'].fill(user['sentence'])

@step('I click share post')
def share_post(context):
    home_page = HomePage(context.browser)
    home_page['status'].click()
    home_page['status_submit'][0].click()

@step('I select the default workspace')
def select_default_workspace(context):
    home_page = HomePage(context.browser)
    home_page['default_workspace'][0].click()

@step('I should see the status post')
def should_see_status(context):
    home_page = HomePage(context.browser)
    user = context.user
    home_page.wait_for_stream(user['sentence'])
    assert(user['sentence'] in home_page['first_steam_post_title'].text)

@step('I should see a status post error icon')
def should_see_error_icon(context):
    home_page = HomePage(context.browser)
    assert home_page['status_error_icon'][0].visible