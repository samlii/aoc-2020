#! env python3
import fileinput, sys, re

instructions = [x.strip() for x in fileinput.input()]


def accumulate(ptr, seen_instr, accum):
  if ptr in seen_instr:
    return -1
  if ptr >= len(instructions):
    return accum
  seen_instr.append(ptr)
  instr, amt = instructions[ptr].split()
  print(instr, amt)
  next_ptr = -1
  if instr == 'acc':
    accum = accum + int(amt)
    next_ptr = ptr + 1
  elif instr == 'jmp':
    next_ptr = ptr + int(amt)
  elif instr == 'nop':
    next_ptr = ptr + 1
  answer = accumulate(next_ptr, seen_instr, accum)
  if answer == -1 and instr in ['jmp','nop']:
    print('flipping', instr, amt)
    next_ptr = ptr + int(amt) if instr == 'nop' else ptr + 1
    answer = accumulate(next_ptr, seen_instr, accum)
  return answer


print(accumulate(0, [], 0))
