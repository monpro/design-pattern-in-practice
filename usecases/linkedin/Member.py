import datetime

from usecases.linkedin.Person import Person
from usecases.linkedin.Profile import Profile


class Member(Person):
  def __init__(self):
    self.__date_of_membership = datetime.date.today()
    self.__headline = ""
    self.__phone = []
    self.__member_suggestions = []
    self.__member_follows = []
    self.__member_connections = []
    self.__company_follows = []
    self.__group_follows = []
    self.__profile = Profile()

  def send_message(self, message):
    pass

  def create_post(self, post):
    pass

  def send_connection_invitation(self, connection_invitation):
    pass