from .interface import InterfaceValidator


class PersonValidator(InterfaceValidator):
    def validate(self, animal: str) -> bool:
        if animal == 'person':
            return True
        return False

    def action(self) -> None:
        print('Hi, im a person')
