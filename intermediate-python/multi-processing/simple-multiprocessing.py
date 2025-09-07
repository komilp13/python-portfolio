from asyncio import threads
from multiprocessing import Process
import os

def square():
  for i in range(100):
    i * i


if __name__ == '__main__':
  processes = []
  processes_num = os.cpu_count()    # use number of CPUs on machine

  # create proceses and assign a function for each process
  for i in range(processes_num):
    p = Process(target=square)
    processes.append(p)

  # start all processes
  for p in processes:
    p.start()

  # wait for all processes to finish
  # block the main process until other processes finish
  for p in processes:
    p.join()


