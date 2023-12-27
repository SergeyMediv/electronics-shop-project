import csv


class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Unknown Error'

    def __str__(self):
        return self.message


class BrokenCSV(InstantiateCSVError):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'InstantiateCSVError: Файл item.csv поврежден'


class NotFoundCSV(InstantiateCSVError):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else f"FileNotFoundError: Отсутствует файл 'items.csv'"


class CSVCheckScript:

    def __init__(self, path):
        try:
            csvfile = open(path)
        except FileNotFoundError:
            raise NotFoundCSV
        else:
            with open(path, newline='', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if not row['name'] and row['price'] and row['quantity']:
                        self.message = 'InstantiateCSVError: Файл item.csv поврежден'
            raise BrokenCSV
