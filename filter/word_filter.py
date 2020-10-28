import re

from filter.main import Filter, FilterChain


class WordFilter(Filter):

  def __init__(self):
    self.filter_words = ['green', 'blue']

  def doFilter(self, elements):
    regex = ''
    for word in self.filter_words:
      regex += word + '|'

    regex = regex[0: len(regex) - 1]

    new_elements = []
    for element in elements:
      item, _ = re.subn(regex, '', element)
      new_elements.append(item)

    return new_elements


class HtmlFilter(Filter):

  def __init__(self):
    self.word_map = {
      ">": "&gt;",
      "<": "&lt;",
      "&": "&amp;",
      "\"": "&quot;"
    }

  def doFilter(self, elements):
    new_elements = []
    for element in elements:
      for key, value in self.word_map.items():
        element = element.replace(key, value)
      new_elements.append(element)
    return new_elements


if __name__ == "__main__":
  contents = ["blue < white", "green > red &"]
  filterChain = FilterChain()
  filterChain.addFilter(WordFilter())
  filterChain.addFilter(HtmlFilter())

  newContents = filterChain.doFilter(contents)
  print(newContents)
