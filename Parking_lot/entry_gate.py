from abc import ABC, abstractmethod
from parking_ticket import ParkingTicket

class IEntryGate(ABC):
    @abstractmethod
    def __init__(self, gate_no) -> None:
        self._gate_no = gate_no

    @abstractmethod
    def get_parking_ticket(self) -> ParkingTicket:
        pass

    @abstractmethod
    def post_providing_ticket(self) -> None:
        self.open_gate()

    @abstractmethod
    def open_gate(self) -> None: pass

    @abstractmethod
    def display_message(self, msg) -> None: pass

class EntryGate(IEntryGate):
    def __init__(self, gate_no) -> None:
        raise NotImplementedError