from selene.support.shared import browser
from selene import be, have
from allure import step


class UISteps:

    def __init__(self):
        browser.config.window_width = '1920'
        browser.config.window_height = '1080'

    def open_main_page_as_auth_user(self, token):
        with step("open_main_page_as_auth_user"):
            browser.open('https://kz.siberianwellness.com/kz-ru/favico.ico')
            browser.driver.add_cookie({'name': 'token', 'value': token})
            browser.open("https://kz.siberianwellness.com/kz-ru/")
            return self

    def check_user_name(self):
        with step('check_user_name'):
            browser.element('[data-qa=VUSERBAR_NAME]').should(be.visible).should(have.exact_text('Testyyui Testeeoi'))
            return self
