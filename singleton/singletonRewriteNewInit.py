class SingletonRe(object):
  __instance = None
  __isFirstInit = False

  def __new__(cls, *args, **kwargs):
    if not cls.__instance:
      SingletonRe.__instance = super().__new__(cls)
    return cls.__instance

  def __init__(self, name):
    if not self.__isFirstInit:
      self.__name = name
      SingletonRe.__isFirstInit = True

  def getName(self):
    return self.__name


if __name__ == "__main__":
  test = SingletonRe("test1")
  test2 = SingletonRe("test2")
  print(test.getName())
  print(test2.getName())