from abc import ABC

from src.Event.EventSubscriberInterface import EventSubscriberInterface

class EventEmitterInterface(ABC):
    subscribers: set[EventSubscriberInterface] = set()

    def attach(self, subscriber: EventSubscriberInterface) -> None:
        self.subscribers.add(subscriber)

    def detach(self, subscriber: EventSubscriberInterface) -> None:
        self.subscribers.discard(subscriber)

    def notify(self, event: str, data: any) -> None:
        for subscriber in list(self.subscribers):
            subscriber.update(event, data)