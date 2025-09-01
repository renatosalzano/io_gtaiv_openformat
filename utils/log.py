from time import time

class StopWatch:
  
  def __init__(self):
    self.total_time = 0.0
    self.start = time()

  def time(self, message):
    self.total_time += time() - self.start
    print(f'{message} in {time() - self.start} s')
    self.start = time()

  def stop(self):
    print(f'DONE in {self.total_time} s')