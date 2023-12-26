from src.item import Item


class MixinLanguage:

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'

    @property
    def language(self):
        return self.__language


class Keyboard(MixinLanguage, Item):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
