from models.user import UserModel
from models.user import User


class UserService:
    def __init__(self):
        self.user_model = UserModel()

    def get_all(self):
        return self.user_model.get_all()

    def get_by_id(self, user_id: int):
        return self.user_model.get_by_id(user_id)

    def get_by_username(self, username: str):
        return self.user_model.get_by_username(username)

    def register(self, username: str, password: str, email: str = None):

        if self.user_model.get_by_username(username):
            return None, "Usuário já existe!"

        new_id = len(self.user_model.get_all()) + 1

        user = User(
            id=new_id,
            username=username,
            password=password,
            email=email
        )

        self.user_model.add_user(user)

        return user, None

    def login(self, username: str, password: str):

        user = self.user_model.get_by_username(username)

        if not user:
            return None, "Usuário não encontrado!"

        if not user.check_password(password):
            return None, "Senha incorreta!"

        return user, None

    def update(self, user: User):
        self.user_model.update_user(user)

    def delete(self, user_id: int):
        self.user_model.delete_user(user_id)


