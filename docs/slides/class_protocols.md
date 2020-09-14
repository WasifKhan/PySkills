<!-- .slide: data-state="title" -->

# Class Protocols

---

## Topics
* Introduction
* Common Protocols

---

## Introduction
* What is a Protocol
* Python Protocols

---

## Introduction - What is a Protocol
* A protocol is a set of functions that define some pre-existing syntax in Python
* There are situations where we may want to add objects of classes (`+`) or compare objects (`<`)
* Python allows us to leverage this built-in syntax if we define various dunder methods

---

## Introduction - Python Protocols
* Python has over 50 different protocols but we will learn the most popular ones
* By the end of this section, we should be able to create instances `x` of a class that can leverage the following syntax:
* `len(x)`, `print(x)`, `x + x`, `x < x`, `x[1]`, `element in x`, `dict[x] = 1`
* This section will use the following class as a running example for the various protocols:
```
class Student:
  def __init__(self, name, age, grades=[]):
    self.name = name
    self.age = age
    self.grades = grades
wasif = Student("Wasif", 28, [50, 60, 55])
anton = Student("Anton", 29, [95, 90, 20])
greg = Student("Greg", 27, [79, 82, 85])
```

---

## Common Protocols
* Length
* Print
* Arithmetic
* Comparison
* Index/Slice
* Others

---

## Common Protocols - Length
* We can define the length (`__len__`) of a student to be the number of grades recorded
```
class Student:
  ...
  def __len__(self):
    return len(self.grades)
len(wasif) == 3
```

---

## Common Protocols - Print
* We can print(`__str__`) a student by returning a string containing his name and age
```
class Student:
  ...
  def __str__(self):
    return f'{self.name}: {self.age}'
print(wasif)
'Wasif: 28'
```

---

## Common Protocols - Arithmetic
* We can add (`__add__`), subtract (`__sub__`), etc.. classes as well
* In this example, it doesn't make sense to add students, so for demonstration purposes - let's assume adding students means adding their grades together
```
class Student
  ...
  def __add__(self, other):
    return Student(f'{self.name}, {self.age}, {self.grades + other.grades}')
wasif2 = wasif + anton
wasif2.grades == [50, 60, 55, 95, 90, 20]
```

---

## Common Protocols - Comparison
* We can see if one student is less than(`__lt__`) another student, as well as other comparison operations
* Let's assume student `a` is less than student `b` if he is younger
```
class Student:
  ...
  def __lt__(self, other):
    return True if self.age < other.age else False
wasif < anton) == True
```

---

## Common Protocols - Index/Slice
* We can index(`__getitem__`) students grades and set(`__setitem__`) grades as well
* Implementing indexing allows us the capacity to slice as well
```
class Student:
  ...
  def __getitem__(self, index):
    return self.grades[index]
  def __setitem__(self, index, value):
    self.grades[index] = value
wasif[0] == 50 # indexing
wasif[0:2] == [50, 60] # slicing
wasif[1] = 10 # mutating
```

---

## Common Protocols - Others
* `__iter__`, `__next__` for iteration
* `__hash__`, `__eq__` for hashing
* `__contains__` for membership(`in`)
* `__and__`, `__or__` for `and` and `or` operations
* Here is a [Comprehensive List](https://docs.python.org/3/reference/datamodel.html) of the protocols

---

<!-- .slide: data-state="title" -->

# End of
# Class Protocols

