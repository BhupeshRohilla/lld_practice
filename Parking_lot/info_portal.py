from abc import ABC, abstractmethod


class IInfoPortal(ABC):
    @abstractmethod
    def process_payment(self, parking_ticket_id, payment_mode) -> bool:
        pass

    @abstractmethod
    def update_display(self, message):
        pass

class InfoPortal:
    def __init__(self) -> None:
        raise NotImplementedError