#Date: 13.11.2016
#Author of file: Simon

import random
import sys
import os


class User:
    __firstname = None
    __lastname = None
    __gender = None
    __age = None
    __disabled = None


    def __init__(self, firstname, lastname, gender, age, disabled):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__gender = gender
        self.__age = age
        self.__disabled = disabled


    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age

    def get_disabled(self):
        return self.__disabled