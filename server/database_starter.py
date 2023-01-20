import sys
import sqlite3


class DatabaseStarter:
    def __init__(self):
        self.directory = '/data/book_database.db'
        self.db = self.__connect()
    
    #connect with dabase
    def __connect(self):
        return sqlite3.connect(self.__get_parent_directory()+ self.directory)

    #get parent directory and
    def __get_parent_directory(self):
        list = sys.path[0].split('/')
        return_str = ''
        for element in list:
            return_str += element + '/'
        return return_str.rstrip('/')
