import random
from abc import ABC, abstractmethod

from LLD_Nokia_Snake_Game.src.Shell import Shell, ShellType

class IBoard(ABC):
    @abstractmethod
    def generate_food(self) -> None: pass

    # @property
    # @abstractmethod
    # def have_food(self) -> bool: pass

    # @abstractmethod
    # def food_consumed() -> None: pass

class Board(IBoard):
    def __init__(self, row_count: int, col_count: int) -> None:
        self.row_count = row_count
        self.col_count = col_count
        # self._have_food = False
        self.board = [ [ Shell(i, j) for j in range(col_count) ] for i in range(row_count) ]

    # @property
    # def have_food(self) -> bool:
    #     return self._have_food

    # def food_consumed(self) -> None:
    #     self._have_food = False
    
    def generate_food(self) -> None:
        while True:
            row = random.choice(range(self.row_count))
            col = random.choice(range(self.col_count))
            if self.board[row][col].shell_type == ShellType.EMPTY:
                self.board[row][col].shell_type = ShellType.FOOD
                # self._have_food = True
                break
