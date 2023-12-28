import csv

from src.csv_err import InstantiateCSVError, CSVCheckScript


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__name, self.price, self.quantity}"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError
        return self.quantity + other.quantity

    # "Item('Смартфон', 10000, 20)"

    @property
    def item_name(self):
        return self.__name

    @item_name.setter
    def item_name(self, data):
        self.__name = data[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path):
        cls.all.clear()
        try:
            csvfile = CSVCheckScript(path)
        except InstantiateCSVError as ms:
            print(ms.message)
            raise InstantiateCSVError
        else:
            with open(path, newline='', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    __name = row['name']
                    price = row['price']
                    quantity = row['quantity']
                    item = cls(__name, price, quantity)

    @staticmethod
    def string_to_number(string):
        number = string.split('.')
        return int(number[0])
