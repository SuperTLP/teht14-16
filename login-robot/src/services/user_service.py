
import sys, pdb

from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        elif len(username)<3:
            raise UserInputError("Username must be at least 3 characters long and contain only characters a-z.")
        elif len(password)<8:
            raise UserInputError("Password must be at least 8 characters long and must contain numbers or special characters.")
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        for i in username:
            if not i in letters:
                raise UserInputError("Username must be at least 3 characters long and contain only characters a-z.")
        validPass = 0
        for i in password:
            if not i in letters:
                validPass+=1
        if validPass==0:
            raise UserInputError("Password must be at least 8 characters long and must contain numbers or special characters.")
