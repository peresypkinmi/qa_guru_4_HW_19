from requests import Session
from allure import step
import logging
import curlify
import allure
from allure_commons.types import AttachmentType


class BaseSession(Session):

    def __init__(self, **kwargs):

        self.base_url = kwargs.pop('base_url')
        self.params = {}
        self.json = None
        super().__init__()


    def request(self, method, url, **kwargs):
        with step(f'{method} {url}'):
                response = super().request(method, url=f'{self.base_url}{url}', **kwargs)
                contentType = response.headers['content-type']
                logging.info(curlify.to_curl(response.request))
                if 'text' in contentType:
                    logging.info(response.text)
                elif 'json' in contentType:
                    logging.info(response.json())
                log = str(response.json())
                allure.attach(f'status_code: {response.status_code} {curlify.to_curl(response.request)}', 'request', AttachmentType.TEXT, '.log')
                allure.attach(log, 'response', AttachmentType.TEXT, '.log')

                return response

    def post(self, url, data=None, json=None, **kwargs):
        return super().post(url, json=self.json, **kwargs)