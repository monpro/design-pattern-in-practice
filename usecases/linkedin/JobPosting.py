import datetime


class JobPosting:
  def __init__(self, description, employment_type, location, is_fulfilled):
    self.__date_of_posting = datetime.date.today()
    self.__description = description
    self.__employment_type = employment_type
    self.__location = location
    self.__is_fulfilled = is_fulfilled