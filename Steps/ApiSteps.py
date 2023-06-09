import os
from dotenv import load_dotenv
from allure import step


class ApiSteps:

    def __init__(self, session, token):
        self.session = session
        self.token = token

    def auth_by_api(self):
        with step('auth_by_api'):
            load_dotenv()
            self.session.headers['token'] = self.token
            self.session.json = {'Password': os.getenv('password'), 'Contract': os.getenv('contract')}
            self.session.post('auth')

    def get_token(self):
        with step('get_token'):
            return self.token