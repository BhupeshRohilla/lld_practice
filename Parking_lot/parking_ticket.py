from abc import abstractmethod, ABC
from datetime import datetime
from constants import PaymentStatus

class IParkingTicket(ABC):
    @abstractmethod
    def __init__(self, id) -> None:
        self.id = id
        self._entry_time = datetime.now()
        self._exit_time = None
        self._payment_status = PaymentStatus.UNPAID

    @abstractmethod
    def update_exit_time(self):
        pass

    @abstractmethod
    def update_payment_status(self, payment_status: PaymentStatus):
        pass

class ParkingTicket(IParkingTicket):
    def __init__(self, id) -> None:
        raise NotImplementedError
        super().__init__(id)