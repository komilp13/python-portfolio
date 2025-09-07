'''
There are two ways to share data between processes:
   1) Value for single value
   2) Array for multiple values
'''


# for single value sharing
from multiprocessing import Process, Value, Array, Lock
import time

def add_100(n, lock):
  for i in range(100):
    time.sleep(0.01)
    with lock:
      n.value += i

if __name__ == '__main__':
  lock = Lock()
  shared_num = Value('i', 0)
  print('Number at beginning: ', shared_num.value)

  p1 = Process(target=add_100, args=(shared_num, lock))
  p2 = Process(target=add_100, args=(shared_num, lock))

  p1.start()
  p2.start()

  p1.join()
  p2.join()

  print('Number at end: ', shared_num.value)




# for multiple value sharing

def add_100_arr(nums, lock):
  for i in range(100):
    time.sleep(0.01)
    for i in range(len(nums)):
      with lock:
        nums[i] += 1

if __name__ == '__main__':
  lock = Lock()
  shared_arr = Array('d', [0.0, 100.0, 200,0])

  print('Array at beginning: ', shared_arr[:])

  p3 = Process(target=add_100_arr, args=(shared_arr, lock))
  p4 = Process(target=add_100_arr, args=(shared_arr, lock))

  p3.start()
  p4.start()

  p3.join()
  p4.join()

  print('Array at end: ', shared_arr[:])

