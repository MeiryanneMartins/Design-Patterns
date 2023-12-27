from .interfaces import Iskills


class Heal(Iskills):

    def __init__(self, level):
        self.level = level

    def behavior(self):
        print('Curar personagem')

    def attribute_level(self):
        print('Nivel de Cura: {}' .format(self.level))
