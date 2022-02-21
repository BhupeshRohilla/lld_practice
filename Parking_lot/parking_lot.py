from abc import ABC, abstractmethod
from floor import Floor
from entry_gate import EntryGate
from exit_gate import ExitGate

class IParkingLot(ABC):
    @abstractmethod
    def add_entry_gate(self, entry_no) -> EntryGate: pass

    @abstractmethod
    def add_exit_gate(self, exit_no) -> ExitGate: pass

    @abstractmethod
    def add_floor(self, floor_no) -> Floor: pass
