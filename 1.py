#! env python3
import fileinput, sys

numbers = [int(x.strip()) for x in fileinput.input() if len(x) > 1 and x.strip().isnumeric()]

for i in numbers:
  for j in numbers:
    for k in numbers:
      combo = i+j+k
      if combo == 2020:
        print(i*j*k)

