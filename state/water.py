from abc import abstractmethod, ABCMeta


class Water:

  def __init__(self, state):
    self.__temperature = 25
    self.__state = state

  def setState(self, state):
    self.__state = state

  def changeState(self, state):
    if self.__state:
      print(f"{self.__state.getName()} change to {state.getName()}")
    else:
      print(f"state is {state.getName()}")
    self.__state = state

  def getTemperature(self):
    return self.__temperature

  def setTemperature(self, temperature):
    if temperature <= 0:
      self.changeState(SolidState('solid'))
    elif temperature <= 100:
      self.changeState(LiquidState('liquid'))
    else:
      self.changeState(GaseousState('gaseous'))
    self.__temperature = temperature

  def riseTemperature(self, step):
    self.setTemperature(self.__temperature + step)

  def reduceTemperature(self, step):
    self.setTemperature(self.__temperature - step)

  def behavior(self):
    self.__state.behavior(self)


class State(metaclass=ABCMeta):

  def __init__(self, name):
    self.__name = name

  def getName(self):
    return self.__name

  @abstractmethod
  def behavior(self, water):
    pass


class SolidState(State):

  def __init__(self, name):
    super().__init__(name)

  def behavior(self, water):
    print(f"solid with {water.getTemperature()}")


class LiquidState(State):

  def __init__(self, name):
    super().__init__(name)

  def behavior(self, water):
    print(f"liquid with {water.getTemperature()}")


class GaseousState(State):

  def __init__(self, name):
    super().__init__(name)

  def behavior(self, water):
    print(f"gaseours with {water.getTemperature()}")


def testState():
  water = Water(LiquidState("liquid"))
  water.behavior()
  water.setTemperature(-10)
  water.behavior()
  water.riseTemperature(20)
  water.behavior()
  water.riseTemperature(110)
  water.behavior()


if __name__ == "__main__":
  testState()
