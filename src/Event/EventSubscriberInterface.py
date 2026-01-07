from abc import ABC, abstractmethod

class EventSubscriberInterface(ABC):
    @abstractmethod
    def update(self, event: str, data: any) -> None:
        pass