from abc import ABC, abstractmethod
from constants import ParkingSpotSize, ParkingSpotType, ParkingSpotStatus
from electric_panel import ElectricPanel

class IParkingSpot(ABC):
    @abstractmethod
    def __init__(self, id, type: ParkingSpotType, size: ParkingSpotSize) -> None:
        self._id = id
        self._type = type
        self._size = size
        self._status = ParkingSpotStatus.AVAILABLE

    @property
    @abstractmethod
    def status(self):
        return self._status
        
    @status.setter
    @abstractmethod
    def status(self, status: ParkingSpotStatus) -> None:
        self._status = status
    
class PertroliumParkingSpot(IParkingSpot):
    def __init__(self, id, type: ParkingSpotType, size: ParkingSpotSize) -> None:
        super().__init__(id, type, size)

    
class ElectricParkingSpot(IParkingSpot):
    def __init__(
        self,
        id,
        type: ParkingSpotType,
        size: ParkingSpotSize,
        electric_panel: ElectricPanel,
    ) -> None:
        super().__init__(id, type, size)
    
    def start_charging(self):
        raise NotImplementedError
    
    def stop_charging(self):
        raise NotImplementedError
