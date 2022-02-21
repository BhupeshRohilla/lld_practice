from abc import abstractmethod, ABC
import threading

from LLD_Nokia_Snake_Game.src.Board import Board
from LLD_Nokia_Snake_Game.src.Shell import Shell, ShellType
from LLD_Nokia_Snake_Game.src.Snake import Direction, Snake

class IGame(ABC):
    @abstractmethod
    def start(self) -> None: pass
    
    @abstractmethod
    def go_left(self) -> None: pass

    @abstractmethod
    def go_right(self) -> None: pass

    @abstractmethod
    def go_up(self) -> None: pass

    @abstractmethod
    def go_down(self) -> None: pass

    @abstractmethod
    def move_forward(self) -> None: pass

    @abstractmethod
    def game_over(self) -> None: pass


class Game(IGame):
    def __init__(self, row_count, col_count) -> None:
        self._board = Board(row_count, col_count)
        self._snake = Snake(self._board.board[0][0])
        self._is_game_over = False
        self.__timer = None
        self.start()
    
    def start(self) -> None:
        self.__timer = threading.Timer(1, self.move_forward)
        self.__timer.start()

    def move_forward(self) -> None:
        head_row = self._snake.head.row
        head_col = self._snake.head.column
        if self._snake.direction == Direction.RIGHT:
            head_col += 1
        elif self._snake.direction == Direction.LEFT:
            head_col -= 1
        elif self._snake.direction == Direction.UP:
            head_row -= 1
        elif self._snake.direction == Direction.DOWN:
            head_row += 1
        if self.within_boundary(head_row, head_col):
            food_generation = False
            next_shell = self._board.board[head_row][head_col]
            if next_shell.shell_type == ShellType.FOOD:
                food_generation = True
            self._snake.move(next_shell)
            if food_generation: self._board.generate_food()
        else:
            self.game_over()
        
    def within_boundary(self, row, col) -> bool:
        if 0 <= row < self._board.row_count \
            and 0 <= col < self._board.col_count:
            return True
        return False
    
    def game_over(self) -> None:
        self._is_game_over = True
        self.__timer.cancel()

'''
We can create other functions to control the directions of the snake.
'''