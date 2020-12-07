#! env python3
import fileinput, sys

sum = 0
curr_set = set()
for line in [x.strip() for x in fileinput.input()]:
  if len(line) == 0:
    sum = sum + len(curr_set)
    curr_set = set()
    continue
  curr_set.update(set(line[:]))

sum = sum + len(curr_set)
  
print(sum)
