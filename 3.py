#! env python3
import fileinput, sys

def is_tree(marker):
  return marker == "#"

trees = [x for (i,x) in enumerate([z.strip() for z in fileinput.input()]) if is_tree(x[(i*3) % len(x)])]

print(trees, len(trees))
