import json 


class DataOpener:
    
    def open_data(self, file_name : str) -> dict:
        with open(file_name) as data_file:
            data = json.load(data_file)
        data_file.close()
        return data