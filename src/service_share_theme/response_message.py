__author__ = 'weizheng'

from consts import *

class ReponseMessage(object):
    def __init__(self):
        self.response_content = {}

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.response_content)

    def set_error_code(self, error_code):
        self.set_response_content(ERROR_CODE_KEY, error_code)

    def set_response_content(self, key, value):
        self.response_content[key] = value