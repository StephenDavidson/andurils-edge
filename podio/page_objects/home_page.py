from podio.common.page import Page


class HomePage(Page):
    path = '/home'

    ELEMENTS = {
        'status': ('status_value', 'id'),
        'share': '.status-submit',
        'status_error_icon': '.icon-16-red-warning-triangle',
        'default_workspace': '.focused',
        'first_stream_post': '.stream-post',
        'first_steam_post_title': '.stream-post .title p'
    }