import time
from observer.main import *


class Account(Observable):

  def __init__(self):
    super().__init__()
    self.__latestIp = {}
    self.__latestRegion = {}

  def login(self, name, ip, loginTime):
    region = self.getRegion(ip)
    if self.isLongDistance(name, region):
      self.notifyObservers({
        "name": name,
        "ip": ip,
        "region": region,
        "time": loginTime
      })
    self.__latestRegion[name] = region
    self.__latestRegion[name] = ip

  @staticmethod
  def getRegion(ip):
    # hard code ip to region just for example
    ipRegions = {
      "101.47.0.0": "China",
      "67.128.0.0": "USA"
    }
    region = ipRegions.get(ip)
    return "" if region is None else region

  def isLongDistance(self, name, region):
    # simply use region exactly match to stimulate long distance
    latestRegion = self.__latestRegion.get(name)
    return latestRegion is not None and latestRegion != region


class SmsSender(Observer):

  def update(self, observable, data):
    print('[sms]', data)


class MailSender(Observer):

  def update(self, observable, data):
    print('[mail', data)


def testLogin():
  account = Account()
  # use the framework to add observers
  account.addObserver(SmsSender())
  account.addObserver(MailSender())
  account.login("mike", "101.47.0.0", time.time())
  account.login("mike", "67.128.0.0", time.time())


if __name__ == "__main__":
  testLogin()
