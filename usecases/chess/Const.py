from enum import Enum


class GameStatus(Enum):
  ACTIVE = 0,
  BLACK_WIN = 1,
  WHITE_WIN = 2,
  FORFEIT = 3,
  STALEMATE = 4,
  RESIGNATION = 5


class AccountStatus(Enum):
  ACTIVE = 0,
  CLOSED = 1,
  CANCELED = 2,
  BLACKLISTED = 3,
  NONE = 4