'''
Multi-threading using queues

Queues are thread-safe & process-safe data exchanges & data processing in multi-threaded or multi-processing env.
Important queue functions:
  q.put(1)  -> adds an item to queue
  q.get()  -> gets & removes item from queue
  q.task_done()  -> flags the current item as processed
  q.join()  -> blocks the current thread until all items are processed
'''
from threading import Thread, Lock, current_thread
from queue import Queue
import time

def worker(q, lock):
  while True:
    val = q.get()

    # processing...
    with lock:
      time.sleep(0.01)
      print(f'in {current_thread().name} got {val}.')
    q.task_done()

if __name__ == '__main__':
  q = Queue()
  lock = Lock()

  threads = 10

  for i in range(threads):
    t = Thread(target=worker, args=(q,lock))
    # we should use a daemon thread when using infinite loops. This ensures that when the main
    #   thread is exited, all child threads are exited as well and program exists.  Otherwise,
    #   the program doesn't exit and
    t.daemon = True
    t.start()

for i in range(1, 21):
  q.put(i)

q.join()

print('end program')