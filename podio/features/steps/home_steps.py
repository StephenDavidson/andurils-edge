from podio.common.user_generator.generator import User
from podio.page_objects.home_page import HomePage
from behave import step
from behaving.web.steps import *

@step('I enter a status post')
def enter_status(context):
    home_page = context.page
    user = context.user
    home_page['status'].fill(user['sentence'])

@step('The status post should be displayed')
def should_see_status(context):
    home_page = context.page
    user = context.user
    home_page.wait_for_text_present(user['sentence'])
    assert(user['sentence'] in home_page['first_steam_post_title'].text)