from http.server import BaseHTTPRequestHandler 
from data_opener import DataOpener
from urllib.parse import  parse_qs, parse_qsl


class BookHandler(BaseHTTPRequestHandler): 
    
    def do_GET(self): 
        data = DataOpener().open_data()
        params = self.__get_params()
        
        if 'book' in params.keys():
            self.send_response(200) 
            self.send_header('Content-Type', params['format']) 
            self.end_headers() 
            self.__open_page(data, params)
        else: 
            self.send_response(404) 
            
    def __open_page(self, data : dict, params: dict):
        for book in data:
                if book['name'] == params['book']:
                    for page in book['pages']:
                        if str(page['page']) == params['page']:
                            self.wfile.write(page["content"].encode())
                else:
                    self.send_response(404)
    
    def __get_params(self):
        return dict(parse_qsl(self.path[1:]))
    