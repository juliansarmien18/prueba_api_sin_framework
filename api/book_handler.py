from http.server import BaseHTTPRequestHandler
from query_executers.format_executer import FormatExecuter
from query_executers.reading_executer import ReadingExecuter

from urllib.parse import  parse_qsl
import json




class BookHandler(BaseHTTPRequestHandler): 
    
    """Open Json Files, searchs for requested params, uses the reuqested format
        and returns a json with data if exists"""
    def do_GET(self):
        format_executer = FormatExecuter()
        reading_executer = ReadingExecuter()
        
        params = self.__get_params()
        format = format_executer.execute_query(params)
        books = reading_executer.execute_query(params)
        body = {}
        
        if 'book' in params.keys():
            if format:
                body['format'] = params['format']
            else:
                body['format'] = 'html'
            self.send_response(200) 
            self.send_header('Content-Type', body['format']) 
            self.end_headers() 
            body = self.__build_body(books, body)
            self.wfile.write(str(json.dumps(body)).encode())
        else: 
            self.send_response(404, "Not Found") 

    #check json files and build json if requested params are available
    def __build_body(self, books: list, body : dict):
        body['books'] = []
        for book in books:
            body['books'].append(book)
        return body
    
    #splith path and turn it into a dictionary
    def __get_params(self) -> dict:
        return dict(parse_qsl(self.path[1:]))
    