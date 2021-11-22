from entities.user import User
from string import ascii_letters
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")
        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")
        if len(username)<3:
            raise UserInputError("Username must be at least 3 characters long and contain only letters a-z")
        for i in username:
            if not i in ascii_letters:
                raise UserInputError("Username must be at least 3 characters long and contain only letters a-z")
        j = 0
        for i in password:
            if not i in ascii_letters:
                j+=1
        if j==0:
            raise UserInputError("Password must be at least 8 characters long and contain special characters and numbers")
            
        if self._user_repository.find_by_username(username):
            raise UserInputError("Username taken")
        if len(password)<8:
            raise UserInputError("Password must be at least 8 characters long and contain special characters and numbers")
        if password!=password_confirmation:
            raise UserInputError("Password and password confirmation do not match")
            



        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa


user_service = UserService()
