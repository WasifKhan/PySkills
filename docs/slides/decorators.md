<!-- .slide: data-state="title" -->

# Decorators

---

## Topics
* Basics
* First Class Functions
* Argument Packing
* Decorators

---

## Basics
* Refresher
* Formal Definition

---

## Basics - Refresher
* Here is a refresher on a basic python function that squares a list of numbers
```
>>> x = [i for i in range(5)]
>>> def square_lst(lst):
>>>   y = []
>>>   for element in lst:
>>>     y.append(square(element))
>>>   return y
>>> y = square_lst(x)
>>> y
[0, 2, 4, 6, 8]
```

---

## Basics - Formal Definition
![functions](images/formal_functions.jpg)

---

## First Class Functions
* Nest
* Return
* Assignment
* Combination

---

## First Class Functions - Nest
* Python considers functions *First Class*
* This means functions are treated the same as any other type such as `int` and `str`
* Can nest functions within functions
```
>>> x = 10
>>> def f(x):
>>>   def g(y):
>>>     return x + y
>>>   return g(x)
>>> f(x)
20
```
---

## First Class Functions - Return
* Can return functions
```
>>> x = 10
>>> def f(x):
>>>   def g(y):
>>>     return x + y
>>>   return g
>>> f(x)(20)
30
```

---

## First Class Functions - Assignment
* Can assign functions to variables
```
>>> x = 10
>>> def f(x):
>>>   def g(y):
>>>     return x + y
>>>   return g
>>> add10 = f(10)
>>> add10(5)
15
```

---

## First Class Functions - Combination
* Combine these notions to produce powerful functions
```
>>> def adder(n):
>>>   def add_n(x):   # Nesting a function
>>>     return n+x
>>>   return add_n    # Returning a function
>>> add5 = adder(5)   # Assiging a function to a variable
>>> add10 = adder(10)
>>> add5(3)
8
>>> add10(5)
15
```

---

## Argument Packing
* Args
* Kwargs

---

## Argument Packing - Args
* Python allows us to pass an arbitrary amount of arguments to functions
* Done using the `*args`(`tuple`) and `**kwargs`(`dict`) keywords
* To pass an arbitrary amount of `elements` - use `*args`
```
>>> def f(*args):
>>>   print(args)
>>> f(1, 2, 'hello', [1, 2])
(1, 2, 'hello', [1, 2])
```
---

## Argument Packing - Kwargs
* To pass an arbirary amount of `key:value` pairs - use `**kwargs`
```
>>> def f(**kwargs):
>>>   print(kwargs)
>>> f(1:'hello', 2:'world')
{1:'hello', 2:'world'}
```

---

## Decorators
* Motivation
* Consolidate Code
* `@` Syntax
* Complete Example

---

## Decorators - Motivation
* Can combine the notion of First Class Functions and Args/Kwargs for complex functionality
* Motivate decorators with an example
* Say we want to write our own arithmetic functions for add, sub, etc...
* Also, say we wanted to ensure only `int` types are passed into each function
* One way to do this is write each function and validate arguments before each operation
```
>>> def add(x, y):                        >>> def sub(x, y):                        >>> def mult(x, y):
>>>   if type(x) is not int:              >>>   if type(x) is not int:              >>>   ...
>>>     print("Need x to be an integer")  >>>     print("Need x to be an integer")  >>> def div(x, y):
>>>   elif type(y) is not int:            >>>   elif type(y) is not int:            >>>   ...
>>>     print("Need y to be an integer")  >>>     print("Need y to be an integer")  >>> def mod(x, y):
>>>   else:                               >>>   else:                               >>>   ...
>>>     return x + y                      >>>     return x + y
```

---

## Decorators - Consolidate Code
- This results in a lot of duplicate code - a practice that's discouraged among programmers
- Decorators allow for us to isolate the common code within these functions into a separate function
- Consider the following function that generally checks the type of two parameters
```
>>> def validate_arguments(x, y):
>>>   if type(x) is not int:
>>>     print("Need x to be an integer")
>>>   elif type(y) is not int:
>>>     print("Need y to be an integer")
```

---

## Decorators - Consolidate Code
- Can nest *valiadte_arguments* within a general arithmetic function that consumes a specific operator
```
>>> def arithmetic(operator):
>>>   def validate_arguments(x, y):
>>>     if type(x) is not int:
>>>       print("Need x to be an integer")
>>>     elif type(y) is not int:
>>>       print("Need y to be an integer")
>>>     else:
>>>       return operator(x, y)
>>>   return validate_arguments
```
- Now if we have arithmetic functions, we can do a neat trick to validate arguments as follows
```
>>> def add(x, y):
>>>   return x + y
>>> add = arithmetic(add)
>>> add(1, 2)
3
>>> add('hi', 2)
'Need x to be an integer'
```

Note:
- Be sure to step through what's happening with `add=arithmetic(add)`

---

## Decorators - `@` Syntax
- Can nest *valiadte_arguments* within a general arithmetic function that consumes a specific operator
- Python provides the `@` keyword to support this behavior
- The above code is identical to the following
```
>>> @arithmetic
>>> def add(x, y):
>>>   return x + y
>>> add(1, 2)
3
>>> add('hi', 2)
'Need x to be an integer'
```
- Can now generally apply *valiadate_arguments* to any operator
```
>>> @arithmetic
>>> def sub(x, y):
>>>   return x - y
>>> sub(1, 2)
-1
>>> sub('hi', 2)
'Need x to be an integer'
```

---

## Decorators - Complete Example
- We can validate the arguments of any arbitrary function using `*args` and `**kwargs`
```
>>> def arithmetic(operator):
>>>   def validate_arguments(*args, **kwargs):
>>>     for x in args:
>>>       if type(x) is not int:
>>>         print("Need x to be an integer")
>>>         return None
>>>     return operator(*args, **kwargs)
>>>   return validate_arguments
```
- Used the same way but with now accepts general arguments
```
>>> @arithmetic             >>> @arithmetic
>>> def add(x, y):          >>> def add(x, y, z):
>>>   return x + y          >>>   return x + y + z
>>> add(1, 2)               >>> add(1, 2, 3)
3                           6
>>> add('hi', 2)            >>> add('hi', 2, 3)
'Need x to be an integer'   'Need x to be an integer'
```

---
