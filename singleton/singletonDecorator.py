def singletonDecorator(cls, *args, **kwargs):
  instance = {}

  def wrapperSingleton(*args, **kwargs):
    if cls not in instance:
      instance[cls] = cls(*args, **kwargs)
    return instance[cls]

  return wrapperSingleton


@singletonDecorator
class Singleton:
  def __init__(self, name):
    self.name = name

  def getName(self):
    return self.name


if __name__ == "__main__":
  test1 = Singleton("test1")
  test2 = Singleton("test2")
  print(test1.getName())
  print(test2.getName())