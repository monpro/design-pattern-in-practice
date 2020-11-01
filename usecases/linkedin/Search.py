from abc import ABC


class Search(ABC):
  def search_member(self, name):
    pass

  def search_company(self, name):
    pass

  def search_job(self, title):
    pass


class SearchIndex(Search):
  def __init__(self):
    self.__member_names = {}
    self.__company_names = {}
    self.__job_titles = {}

  def add_member(self, member):
    if member.name in self.__member_names:
      self.__member_names.get(member.name).add(member)
    else:
      self.__member_names[member.name] = member

  def add_company(self):
    pass

  def add_job_posting(self):
    pass

  def search_member(self, name):
    return self.__member_names.get(name)

  def search_company(self, name):
    return self.__company_names.get(name)

  def search_job(self, title):
    return self.__job_titles.get(title)