from typing import Type
from .skills import Iskills


class Warrior:

    def __init__(self, skills: Type[Iskills]):
        self.skills = skills

    def action(self):
        # process
        self.skills.behavior()

    def attributes(self):
        self.skills.attribute_level()
