from query_executers.query_executer import QueryExecuter
import sqlite3
import os


class FormatExecuter(QueryExecuter):
    def __init__(self) -> None:
        super().__init__()

    def execute_query(self, params=None):
        try:
            conn = self.db
            c = conn.cursor()
            cursor = c.execute('select * from Formats')
        except Exception as e:
            raise sqlite3.DatabaseError
        else:
            return self.build_dict(cursor)




