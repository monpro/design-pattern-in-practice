import math
import random
from threading import Thread


def merge_sort(start, end, sort_list, helper_list):
  if start == end:
    return

  mid = start + math.floor((end - start) / 2)

  '''
  single thread to do the sort
  
  # sort the left half
  merge_sort(start, mid, sort_list, helper_list)

  # sort the right half
  merge_sort(mid + 1, end, sort_list, helper_list)
  '''

  '''
  use two threads to sort the left and right half
  because they are sorting different data
  so no critical condition
  '''
  left_thread = Thread(target=merge_sort, args=(start, mid, sort_list, helper_list), name="left_thread")
  right_thread = Thread(target=merge_sort, args=(mid + 1, end, sort_list, helper_list), name="right_thread")

  left_thread.start()
  right_thread.start()
  left_thread.join()
  right_thread.join()

  # merge two sorted list
  for i in range(start, end + 1):
    # use helper list to preserve the origin sort_list
    helper_list[i] = sort_list[i]

  left = start
  right = mid + 1

  cur_index = start
  while cur_index <= end:
    if left <= mid and right <= end:
      sort_list[cur_index] = min(helper_list[left], helper_list[right])
      # use the helper list to know exact match
      if sort_list[cur_index] == helper_list[left]:
        left += 1
      else:
        right += 1

    elif left <= mid and right > end:
      sort_list[cur_index] = helper_list[left]
      left += 1

    else:
      sort_list[cur_index] = helper_list[right]
      right += 1

    cur_index += 1


def create_data(size):
  unsorted_list = [None] * size
  random.seed()

  for i in range(0, size):
    unsorted_list[i] = random.randint(0, 1000)

  return unsorted_list


if __name__ == "__main__":
  l = create_data(12)
  print(l)
  merge_sort(0, 11, l, [None for i in range(len(l))])
  print(l)
