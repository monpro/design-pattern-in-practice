from multiprocessing import Pool, Manager
import time
import requests


def main():
  link_list = []
  with open('alpha.txt', 'r') as file:
    file_list = file.readlines()
    for line in file_list:
      link = line.split('\t')[1].replace('\n', '')
      link_list.append(link)
  start = time.time()
  manager = Manager()
  work_queue = manager.Queue(1000)
  for url in link_list:
    work_queue.put(url)
  pool = Pool(processes=3)
  for i in range(4):
    # non blocking
    pool.apply_async(crawler, args=(work_queue, str(i)))
  print('started processes')
  pool.close()
  pool.join()
  end = time.time()
  print('total time', end - start)
  print('processes ended')


def crawler(queue, index):
  process_id = 'Process' + index
  while not queue.empty():
    url = queue.get(timeout=2)
    try:
      res = requests.get(url, timeout=20)
      print(process_id, queue.qsize(), res.status_code, url)
    except Exception as e:
      print(process_id, queue.qsize(), url, "Error: ", e)


if __name__ == "__main__":
  main()