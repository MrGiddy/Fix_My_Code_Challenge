#!/usr/bin/python3
"""
Defines User class
"""


class User():
    """ Represents a User """

    def __init__(self):
        """ Initializes a User """
        self.__email = None

    @property
    def email(self):
        """ Retrieves a User's email """
        return self.__email

    @email.setter
    def email(self, value):
        """ Sets a User's email to a value """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
