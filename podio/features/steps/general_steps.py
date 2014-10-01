from podio.common.user_generator.generator import User
import podio.page_objects
from behave import step
from behaving.web.steps import *


@step('I visit the {page_name} page')
def visit(context, page_name):
    context.browser.visit(context.sites['url'] + page_name)

@step('I am a "{user_type}" user')
def step_define_signup_user(context, user_type):
    context.user = User.create(user_type)