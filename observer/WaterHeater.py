from abc import ABCMeta, abstractmethod
'''
WaterHeater is the Observable
WashingMode and DrinkingMode is the Observer
Observable -> notifies -> Observer.update
this is exactly how publisher and subscriber works
'''


class WaterHeater:

  def __init__(self):
    self.__observers = []
    self.__temperature = 25

  def getTemperature(self):
    return self.__temperature

  def setTemperature(self, temperature):
    self.__temperature = temperature
    print(f'current temperature is {temperature}')
    self.notifies()

  def addObserver(self, observer):
    self.__observers.append(observer)

  def notifies(self):
    for observer in self.__observers:
      observer.update(self)


class Observer(metaclass=ABCMeta):

  @abstractmethod
  def update(self, waterHeater):
    pass


class WashingMode(Observer):

  def update(self, waterHeater):
    if 50 <= waterHeater.getTemperature() < 70:
      print("you could start to have shower now")


class DrinkingMode(Observer):

  def update(self, waterHeater):
    if waterHeater.getTemperature() >= 100:
      print('you could start to drink tea now')


def testHeater():
  heater = WaterHeater()
  waterObserver = WashingMode()
  drinkingObserver = DrinkingMode()
  heater.addObserver(waterObserver)
  heater.addObserver(drinkingObserver)
  heater.setTemperature(40)
  heater.setTemperature(60)
  heater.setTemperature(90)
  heater.setTemperature(100)


if __name__ == "__main__":
  testHeater()
