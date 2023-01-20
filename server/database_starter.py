import sys
import sqlite3


class DatabaseStarter:
    def __init__(self) -> None:
        self.db = self.__connect()
    
    def __connect(self):
        print(self.__get_parent_directory()+'/data/book_database.db')
        return sqlite3.connect(self.__get_parent_directory()+'/data/book_database.db')

    def __get_parent_directory(self):
        list = sys.path[0].split('/')
        return_str = ''
        for element in list:
            return_str += element + '/'
        return return_str.rstrip('/')
