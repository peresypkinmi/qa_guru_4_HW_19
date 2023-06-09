from Steps.Step import Step


class TestUsers:

    def test_get_user_quantity(self, get_session):

        step = Step(get_session)

        step.get_user_quantity()

        step.assert_quantity_users()

    def test_create_user(self, get_session):

        step = Step(get_session)

        step.create_new_user()

        step.assert_existing_user()

    def test_check_user_list_schema(self, get_session):

        step = Step(get_session)

        step.get_users_list()

        step.assert_users_list_model()

    def test_total_page_in_user_list(self, get_session):
        step = Step(get_session)

        step.get_total_page_parameter()

        step.assert_total_pages()

    def test_compare_users_and_single_user_data(self, get_session):
        step = Step(get_session)

        step.get_users_list()
        step.get_random_single_user_from_user_list()

        step.assert_single_user_to_user_from_list()

    def test_status_code_user_list(self, get_session):
        step = Step(get_session)

        step.get_status_code_user_list_response()

        step.assert_status_code()

    def test_date_create_user(self, get_session):
        step = Step(get_session)

        step.get_data_creating_user()

        step.assert_date_creating_user()

    def test_check_token(self, get_session):
        step = Step(get_session)

        step.get_token_after_register()

        step.assert_token_length()

    def test_unsuccessful_register(self, get_session):
        step = Step(get_session)

        step.register_user_without_password()

        step.assert_error_message()

    def test_400_response_unsuccessful_register(self, get_session):
        step = Step(get_session)

        step.get_status_code_unsuccessful_register()

        step.assert_status_code()
