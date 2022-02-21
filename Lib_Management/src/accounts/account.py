from abc import ABC
from src.constants import *
from src.accounts.person import Person

class IAccount(ABC):
    def __init__(self, id, password, person: Person, status=AccountStatus.ACTIVE) -> None:
        self.__id = id
        self.__password = password
        self.__status = status
        self.__person = person

    def reset_password(self, password) -> bool:
        pass