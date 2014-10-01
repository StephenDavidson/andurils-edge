from podio.common.page import Page


class LoginPage(Page):
    ELEMENTS = {
        'email': '#email',
        'password': '#password',
        'submit': ('commit', 'name')
    }