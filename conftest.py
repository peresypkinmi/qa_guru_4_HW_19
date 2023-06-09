import pytest
from BaseSession.BaseSession import BaseSession
import os
from dotenv import load_dotenv
from Steps.ApiSteps import ApiSteps

@pytest.fixture()
def get_base_url():
    return "https://reqres.in/api/"


@pytest.fixture()
def get_reqres(get_base_url):
    return BaseSession(base_url=get_base_url)

@pytest.fixture()
def get_token(get_sw_session):
    load_dotenv()
    return get_sw_session.get('myValidToken').json()['Model']['Token']

@pytest.fixture()
def get_sw_session():
    load_dotenv()
    return BaseSession(base_url=os.getenv('baseUrl'))

@pytest.fixture()
def api_step(get_token, get_sw_session):
    return ApiSteps(get_sw_session, get_token)

