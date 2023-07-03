# your code goes here!
import time

def countdown(index):
  while index > 0:
    print(f'{index} SECOND(S)!')
    index -= 1
  print('HAPPY NEW YEAR!')

def countdown_with_sleep(index):
  while index > 0:
    print(f'{index} SECOND(S)!')
    time.sleep(1)
    index -= 1
  print('HAPPY NEW YEAR!')