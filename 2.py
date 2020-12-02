#! env python3
import fileinput, sys

counter = 0
for x in fileinput.input():
  parts = x.strip().split(':')
  pwd = parts[1]
  pw_def = parts[0].split()
  letter = pw_def[1]
  counts = pw_def[0].split('-')
  min_count = int(counts[0])
  max_count = int(counts[1])
  if min_count <= len([x for x in pwd if x == letter]) <= max_count:
    counter = counter + 1
print(counter)
