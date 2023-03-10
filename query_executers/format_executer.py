from query_executers.query_executer import QueryExecuter
import sqlite3

#child class from QueryExecuter
class FormatExecuter(QueryExecuter):
    def __init__(self) -> None:
        super().__init__()

    #Execute query, and call parent method build_dict in order to return it
    def execute_query(self, params : dict):
        if not 'format' in params.keys():
            requested_format = 'html'
        else:
            requested_format = params['format']
        try:
            c = self.db
            cursor = c.execute("select * from Formats where format =?;",[requested_format])
        except Exception as e:
            raise sqlite3.DatabaseError
        else:
            data = self.build_dict(cursor)
            c.close()
            return data




