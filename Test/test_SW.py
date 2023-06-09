import time
from Steps.UISteps import UISteps

import pytest
from selene.support.shared import browser
from Steps.ApiSteps import ApiSteps



class Test_SW:


    def test_auth_user(self, api_step):

        api_step.auth_by_api()

        UISteps()\
            .open_main_page_as_auth_user(api_step.get_token())\
            .check_user_name()




