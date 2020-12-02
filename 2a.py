#! env python3
import fileinput, sys

counter = 0
for x in fileinput.input():
  parts = x.strip().split(':')
  pwd = parts[1].strip()
  pw_def = parts[0].split()
  letter = pw_def[1]
  counts = pw_def[0].split('-')
  pos_one = pwd[int(counts[0]) - 1]
  pos_two = pwd[int(counts[1]) - 1]
  print(pwd, pw_def, letter, pos_one, pos_two)
  if (pos_one == letter) ^ (pos_two == letter):
    print("valid")
    counter = counter + 1
print(counter)
