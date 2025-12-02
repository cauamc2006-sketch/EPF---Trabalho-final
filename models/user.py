import json
import os
from dataclasses import dataclass, asdict
from typing import List

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
class User:
    def __init__(self, id: int, username: str, password: str, email: str ):
        self.id = id
        self.username = username
        self.password = password   
        self.email = email

    def check_password(self, password: str) -> bool:
        return self.password == password

    def update(self, username=None, password=None, email=None):
        if username:
            self.username = username
        if password:
            self.password = password
        if email:
            self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email": self.email
        }

    @staticmethod
    def from_dict(data: dict):
        return User(
            id=data["id"],
            username=data["username"],
            password=data["password"],
            email=data.get("email")
        )



class UserModel:
    FILE_PATH = os.path.join(DATA_DIR, 'users.json')

    def __init__(self):
        self.users = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []

        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [User.from_dict(item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.users

    def get_by_id(self, user_id: int):
        return next((u for u in self.users if u.id == user_id), None)

    def get_by_username(self, username):
        for u in self.users:
            if u.username == username:
                return u
        return None


    def add_user(self, user: User):
        self.users.append(user)
        self._save()

    def update_user(self, updated_user: User):
        for i, u in enumerate(self.users):
            if u.id == updated_user.id:
                self.users[i] = updated_user
                self._save()
                break

    def delete_user(self, user_id: int):
        self.users = [u for u in self.users if u.id != user_id]
        self._save()