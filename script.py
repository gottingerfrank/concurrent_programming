#!/usr/bin/env python3


import time
import threading
import asyncio
from multiprocessing import Process


def cal_average(num):  # Average function used for sequential programming, threading, and multiprocessing
  sum_num = 0
  for t in num:
    sum_num = sum_num + t
  avg = sum_num / len(num)
  time.sleep(1)
  return avg

def main_sequential(list1, list2, list3):  # Main wrapper for sequential example
  s = time.perf_counter()
  # your code goes here
  # calculate avg of 3 lists sequentially
  cal_average(list1)
  cal_average(list2)
  cal_average(list3)
  # check perf time
  elapsed = time.perf_counter() - s
  print("Sequential Programming Elapsed Time: " + str(elapsed) + " seconds")

async def cal_average_async(num):  # Average function used for asynchronous programming only ( needs await asyncio.sleep() )
  sum_num = 0
  for t in num:
    sum_num = sum_num + t
  avg = sum_num / len(num)
  await asyncio.sleep(1)
  return avg

async def main_async(list1, list2, list3):  # Main wrapper for asynchronous example
  s = time.perf_counter()
  # your code goes here
  # create tuple/list of async-func calls
  tasks = [cal_average_async(list1), cal_average_async(list2), cal_average_async(list3)]

  # run the async func-calls together
  await asyncio.gather(*tasks)

  elapsed = time.perf_counter() - s
  print("Asynchronous Programming Elapsed Time: " + str(elapsed) + " seconds")

def main_threading(list1, list2, list3):  # Main wrapper for threading example
  s = time.perf_counter()
  # your code goes here
  # create args (lists) + threads lists
  lists = [list1, list2, list3]
  threads = []

  # iterate thru args(=lists) and instantiate new Thread x for each, append to threads list, and start each Thread x
  for i in range(len(lists)):
    x = threading.Thread(target=cal_average, args=(lists[i],))
    threads.append(x)
    x.start()

  # join each thread
  for thread in threads:
    thread.join()

  elapsed = time.perf_counter() - s
  print("Threading Elapsed Time: " + str(elapsed) + " seconds")

def main_multiprocessing(list1, list2, list3):  # Main wrapper for multiprocessing example
  s = time.perf_counter()
  # your code goes here
  # create lists + processes lists
  lists = [list1, list2, list3]
  processes = []
  # create Process for each list
  for l in lists:
    p = Process(target=cal_average, args=(l,))
    processes.append(p)

  # start each process
  for p in processes:
    p.start()
  # join each process
  for p in processes:
    p.join()

  elapsed = time.perf_counter() - s
  print("Multiprocessing Elapsed Time: " + str(elapsed) + " seconds")


if __name__ == '__main__':  # Need to use this if-statement so multiprocessing doesn't cause an infinite loop
  l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Three lists we are trying to calculate average on
  l2 = [2, 4, 6, 8, 10]
  l3 = [1, 3, 5, 7, 9, 11]
  main_sequential(l1, l2, l3)
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main_async(l1, l2, l3))
  main_threading(l1, l2, l3)
  main_multiprocessing(l1, l2, l3)