from collections import deque
from abc import ABC, abstractmethod
from enum import Enum

from LLD_Nokia_Snake_Game.src.Shell import Shell, ShellType

class Direction(Enum):
    LEFT = 1
    RIGHT = -1
    UP = 2
    DOWN = -2

class ISnake(ABC):
    @abstractmethod
    def move(self, new_shell: Shell) -> None: pass

    @abstractmethod
    def get_score(self) -> int: pass


class Snake(ISnake):
    def __init__(self, head: Shell) -> None:
        self.head = head
        self.head.shell_type = ShellType.SNAKE
        self.__snake = deque([head])
        self.direction = Direction.RIGHT

    def move(self, new_shell: Shell) -> None:
        if new_shell.shell_type != ShellType.FOOD:
            popped_shell = self.__snake.pop()
            popped_shell.shell_type = ShellType.EMPTY
        self.__snake.appendleft(new_shell)
        new_shell.shell_type = ShellType.SNAKE
        self.head = new_shell
        
    def get_score(self) -> int:
        return len(self.__snake)