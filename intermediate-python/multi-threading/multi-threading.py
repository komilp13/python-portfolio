'''
Multiprocessing

Process vs Thread
  Process: an instance of a program - can have multiple threads
     + Takes advantage of multiple CPUs and cores
     + Separate memory space -> memory is not shared between processes
     + Great for CPU-bound processing
     + New process is started independently of other processes
     + Processes are interruptable/killable
     + One GIL for each process -> avoids GIL limitation (GIL is global interpreter)

     - Heavyweight
     - Starting a process is slower than starting a thread
     - Consumes more memory
     - IPC (inter-process communication) is more complicated


  Thread: An entity within a process that can be scheduled (aka lightweight process)
     + All threads within a process share the same memory
     + Lightweight
     + Starting a thread is faster compared to process
     + Great for I/O-bound tasks

     - Threading is limited to GIL: only one thread at a time
     - No effect for CPU-bound tasks
     - Not interruptable/killable
     - Careful with race conditions


  GIL: Global interpreter lock
     - a lock that allows only one thread at a time to execute
     - Needed in CPython because of memory mgmt is not thread-safe
     - Avoid:
        - using multiprocessing
        - using a different, free-threaded python implementation (Jython, IronPython)
        - using Python as a wrapper for 3rd party libraries (C/C++) -> numpy, scipy
'''
from threading import Thread
import os
import time

def square():
  for i in range(100):
    i * i
    time.sleep(0.1)

threads = []
num_threads = 10

for i in range(num_threads):
  t = Thread(target=square)
  threads.append(t)

# start
for t in threads:
  t.start()

# join threads: wait to complete & block main thread
for t in threads:
  t.join()

print('end main thread')




'''
 
'''