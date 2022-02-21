from abc import ABC, abstractmethod


class IElectricPanel(ABC):
    @abstractmethod
    def __init__(self, id) -> None:
        self._id = id
        self.start_time = None
        self.end_time = None
        self._total_units_used = 0
    
    @abstractmethod
    def start_charging(self): pass

    @abstractmethod
    def stop_charging(self): pass

    @abstractmethod
    def pay_for_units_used(self): pass

class ElectricPanel(IElectricPanel):
    def __init__(self, id) -> None:
        raise NotImplementedError
        super().__init__(id)