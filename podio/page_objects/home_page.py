from podio.common.page import Page


class HomePage(Page):
    ELEMENTS = {
        'status': ('status_value', 'id'),
        'status_submit': '.status-submit',
        'default_workspace': '.focused',
        'first_stream_post': '.stream-post',
        'first_steam_post_title': '.stream-post .title p'
    }

    def wait_for_stream(self, text):
        self.driver.is_text_present(text)