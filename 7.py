#! env python3
import fileinput, sys, re

class Node:
  def __init__(self, name = "", parents = [], children = []):
    self.parents = parents
    self.children = children
    self.name = name
  
  def __str__(self):
    str_repr = "Node('" + self.name + "', parents = '[" 
    str_repr = str_repr + ",".join([x.name for x in self.parents])
    str_repr = str_repr + "]', children = '["
    str_repr = str_repr + ",".join([x.name for x in self.children]) 
    str_repr = str_repr + "]')"
    return str_repr


def all_containers(bag_type, map, bag_set):
  bag_set.update([bag_type])
  if len(map[bag_type].parents) == 0:
    return
  
  [all_containers(x.name, map, bag_set) for x in map[bag_type].parents]


map = {}
for line in [x.strip() for x in fileinput.input()]:
  parts = line.split('bags contain')
  bag_type = parts[0].strip()
  node = map.get(bag_type, Node(bag_type, parents = [], children = []))
  child_bags = parts[1].split(',')
  for child in child_bags:
    m = re.search(r'(\d{1,3})\s*(.*?)\s*bags?.?', child)
    if m is not None:
      child_node = map.get(m.group(2), Node(m.group(2), parents = [], children=[]))
      child_node.parents.append(node)
      map[child_node.name] = child_node
      node.children.extend([child_node] * int(m.group(1)))
  map[bag_type] = node

for k,v in map.items():
  print(k, v)

s = set()
all_containers('shiny gold', map, s)
s.discard('shiny gold')
print(len(s), s)
