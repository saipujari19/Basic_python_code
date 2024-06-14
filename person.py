#!/usr/bin/env python3
#saiprasad pujari
# define a class
class Person:
  """This is a simple class that holds info on a person"""

  def __init__(self, name, age):     # this init sets fields
    self.name = name
    self.age = age

# set fields
p1 = Person("John", 36)
p2 = Person("Mary", 18)
#p3 = Person("Rick")

print(p1.name)
print(p1.age)

print(p2.name)
print(p2.age)

#print (p2.gender)
#print (p3.name)

help(Person)
