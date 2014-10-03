from podio.common.page import Page


class LoginPage(Page):
    path = '/login'

    ELEMENTS = {
        'email': '#email',
        'password': '#password',
        'submit': ('commit', 'name'),
        'warning': '.warning'
    }