from abc import ABCMeta, abstractmethod


class Filter(metaclass=ABCMeta):

  @abstractmethod
  def doFilter(self, elements):
    pass


class FilterChain(Filter):

  def __init__(self):
    self._filters = []

  def addFilter(self, _filter):
    self._filters.append(_filter)

  def removeFilter(self, _filter):
    self._filters.remove(_filter)

  def doFilter(self, elements):
    for _filter in self._filters:
      elements = _filter.doFilter(elements)
    return elements
