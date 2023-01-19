from http.server import BaseHTTPRequestHandler 
from data_opener import DataOpener
from urllib.parse import  parse_qsl

import json


class BookHandler(BaseHTTPRequestHandler): 
    
    def do_GET(self):
        data_opener = DataOpener()
        books = data_opener.open_data("books.json")
        formats = data_opener.open_data("formats.json")
        params = self.__get_params()
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
    
    def __check_format(self, formats : list, selected_format : str):
        for format in formats:
            if selected_format == format['format']:
                return True
        return False

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
    
    def __check_page(self, pages : list, page : int) -> bool:
        return page <= len(pages)
    
    def __get_params(self) -> dict:
        return dict(parse_qsl(self.path[1:]))
    