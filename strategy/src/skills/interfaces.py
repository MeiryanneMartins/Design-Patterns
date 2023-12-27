from abc import ABC, abstractclassmethod


class Iskills(ABC):

    @abstractclassmethod
    def behavior(self):
        pass

    @abstractclassmethod
    def attribute_level(self):
        pass
