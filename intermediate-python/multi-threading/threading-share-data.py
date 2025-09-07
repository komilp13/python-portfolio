'''
Dealing with race condition when working with multiple threads.
'''

from threading import Thread, Lock
import time

db_value = 0

# without utilizing lock encounters race condition
def increment_old():
    global db_value
    local_copy = db_value

    # processing
    local_copy += 1
    time.sleep(0.1)
    db_value = local_copy

# using lock eliminates lock condition
def increment(lock):
  global db_value

  with lock:     # the with is similar to lock.acquire()
    local_copy = db_value

    # processing
    local_copy += 1
    time.sleep(0.1)
    db_value = local_copy
  # lock.release() - you don't need to explicitly release the lock using with


if __name__ == '__main__':

  # The Lock object is used to lock the variable from being accessed by
  #   multiple threads
  lock = Lock()

  print('start db value:', db_value)

  thread1 = Thread(target=increment, args=(lock,))
  thread2 = Thread(target=increment, args=(lock,))

  thread1.start()
  thread2.start()

  thread1.join()
  thread2.join()

  print('end db value:', db_value)
  print('end program')