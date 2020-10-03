class numCallsDecorator:

  def __init__(self, func):
    self.__numOfCall = 0
    self.__func = func

  def __call__(self, *args, **kwargs):
    '''
    must implement __call__ to make a class decorator
    :param args:
    :param kwargs:
    :return:
    '''
    self.__numOfCall += 1
    obj = self.__func(*args, **kwargs)
    print(f"{self.__func.__name__, self.__numOfCall, id(obj)}")
    return obj

@numCallsDecorator
class testClass:

  def __init__(self, name):
    self.__name = name

  def getName(self):
    return self.__name


if __name__ == "__main__":
  test1 = testClass("test1")
  test2 = testClass("test2")
  test3 = testClass("test3")