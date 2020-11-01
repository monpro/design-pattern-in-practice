from enum import Enum


class ConnectionInvitationStatus(Enum):
  PENDING = 1,
  ACCEPTED = 2,
  CONFIRMED = 3,
  REJECTED = 4,
  CANCELED = 5


class AccountStatus(Enum):
  ACTIVE = 1,
  BLOCKED = 2,
  BANNED = 3,
  COMPROMISED = 4,
  UNKNOWN = 5


class Address:
  def __init__(self, street, city, state, zip_code, country):
    self.street = street
    self.city = city
    self.state = state
    self.zip_code = zip_code
    self.country = country
    