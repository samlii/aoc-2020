#! env python3
import fileinput, sys

sum = 0
curr_set = None
for line in [x.strip() for x in fileinput.input()]:
  if len(line) == 0:
    sum = sum + len(curr_set)
    curr_set = None
    continue
  if curr_set is None:
    curr_set = set(line[:])
  else:
    curr_set = curr_set.intersection(set(line[:]))

sum = sum + len(curr_set)
  
print(sum)
