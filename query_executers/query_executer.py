from server.database_starter import DatabaseStarter

#Parent Class
class QueryExecuter:
    
    #open conecction with database
    def __init__(self) -> None:
        self.db = DatabaseStarter().db.cursor()
    
    #parent method wghich is empty in order to modify it
    def execute_query(self, params=None):
        pass
    
    #build dictionary from queries
    def build_dict(self, cursor):
        final_data = []
        for row in cursor:
            page = dict((column[0],row[index]) for index, column in enumerate(cursor.description))
            final_data.append(page)
        
        return final_data