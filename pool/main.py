from abc import ABCMeta, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)


class PooledObject:

  def __init__(self, obj):
    self.obj = obj
    self.busy = False

  def getObject(self):
    return self.obj

  def setObject(self, obj):
    self.obj = obj

  def isBusy(self):
    return self.busy

  def setBusy(self, busy):
    self.busy = busy


class ObjectPool(metaclass=ABCMeta):

  def __init__(self):
    self.num_of_objects = 10
    self.max_num_of_objects = 50
    self.pools = []

    for i in range(self.num_of_objects):
      obj = self.createPooledObject()
      self.pools.append(obj)

  @abstractmethod
  def createPooledObject(self):
    pass

  def findFreeObject(self):
    result = None
    for obj in self.pools:
      if not obj.isBusy():
        result = obj.getObject()
        obj.setBusy(True)
        break
    return result

  def clear(self):
    self.pools.clear()

  def borrowObject(self):
    pass

  def returnObject(self):
    pass