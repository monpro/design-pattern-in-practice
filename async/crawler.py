import time
import threading
import requests


def main():
  link_list = []
  with open('alpha.txt', 'r') as file:
    file_list = file.readlines()
    for line in file_list:
      link = line.split('\t')[1].replace('\n', '')
      link_list.append(link)
  start = time.time()

  link_range_list = [(1, 75), (76, 150), (151, 225), (226, 280)]
  thread_list = []
  for i in range(len(link_range_list)):
    thread = CrawlerThread('Thread {0}'.format(i + 1), link_range_list[i], link_list)
    thread.start()
    thread_list.append(thread)
  for thread in thread_list:
    thread.join()
  end = time.time()

  # for link in link_list:
  #   try:
  #     res = requests.get(link)
  #     print(res.status_code, link)
  #   except Exception as e:
  #     print('Error', e)
  # end = time.time()

  print('total time is {0}'.format(end - start))


class CrawlerThread(threading.Thread):
  def __init__(self, name, link_range, link_list):
    threading.Thread.__init__(self)
    self.name = name
    self.link_range = link_range
    self.link_list = link_list
    print(self.link_list)
    print(self.link_range)

  def run(self):
    print('starting ' + self.name)
    crawler(self.name, self.link_range, self.link_list)
    print('exiting ' + self.name)


def crawler(name, link_range, link_list):
  for i in range(link_range[0], link_range[1]):
    try:
      res = requests.get(link_list[i], timeout=20)
      print(name, res.status_code, link_list[i])
    except Exception as e:
      print(name, 'Error: ', e)


if __name__ == "__main__":
  main()