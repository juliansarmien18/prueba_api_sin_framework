import json 


class DataOpener:
    
    #Open a file an save its information into a json
    def open_data(self, file_name : str) -> dict:
        with open(file_name) as data_file:
            data = json.load(data_file)
        data_file.close()
        return data