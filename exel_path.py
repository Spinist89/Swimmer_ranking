from pprint import pprint

import openpyxl
from loguru import logger


class ExelWorker:

    def __init__(self, file_path):
        self.wb = openpyxl.load_workbook(file_path)
        self.ws = self.wb.active

    def get_data(self):
        return self.sorting(list(self.ws.values))

    def sorting(self, data: list) -> list: #Ранжирование по году рождения
        for i in range(len(data)):
            for k, i in enumerate(data):
                try:
                    year_birth = self.get_year_birth(i)
                    previous_iter = data[k - 1]
                    previous_year_birth = self.get_year_birth(previous_iter)
                    if year_birth < previous_year_birth:
                        data.insert(0, i)
                        del data[k+1]
                except Exception:
                    pass


        new_years = [] #ранжирование по полу
        for i in range(len(data)):
            for k, i in enumerate(data):
                year_birth = self.get_year_birth(i)
                previous_iter = data[k - 1]
                previous_year_birth = self.get_year_birth(previous_iter)
                if year_birth == previous_year_birth:
                    if self.get_gender(i) == 'д':
                        data.insert(new_years[len(new_years)-1], i)
                        del data[k+1]
                else:
                    new_years.append(k)
        return data

    @staticmethod
    def get_gender(i: tuple) -> str:
        return i[2]

    @staticmethod
    def get_year_birth(i: tuple) -> int:
        try:
            return int(i[3].replace('г.', ''))
        except IndexError:
            pass
