from http.server import HTTPServer
from book_handler import BookHandler


class ServerStarter:
    def __init__(self) -> None:
        self.server = self.__start_server()
    
    def __start_server(self): 
        httpd = HTTPServer(('localhost', 8000), BookHandler) 
        httpd.serve_forever()