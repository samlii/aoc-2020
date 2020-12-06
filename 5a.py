#! env python3
import fileinput, sys

def seat_id(line):
  return int(''.join(['0' if x == 'F' or x == 'L' else '1' for x in line.strip()]),2)

seats = [seat_id(x) for x in fileinput.input()]
print(set(range(min(seats), max(seats))) - set(seats))
