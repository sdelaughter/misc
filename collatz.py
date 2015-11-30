"""Last Updated 11/30/15
Author: Samuel DeLaughter

Tests a number or range of numbers for consistency with the Collatz conjecture

Run with no arguments to test numbers 1 - 100
Run with a single integer argument to test it
Run with two integer arguments (MIN, MAX) to test a range of numbers

"""

import sys

#Process command-line arguments
try:
  if(len(sys.argv) == 3):
    MIN = int(sys.argv[1])
    if MIN < 1:
      MIN = 1
      MAX = int(sys.argv[2])
    if MAX < MIN:
      MAX = MIN + 1
  elif(len(sys.argv) == 2):
    MIN = int(sys.argv[1])
    MAX = int(sys.argv[1])
  else:
    MIN = 1
    MAX = 100
except:
  print('Invalid command-line arguments.  Supply one integer argument to test a single number, or two integers to test a range of numbers')
  sys.exit()
  
def test(number):
  n = number
  counter = 0
  while(not (n == 1)):
    if((n % 2) == 0):
      n = (n / 2)
    else:
      n = ((n * 3) + 1)
      counter += 1
      print ('Reached 1 from ' + str(number) + ' in ' + str(counter) +  ' steps')

def main():
  number = MIN
  while number <= MAX:
    test(number)
    number += 1
    print('Done')

if __name__ == '__main__':
  main()
