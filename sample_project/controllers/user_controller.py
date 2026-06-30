from repositories.user_repository import UserRepository


class UserController:

    def __init__(self):
        self.repository = UserRepository()

    def get_user(self):
        return self.repository.get_user()