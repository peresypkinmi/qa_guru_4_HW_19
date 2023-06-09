from dataclasses import dataclass


@dataclass()
class User:
    id: int = 0
    name: str = ''
    job: str = ''
    createdAt: str = ''

    @staticmethod
    def get_user_list(req, page=1):
        req.params['page'] = page
        return req.get('users').json()

    @staticmethod
    def get_single_user(req, user_id: str):
        req.params['id'] = user_id
        return req.get('users').json()

    def create_user(self, job: str, name: str, req):
        req.json = {'job': job,
                    'name': name}

        data_user = req.post('users').json()
        self.id = data_user['id']
        self.name = data_user['name']
        self.job = data_user['job']
        self.createdAt = data_user['createdAt']

    @staticmethod
    def register_user_without_pass(req):
        req.json = {"email": "eve.holt@reqres.in"}
        data_user = req.post('register')
        return data_user

    @staticmethod
    def get_status_code_user_list(req, page=1):
        req.params['page'] = page
        return req.get('users').status_code

    @staticmethod
    def register_user(req):
        req.json = {"email": "eve.holt@reqres.in",
                    "password": "pistol"}
        data_user = req.post('register').json()
        return data_user
