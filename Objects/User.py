from dataclasses import dataclass
from requests import Request, Response


@dataclass()
class User:
    id: int = 0
    name: str = ''
    job: str = ''
    createdAt: str = ''

    @staticmethod
    def get_user_list(req, page=1):
        req.params['page'] = page
        return  req.get('users').json()


    @staticmethod
    def get_single_user(req, id: str):
        req.params['id'] = id
        s = req.get('users').json()
        return s

    def create_user(self, job: str, name: str, req):
        req.json = {'job': job,
                    'name': name}

        data_user = req.post('users').json()
        return User(data_user['id'], data_user['name'], data_user['job'], data_user['createdAt'])

    def register_user_without_pass(self, req):
        req.json = {"email": "eve.holt@reqres.in"}
        data_user = req.post('register')
        return data_user

    @staticmethod
    def get_status_code_user_list(req, page=1):
        req.params['page'] = page
        return req.get('users').status_code

    def register_user(self, req):
        req.json = {"email": "eve.holt@reqres.in",
                        "password": "pistol"}
        data_user = req.post('register').json()
        return data_user

