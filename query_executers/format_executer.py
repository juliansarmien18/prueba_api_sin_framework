from query_executers.query_executer import QueryExecuter
import sqlite3


class FormatExecuter(QueryExecuter):
    def __init__(self) -> None:
        super().__init__()

    def execute_query(self, params : dict):
        if not 'format' in params.keys():
            requested_format = 'html'
        else:
            requested_format = params['format']
        try:
            conn = self.db
            c = conn.cursor()
            cursor = c.execute("select * from Formats where format =?;",[requested_format])
        except Exception as e:
            raise sqlite3.DatabaseError
        else:
            return self.build_dict(cursor)




