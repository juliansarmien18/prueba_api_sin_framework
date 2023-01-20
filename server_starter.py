from http.server import HTTPServer
from book_handler import BookHandler


class ServerStarter:
    
    #Initialize its instance starting the server
    def __init__(self) -> None:
        self.server = self.__start_server()
    
    #Start server on localhost port 8000
    def __start_server(self): 
        httpd = HTTPServer(('localhost', 8000), BookHandler) 
        httpd.serve_forever()