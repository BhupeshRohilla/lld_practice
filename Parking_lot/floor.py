from abc import ABC, abstractmethod

from info_portal import InfoPortal

class IFloor(ABC):
    @abstractmethod
    def __init__(self, floor_no, info_portal: InfoPortal) -> None:
        self._floor_no = floor_no
        self._info_portal = info_portal

    @abstractmethod
    def add_parking_spot(self, spot_id, type, size):
        pass

    @abstractmethod
    def update_parking_spot_status(self, spot_id):
        pass

    @abstractmethod
    def update_info_portal(self):
        pass

class Floor(IFloor):
    def __init__(self, floor_no, info_portal: InfoPortal) -> None:
        raise NotImplementedError
        super().__init__(floor_no, info_portal)