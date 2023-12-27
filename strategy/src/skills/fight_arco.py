from .interfaces import Iskills


class FightArco(Iskills):

    def __init__(self, level):
        self.level = level

    def behavior(self):
        print("Atirar flexas")

    def attribute_level(self):
        print('Nivel de uso Arco: {}' .format(self.level))
