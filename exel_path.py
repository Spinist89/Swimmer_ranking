import openpyxl


class ExelWorker:

    def __init__(self, file_path):
        self.wb = openpyxl.load_workbook(file_path)
        self.ws = self.wb.active

    def get_data(self):
        return list(self.ws.values)