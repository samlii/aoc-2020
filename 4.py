#! env python3
import fileinput, sys

def is_valid(document):
  required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  return all(field in document.keys() for field in required_fields)


count = 0
doc = {}
for line in fileinput.input():
  line = line.strip()
  if len(line) == 0:
    print(doc, is_valid(doc))
    if is_valid(doc):
      count = count + 1
    doc = {}
  else:
    doc.update(dict(x.split(':') for x in line.split()))

if is_valid(doc):
  count = count + 1

print(count)
