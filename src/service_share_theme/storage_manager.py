__author__ = 'weizheng'

from consts import *

class StorageManager(object):
    def __init__(self):
        self.__theme_content_root_dir = ''
        self.__account_content_root_dir = ''

    def get_storage_content(self, content_index_path, content_type):
        storage_content = None
        if content_type == STORAGE_CONTENT_TYPE_ACCOUNT_INFO:
            storage_content = self.__get_account_content(content_index_path)
        elif content_type == STORAGE_CONTENT_TYPE_THEME_INFO:
            storage_content = self.__get_theme_content(content_index_path)
        return storage_content

    def __get_theme_content(self, content_index_path):
        return None

    def __get_account_content(self, content_index_path):
        return None

    def save_content(self, content_index_path, content_type):
        if content_type == STORAGE_CONTENT_TYPE_ACCOUNT_INFO:
            self.__save_account_content(content_index_path)
        elif content_type == STORAGE_CONTENT_TYPE_THEME_INFO:
            self.__save_theme_content(content_index_path)

    def __save_theme_content(self, content_index_path):
        pass

    def __save_account_content(self, content_index_path):
        pass