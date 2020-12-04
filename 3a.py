#! env python3
import fileinput, sys


def is_tree(marker):
  return marker == "#"


def count_trees(slope, mtn_map):
  return len( [x for (i,x) in enumerate(mtn_map) if (i % slope[1]) == 0 and is_tree(x[int(i*slope[0]) % len(x)])] )


mtn_map = [z.strip() for z in fileinput.input()]
slopes = [(1,1), (3,1), (5,1), (7,1), (.5,2)]

answer = 1

for slope in slopes:
  answer = answer * count_trees(slope, mtn_map)

print(answer)

