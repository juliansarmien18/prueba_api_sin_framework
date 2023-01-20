from http.server import BaseHTTPRequestHandler
from data_opener import DataOpener 
from query_executers.format_executer import FormatExecuter
from urllib.parse import  parse_qsl

import json


class BookHandler(BaseHTTPRequestHandler): 
    
    """Open Json Files, searchs for requested params, uses the reuqested format
        and returns a json with data if exists"""
    def do_GET(self):
        data_opener = DataOpener()
        format_executer = FormatExecuter()
        formats = format_executer.execute_query()
        params = self.__get_params()
        books = data_opener.open_data("books.json")
        body = {}
        
        if 'book' in params.keys() and self.__check_format(formats, params['format']):
            body['format'] = params['format']
            
            self.send_response(200) 
            self.send_header('Content-Type', "text") 
            self.end_headers() 
            body = self.__build_body(books, params, body)
            self.wfile.write(str(json.dumps(body)).encode())
        else: 
            self.send_response(404) 
            
    #Check if requested format exists on database
    def __check_format(self, formats : list, selected_format : str):
        for format in formats:
            if selected_format == format['format']:
                return True
        return False

    #check json files and build json if requested params are available
    def __build_body(self, books : dict, params: dict, body : dict):
        for book in books:
                if book['id'] == int(params['book']) and self.__check_page(book['pages'], int(params['page'])):
                    body['book'] = book['name']
                    
                    for page in book['pages']:
                        if str(page['page']) == params['page']:
                            body['page'] = page["content"]
                            return body
                else:
                    self.send_response(404)
    
    #check if requested page exists in requested Book
    def __check_page(self, pages : list, page : int) -> bool:
        return page <= len(pages)
    
    #splith path and turn it into a dictionary
    def __get_params(self) -> dict:
        return dict(parse_qsl(self.path[1:]))
    