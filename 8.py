#! env python3
import fileinput, sys, re

instructions = [x.strip() for x in fileinput.input()]
seen_instructions = []
ptr = 0
acc = 0
while ptr < len(instructions):
  if ptr in seen_instructions:
    print(acc)
    sys.exit()
  seen_instructions.append(ptr)
  instr, amt = instructions[ptr].split()
  print(instr, amt)
  if instr == 'acc':
    acc = acc + int(amt)
    ptr = ptr + 1
  elif instr == 'jmp':
    ptr = ptr + int(amt)
  else:
    ptr = ptr + 1
