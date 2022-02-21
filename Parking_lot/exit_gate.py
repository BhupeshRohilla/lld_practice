from abc import ABC, abstractmethod

class IExitGate(ABC):
    @abstractmethod
    def __init__(self, gate_no) -> None:
        self._gate_no = gate_no

    @abstractmethod
    def is_payment_done(self, parking_ticket_id) -> bool:
        pass

    @abstractmethod
    def process_payment(self, parking_ticket_id, payment_mode) -> bool:
        pass

    @abstractmethod
    def open_gate(self) -> None: pass

class ExitGate(IExitGate):
    def __init__(self, gate_no) -> None:
        raise NotImplementedError