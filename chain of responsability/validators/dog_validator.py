from .interface import InterfaceValidator


class DogValidator(InterfaceValidator):
    def validate(self, animal: str) -> bool:
        if animal == 'dog':
            return True
        return False

    def action(self) -> None:
        print('dogs cant talk')
