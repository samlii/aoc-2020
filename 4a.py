#! env python3
import fileinput, sys, re

def valid_height(value):
  if value[-2:] == 'in':
    return 59 <= int(value[:-2]) <= 76
  elif value[-2:] == 'cm':
    return 150 <= int(value[:-2]) <= 193
  else:
    return False

def valid_value(field, value):
  checks = {'byr': lambda v: 1920 <= int(v) <= 2002, 
   'iyr': lambda v: 2010 <= int(v) <= 2020,
   'eyr': lambda v: 2020 <= int(v) <= 2030, 
   'hgt': valid_height,
   'hcl': lambda v: v[0] == '#' and re.match(r'^[0-9a-f]{6}$', v[1:]),
   'ecl': lambda v: v in ['amb','blu','brn','gry','grn','hzl','oth'],
   'pid': lambda v: re.match(r'^[0-9]{9}$', v)}
  
  if checks[field](value):
    print("valid", field, value)
  
  return checks[field](value)
  



def is_valid(document):
  required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  return all(field in document.keys() and valid_value(field, document[field]) for field in required_fields)


count = 0
doc = {}
for line in fileinput.input():
  line = line.strip()
  if len(line) == 0:
    if is_valid(doc):
      print('valid', doc)
      count = count + 1
    else:
      print('invalid', doc)
    doc = {}
  else:
    doc.update(dict(x.split(':') for x in line.split()))

if is_valid(doc):
  print(doc)
  count = count + 1

print(count)
