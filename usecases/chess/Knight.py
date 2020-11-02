from usecases.chess.Piece import Piece


class Knight(Piece):
  def __init__(self, white):
    super().__init__(white)

  def can_move(self, board, start, end):
    if end.get_piece().is_white() == self.is_white():
      return False

    x = abs(start.get_x() - end.get_x())
    y = abs(start.get_y() - end.get_y())

    return x * y == 2