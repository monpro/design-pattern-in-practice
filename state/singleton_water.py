from state.main import *

class Water(Context):

  def __init__(self):
    super().__init__()
    self.addState(SolidState('solid'))
    self.addState(LiquidState('liquid'))
    self.addState(GaseousState('gaseous'))
    self.setTemperature(25)

  def getTemperature(self):
    return self.getStateInfo()

  def setTemperature(self, temperature):
    self.setStateInfo(temperature)

  def riseTemperature(self, step):
    self.setTemperature(self.getTemperature() + step)

  def reduceTemperature(self, step):
    self.setTemperature(self.getTemperature() - step)

  def behavior(self):
    state = self.getState()
    if isinstance(state, State):
      state.behavior(self)


def singleton(cls, *args, **kwargs):
  instance = {}

  def __singleton(*args, **kwargs):
    if cls not in instance:
      instance[cls] = cls(*args, **kwargs)
    return instance[cls]
  return __singleton


@singleton
class SolidState(State):

  def __init__(self, name):
    super().__init__(name)

  def isMatch(self, stateInfo):
    return stateInfo <= 0

  def behavior(self, context):
    print(f"solid with {context.getStateInfo()}")


@singleton
class LiquidState(State):

  def __init__(self, name):
    super().__init__(name)

  def isMatch(self, stateInfo):
    return 0 <= stateInfo <= 100

  def behavior(self, context):
    print(f"liquid with {context.getStateInfo()}")


@singleton
class GaseousState(State):

  def __init__(self, name):
    super().__init__(name)

  def isMatch(self, stateInfo):
    return stateInfo > 100

  def behavior(self, context):
    print(f"gaseous with {context.getStateInfo()}")


def testState():
  water = Water()
  water.behavior()
  water.setTemperature(-10)
  water.behavior()
  water.riseTemperature(20)
  water.behavior()
  water.riseTemperature(110)
  water.behavior()


if __name__ == "__main__":
  testState()
