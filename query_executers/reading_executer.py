from query_executers.query_executer import QueryExecuter
import sqlite3


class ReadingExecuter(QueryExecuter):
    def __init__(self) -> None:
        super().__init__()
        self.page_query = "SELECT Books.name, Pages.book_id, Pages.page, Pages.content FROM Books, Pages WHERE  Books.id =? and Pages.book_id = Books.id and Pages.page =?"
        self.book_query = "SELECT Books.name, Pages.book_id, Pages.page, Pages.content FROM Books, Pages WHERE  Books.id =? and Pages.book_id = Books.id"

    def execute_query(self, params : dict):
        if params:
            if not 'book' in params.keys():
                raise KeyError
            try:
                c = self.db
                if not 'page' in params.keys():
                    cursor = c.execute(self.book_query, [int(params['book'])])
                else:
                    cursor = c.execute(self.page_query, [int(params['book']), int(params['page'])])
            except Exception as e:
                raise sqlite3.DatabaseError
            else:
                data = self.build_dict(cursor)
                c.close()
                return data