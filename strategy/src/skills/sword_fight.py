from .interfaces import Iskills


class FightSword(Iskills):

    def __init__(self, level):
        self.level = level

    def behavior(self):
        print('Lutar com espada')

    def attribute_level(self):
        print('Nivel de uso Espada: {}' .format(self.level))
