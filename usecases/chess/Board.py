import collections

from usecases.chess.Rook import Rook
from usecases.chess.Bishop import Bishop
from usecases.chess.Box import Box
from usecases.chess.Knight import Knight


class Board:
  def __init__(self):
    self.__boxes = collections.defaultdict(list)

  def Board(self):
    self.reset_board()

  def get_box(self, x, y):
    if x < 0 or x > len(self.__boxes) or y < 0 or y > len(self.__boxes[0]):
      raise Exception("Index out of bound")
    return self.__boxes[x][y]

  def reset_board(self):
    for i in range(7):
      self.__boxes[i] = [None for _ in range(3)]

    for i in range(7):
        self.__boxes[i][0] = Box(0, 0, Rook(True))
        self.__boxes[i][0] = Box(0, 0, Knight(True))
        self.__boxes[i][0] = Box(0, 0, Bishop(True))
    # TODO: add more logic
    