import json 


class DataOpener:
    
    def open_data(self):
        with open("prueba.json") as data_file:
            data = json.load(data_file)
        return data