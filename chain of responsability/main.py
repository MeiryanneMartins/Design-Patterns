from validators import DogValidator, PersonValidator


class Validator:

    def __init__(self) -> None:
        self.val = [
            DogValidator(),
            PersonValidator()
        ]

    def process(self, animal: str):
        for v in self.val:
            if v.validate(animal):
                return v.action()


validation = Validator()
validation.process('person')
