from datetime import datetime
import random

from allure import step
from objects.user import User
from pytest_voluptuous import S
from models.usermodel import *


class Step:
    """dict for keeping expected results of parameters which get executing steps of test"""
    EXPECTED_DICT = {}

    """dict for keeping actual results of parameters which get executing steps of test"""
    ACTUAL_DICT = {}

    def __init__(self, req):
        self.req = req

    def get_user_quantity(self):
        """step gets user quantity and saves it in EXPECTED_DICT and ACTUAL_DICT"""

        with step('get_user_quantity'):
            data_users = User.get_user_list(self.req)
            self.EXPECTED_DICT['total'] = data_users['total']
            self.ACTUAL_DICT['total'] = 0
            for i in range(1, data_users['total_pages'] + 1):
                self.ACTUAL_DICT['total'] += len(User.get_user_list(self.req, i)['data'])

    def create_new_user(self):
        with step('create_new_user'):
            self.EXPECTED_DICT['name'] = 'test'
            self.EXPECTED_DICT['job'] = 'test'
            user = User()
            user.create_user(name='test', job='test', req=self.req)
            self.ACTUAL_DICT['name'] = user.name
            self.ACTUAL_DICT['job'] = user.job

    def get_users_list(self):
        with step('get_users_list'):
            page = 1
            self.ACTUAL_DICT['response'] = []
            while True:
                response = User.get_user_list(self.req, page=page)
                self.ACTUAL_DICT['response'].append(response)
                if response['total_pages'] > page:
                    page += 1
                else:
                    break

    def get_total_page_parameter(self):
        with step('get_total_page_parameter'):
            user_list = User.get_user_list(self.req)
            self.ACTUAL_DICT['total_pages'] = user_list['total_pages']
            self.ACTUAL_DICT['total'] = user_list['total']
            self.ACTUAL_DICT['per_page'] = user_list['per_page']

    def get_random_single_user_from_user_list(self):
        with step('get_random_single_user_from_user_list'):
            response_item = random.randint(0, len(self.ACTUAL_DICT['response']) - 1)
            data_user_item = random.randint(0, len(self.ACTUAL_DICT['response'][response_item]['data']) - 1)
            self.ACTUAL_DICT['single_user'] = self.ACTUAL_DICT['response'][response_item]['data'][data_user_item]
            self.EXPECTED_DICT['single_user'] = User.get_single_user(self.req, self.ACTUAL_DICT['single_user']['id'])

    def get_status_code_unsuccessful_register(self):
        with step('get_status_code_unsuccessful_register'):
            user = User()
            self.ACTUAL_DICT['status_code'] = user.register_user_without_pass(self.req).status_code
            self.EXPECTED_DICT['status_code'] = 400

    def get_status_code_user_list_response(self):
        with step('get_status_code_user_list_response'):
            self.EXPECTED_DICT['status_code'] = 200
            self.ACTUAL_DICT['status_code'] = User.get_status_code_user_list(self.req)

    def get_data_creating_user(self):
        with step('get_data_creating_user'):
            user = User()
            user.create_user(req=self.req, job='test', name='test')
            self.ACTUAL_DICT['createdAt'] = user.createdAt[2:10]

    def get_token_after_register(self):
        with step('get_token_after_register'):
            user = User()
            self.ACTUAL_DICT['token'] = user.register_user(self.req)['token']

    def register_user_without_password(self):
        with step('register_user_without_password'):
            user = User()
            self.ACTUAL_DICT['error_message'] = user.register_user_without_pass(self.req).json()['error']
            self.EXPECTED_DICT['error_message'] = 'Missing password'

    def assert_quantity_users(self):
        """assertion total quantity from ACTUAL_DICT and EXPECTED_DICT"""

        with step('assert_quantity_users'):
            assert self.ACTUAL_DICT['total'] == self.EXPECTED_DICT['total']

    def assert_existing_user(self):
        with step('assert_existing_user'):
            assert self.ACTUAL_DICT['name'] == self.EXPECTED_DICT['name']
            assert self.ACTUAL_DICT['job'] == self.EXPECTED_DICT['job']

    def assert_users_list_model(self):
        with step('assert_users_list_model'):
            for i in range(len(self.ACTUAL_DICT['response'])):
                assert S(UserModels.list_users_model) == self.ACTUAL_DICT['response'][i]

    def assert_total_pages(self):
        with step('assert_total_pages'):
            assert self.ACTUAL_DICT['total_pages'] == self.ACTUAL_DICT['total'] // self.ACTUAL_DICT['per_page']

    def assert_single_user_to_user_from_list(self):
        with step('assert_single_user_to_user_from_list'):
            assert self.EXPECTED_DICT['single_user']['data'] == self.ACTUAL_DICT['single_user']

    def assert_status_code(self):
        with step('assert_status_code'):
            assert self.ACTUAL_DICT['status_code'] == self.EXPECTED_DICT['status_code']

    def assert_date_creating_user(self):
        with step('assert_date_creating_user'):
            self.EXPECTED_DICT['createdAt'] = datetime.today().strftime('%y-%m-%d')
            assert self.ACTUAL_DICT['createdAt'] == self.EXPECTED_DICT['createdAt']

    def assert_token_length(self):
        with step('assert_token_length'):
            assert len(self.ACTUAL_DICT['token']) == 17

    def assert_error_message(self):
        with step('assert_error_message'):
            assert self.ACTUAL_DICT['error_message'] == self.EXPECTED_DICT['error_message']
