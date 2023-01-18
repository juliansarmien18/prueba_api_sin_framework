from http.server import HTTPServer, BaseHTTPRequestHandler 
import json 

with open("prueba.json") as data_file:
	data = json.load(data_file)
 
class APIHandler(BaseHTTPRequestHandler): 

    def do_GET(self): 
        path_elements = self.path.split('/')
        del path_elements[0]
        
        if path_elements[0] == 'book':
            parameters = self.__build_dict_parameters(path_elements)
            self.send_response(200) 
            self.send_header('Content-Type', parameters['format']) 
            self.end_headers() 
            for book in data:
                if book['name'] == parameters['book']:
                    for page in book['pages']:
                        if str(page['page']) == parameters['page']:
                            self.wfile.write(page["content"].encode())
        else: 
            self.send_response(404) 

    def __build_dict_parameters(self, path_elements : list) -> dict:
        return {
            path_elements[0]: path_elements[1],
            path_elements[2]: path_elements[3],
            path_elements[4]: path_elements[5]
        }

httpd = HTTPServer(('localhost', 8000), APIHandler) 
httpd.serve_forever()