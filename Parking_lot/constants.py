from enum import Enum

class ParkingSpotStatus(Enum):
    AVAILABLE = 1
    UNAVAILABLE = 2

class ParkingSpotSize(Enum):
    COMPACT = 1
    MEDIUM = 2
    LARGE = 3

class ParkingSpotType(Enum):
    HANDICAPPED = 1
    MOTORCYCLE = 2
    CAR = 3
    TRUCK = 4
    VAN = 5

class PaymentStatus(Enum):
    PAID = 1
    UNPAID = 2

class FeeStructure(Enum):
    FIRST_HOUR = 4
    SECOND_AND_THIRD_HOUR = 3.5
    FOURTH_HOUR_ONWARDS = 2.5
