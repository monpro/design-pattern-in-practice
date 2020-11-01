class Post:
  def __init__(self, text, owner):
    self.__text = text
    self.__total_likes = 0
    self.__total_shares = 0
    self.__owner = owner
