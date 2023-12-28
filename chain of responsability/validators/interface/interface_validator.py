from abc import ABC, abstractmethod


class InterfaceValidator(ABC):

    @abstractmethod
    def validate(self, animal: str) -> bool:
        pass

    @abstractmethod
    def action(self) -> None:
        pass
