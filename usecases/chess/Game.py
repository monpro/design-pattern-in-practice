from usecases.chess.Board import Board
from usecases.chess.Const import GameStatus
from usecases.chess.Move import Move


class Game:
  def __init__(self):
    self.__players = []
    self.__board = Board()
    self.__current_turn = None
    self.__status = GameStatus.ACTIVE
    self.__moves_played = []

  def initialize(self, player1, player2):
    self.__players[0] = player1
    self.__players[1] = player2

    self.__board.reset_board()

    if player1.is_white_side():
      self.__current_turn = player1
    else:
      self.__current_turn = player2

    self.__moves_played.clear()

  def get_status(self):
    return self.__status

  def set_status(self, status):
    self.__status = status

  def player_move(self, player, start_x, start_y, end_x, end_y):
    start_box = self.__board.get_box(start_x, start_y)
    end_box = self.__board.get_box(end_x, end_y)

    move = Move(player, start_box, end_box)
    return self.make_move(move, player)

  def make_move(self, move, player):
    # todo: add make move logic
    pass