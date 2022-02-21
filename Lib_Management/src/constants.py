from abc import ABC, abstractmethod
from enum import Enum

class BookFormat(Enum):
    HARDCOVER = 1
    PAPERBACK = 2
    AUDIO_BOOK = 3
    EBOOK = 4
    NEWSPAPER = 5
    MAGAZINE = 6
    JOURNAL = 7

class BookStatus(Enum):
    AVAILABLE = 1
    RESERVED = 2
    LOANED = 3
    LOST = 4

class ReservationStatus(Enum):
    WAITING = 1
    PENDING = 2
    CANCELED = 3
    COMPLETED = 4

class AccountStatus(Enum):
    ACTIVE = 1
    CLOSED = 2
    CANCELED = 3
    BLACKLISTED = 4
    NONE = 5

class IAddress(ABC):
    def __init__(self, line_1: str, line_2: str, city: str, state: str, pincode: int) -> None:
        self.__line_1 = line_1
        self.__line_2 = line_2
        self.__city = city
        self.__state = state
        self.__pincode = pincode
    
    @abstractmethod
    def get_address(self) -> str: pass

class IPerson(ABC):
    def __init__(self, name: str, address: IAddress, email: str, phone: str) -> None:
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone

class Constants:
    def __init__(self) -> None:
        self.MAX_BOOKS_ISSUES_TO_A_MEMBER = 5
        self.MAX_LENDING_DAYS = 10

class IBook(ABC):
    def __init__(self, ISBN, title, authors, subject, publisher, language) -> None:
        self.__ISBN = ISBN
        self.__title = title
        self.__authors = authors
        self.__subject = subject
        self.__publisher = publisher
        self.__language = language
