from abc import ABC, abstractmethod
from enum import Enum

class ShellType(Enum):
    EMPTY = 1
    SNAKE = 2
    FOOD = 3

class IShell(ABC):
    @property
    @abstractmethod
    def shell_type(self) -> ShellType: pass

    @property
    @abstractmethod
    def row(self) -> int: pass

    @property
    @abstractmethod
    def column(self) -> int: pass


class Shell(IShell):
    def __init__(self, row: int, column: int) -> None:
        self._row = row
        self._column = column
        self._shell_type = ShellType.EMPTY
    
    @property
    def shell_type(self) -> ShellType:
        return self._shell_type
    
    @shell_type.setter
    def shell_type(self, value: ShellType) -> None:
        self._shell_type = value

    @property
    def row(self) -> int:
        return self._row
    
    @property
    def column(self) -> int:
        return self._column

