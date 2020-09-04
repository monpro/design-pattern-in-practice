from abc import abstractmethod, ABCMeta


class Context(metaclass=ABCMeta):

  def __init__(self):
    self.__state = []
    self.__curState = None
    self.__stateInfo = 0

  def addState(self, state):
    if state not in self.__state:
      self.__state.append(state)

  def changeState(self, state):
    if state is None:
      return False
    if self.__curState is None:
      print(f"init to {state.getName()}")
    else:
      print(f"state change from {self.__curState.getName()} to {state.getName()}")
    self.__curState = state
    self.addState(state)
    return True

  def getState(self):
    return self.__curState

  def setStateInfo(self, stateInfo):
    # iterate the state array, use the state i impl method to judge
    # whether match or not.
    # if match simply change the state to state i.
    self.__stateInfo = stateInfo
    for state in self.__state:
      if state.isMatch(stateInfo):
        self.changeState(state)

  def getStateInfo(self):
    return self.__stateInfo


class State:

  def __init__(self, name):
    self.__name = name

  def getName(self):
    return self.__name

  def isMatch(self, stateInfo):
    return False

  @abstractmethod
  def behavior(self, context):
    pass