from server import DatabaseStarter


class QueryExecuter:
    def __init__(self) -> None:
        self.db = DatabaseStarter().db
    
    def execute_query(self, params=None):
        pass
    
    def build_dict(self, cursor):
        final_data = []
        for row in cursor:
            page = dict((column[0],row[index]) for index, column in enumerate(cursor.description))
            final_data.append(page)
        
        return final_data