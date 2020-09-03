from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):


  @abstractmethod
  def update(self, observable, data):
    pass


class Observable:

  def __init__(self):
    self.__observers = []

  def addObserver(self, observer):
    self.__observers.append(observer)

  def removeObserver(self, observer):
    self.__observers.remove(observer)

  def notifyObservers(self, data=None):
    for o in self.__observers:
      o.update(self, data)
