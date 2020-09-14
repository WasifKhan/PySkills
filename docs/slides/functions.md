<!-- .slide: data-state="title" -->

# Functions

---

## Topics
* Basics
* Scope
* Functional Programming
* Complexity Theory

---

## Basics
- Python Memory Manipulation
- Formal Definition
- Args, Kwargs

---

## Basics - Python Memory Manipulation
* Functions allow us to manipulate memory in complex, systematic ways
* Functions can manipulate internal memory through the ```return``` statement
* An implicit ```return None``` is appended to the end of each function that doesn't explicitly return anything
```
>>> x = 10
>>> def square(x):
>>>   return x ** 2
>>> x = square(x)
>>> print(x)
100
```

---

## Basics - Python Memory Manipulation
* All previously learned notions can be applied within the context of a function
```
>>> x = [i for i in range(5)]
>>> def square_lst(lst):
>>>   y = []
>>>   for element in lst:
>>>     y.append(square(element))
>>>   return y
>>> y = square_lst(x)
>>> y
[0, 1, 4, 9, 16]
```

---

## Basics - Formal Definition
![functions](images/formal_functions.jpg)

---

## Basics - Args, Kwargs
* Python allows us to pass an arbitrary amount of arguments to functions
* Done using the `\*args`(`tuple`) and `\*\*kwargs`(`dict`) keywords
* To pass an arbitrary amount of `elements` - use `\*args`
```
>>> def f(*args):
>>>   print(args)
>>> f(1, 2, 'hello', [1, 2])
(1, 2, 'hello', [1, 2])
```
* To pass an arbirary amount of `key:value` pairs - use `\*\*kwargs`
```
>>> def f(**kwargs):
>>>   print(kwargs)
>>> f(v1:'hello', v2:'world')
{'v1':'hello', 'v2':'world'}
```

---

## Scope
- Terminology
- Blocks
- LEGB Scope
- Leaky Scope
- `global`, `nonlocal`

---

## Scope - Terminology
* ```Scope``` refers to the coding region from which a particle object is accessable
* We have seen code can be grouped through conditionals, iteration and functions
* When refering to a object, how does Python know which indent to retrieve this object from?
```
>>> x = 5
>>> if True:
>>>   x = 10
>>> def f():
>>>   x = 20
>>> f()
>>> print(x)
# What is x?
```
* To understand what ```x``` refers to, we need to understand Python [name resolution](https://docs.python.org/3/reference/executionmodel.html#resolution-of-names) rules

---

## Scope - Blocks
* A [block](https://docs.python.org/3/reference/executionmodel.html) is used block  to group related lines of code together that are meant to be executed as a unit
* The 3 block units in Python are functions, modules and classes (more on this later)
* Most languages have conditionals and iteration as blocks, Python is an exception here
* In Python, any indent (including blocks) is referred to as a [compound statement](https://docs.python.org/3/reference/executionmodel.htm://docs.python.org/3/reference/compound_stmts.html#grammar-token-funcdef)

---

## Scope - LEGB Scope
- When referencing a variable, Python follows the **LEGB** scope resolution order
- First look for an object in the **L**ocal block, then **E**nclosing, **G**lobal and finally **B**uilt-in block in order
- Given the following code, determine which block each reference belongs to
```
>>> x = 5
>>> def f(var):
>>>   x = 10
>>> f(20)
>>> print(x)
```
* ```f``` is called at **G**lobal block and exists at the **G**lobal block
* ```20``` is called at **G**lobal block and exists at the **B**uilt-in block
* ```print``` is called at **G**lobal block and exists at the **B**uild-in block
* ```x``` is called at the **G**lobal block and exists at the **G**lobal block

---

## Scope - LEGB Scope
* Given the following code, determine which block each reference belongs to
```
>>> x = 5
>>> def f(var):
>>>   x = 10
>>>   print(x)
>>> f(20)
```

* ```f``` is called at **G**lobal block and exists at the **G**lobal block
* ```20``` is called at **G**lobal block and exists at the **B**uilt-in block
* ```print``` is called at **L**ocal block (of ```f```) and exists at the **B**uild-in block
* ```x``` is called at the **L**ocal block (of ```f```) and exists at the **L**ocal  block

---

## Scope - Leaky Scope
* Going back to our previous code, we can now answer what `x` refers to
```
>>> x = 5
>>> if True:
>>>   x = 10
>>> def f():
>>>   x = 20
>>> f()
>>> print(x)
# What is x?
```
* Since conditionals (and loops) are not a valid block in Python, objects referenced within them will *leak* to the closest block they are in
* Therefore `x` will be `10` as the `x` within the `if` condition is not a block while the `x` within `f` is a block

---

## Scope - `global`, `nonlocal`
* What if we want to change a reference at global block within a function?
```
>>> x = 10
>>> def change_x():
>>>   x = 11
>>> change_x()
>>> x
10
```
* This is because a function is a *block*, therefore it will create a new reference to `x` in the **L**ocal block
* The ```global``` keyword is required to achieve this functionality
```
>>> x = 10
>>> def change_x():
>>>   global x
>>>   x = 11
>>> change_x()
>>> print(x)
11
```

---

## Scope - `global`, `nonlocal`
* For nested blocks that aren't global, use the ```nonlocal``` keyword
```
>>> x = 10
>>> def f():
>>>   x = 20
>>>   def g():
>>>     nonlocal x
>>>     x = x + 1
>>>   g()
>>>   print(x)
>>> f()
```
* The line `x = x + 1` refers to `x` in the **E**nclosing scope (`f`) therefore `x` will be `21`

---

## Functional Programming
- Motivation
- `map`
- `filter`
- Lambda Functions

---

## Functional Programming - Motivation
* Most tasks that can be accomplished with iteration can be accomplished with other methods as well
* As opposed to iterating over a container manually, we can call functions that do the same thing
* This is known as *Functional Programming* with the 2 most common functions being `map` and `filter`
* For example, consider a function that consumes a `list` of `int` and squares each number in the list
```
>>> def square_list(list_of_numbers):
>>>   for i in range(len(list_of_numbers)):
>>>     list_of_numbers[i] = list_of_numbers[i] ** 2
>>>   return list_of_numbers
>>> square_list([1, 2, 3])
[1, 4, 9]
```
* Notice we are applying a specific operation `lon[i] \*\* 2` to each element in the list. This is known as *mapping* a list

---

## Functional Programming - `map`
* To apply an operation to event element in a container, a good convention is to use `map`
```
>>> def square(n):
>>>   return n ** 2
>>> def square_list(list_of_numbers):
>>>   return list(map(square, list_of_numbers))
>>> square_list([1, 2, 3])
[1, 4, 9]
```
* The `map` function consumes a function and applies it to every element within the container

---

## Functional Programming - `filter`
* To selectively remove items from a container, a good convention is to use `filter`
```
>>> def is_odd(n):
>>>   return bool(n % 2)
>>> def remove_evens(list_of_numbers):
>>>   return list(filter(is_odd, list_of_numbers))
>>> remove_evens([1, 2, 3])
[1, 3]
```
* The `filter` function consumes a function and removes elements from the container which return false when applying the function

---

## Functional Programming - Lambda Functions
* Observe in the previous section, we wrote a lot of 1-line functions
* If a function requires one line, a good coding convention is to use `lambda`
* `lambda` dynamically creates a function that doesn't require a name
```
>>> list_of_numbers = [1, 2, 3]
>>> L_squared = list(map(lambda x: x**2, list_of_numbers)
>>> L_squared
[1, 4, 9]
```
---

## Complexity Theory
- Definition
- Performance Analysis
- Examples

---

## Complexity Theory - Definition
* Complexity theory is the study of how *complex* functions are
* One central goal for software development is to write programs as efficiently as possible
* We can analyze and compare the efficiency of different programs using complexity theory

---

## Complexity Theory - Definition
* To analyze the runtime of a program, we need to cumulate the runtimes of all the operations within the program
* Runtimes can be grouped into 5 main categories
  * Constant runtime, denoted as `O(1)`
  * Logarithmic runtime, denoted as `O(logn)`
  * Linear runtime, denoted as `O(n)`
  * Quadratic runtime, denoted as `O(n^2)`
  * Exponential runtime, denoted as `O(2^n)`

---

## Complexity Theory - Performance Analysis
* Constant runtime example
```
>>> def constant_runtime(n):
>>>   return n * 2
```
* Logarithmic runtime example
```
>>> def logarithmic_runtime(n):
>>>   while n > 0:
>>>     print(n)
>>>     n = n / 2
```
* Linear runtime example
```
>>> def linear_runtime(n):
>>>   while n > 0:
>>>     print(n)
>>>     n = n - 1
```

Note:
* Explain these runtimes at a high level, will go into the math later

---

## Complexity Theory - Performance Analysis
* Quadratic runtime example
```
>>> def quadratic_runtime(n):
>>>   while n > 0:
>>>     m = n
>>>     while m > 0:
>>>       print(n*m)
>>>       m = m - 1
>>>     n = n - 1
```
* Exponential runtime examples require additional concepts so we will see this later in the course

---

## Complexity Theory - Performance Analysis - Arithmetic
* When adding runtimes by a constant, omit the constant
* `O(n) + 5 = O(n)`
* When multiplying runtimes by a constant, omit the constant
* `O(n^2) * 10 = O(n^2)`
* When adding runtimes together, keep the largest runtime
* `O(1) + O(n) + O(logn) + O(n^2) = O(n^2)`
* When multiply runtimes together, simply multiply the numbers
* `O(n) * O(logn) = O(nlogn)`

---

## Complexity Theory - Performance Analysis - Code
* We can determine the runtime of an arbitrary function using some guidelines
* The runtime of code written in the same block is **added** together
* The runtime of code written in a nested block is **added** together, with the exception of *iteration*
* The runtime of code written in a nested block of *iteration* is **multiplied** together

---

## Complexity Theory - Examples
* Let's consider a more complex function and determine it's runtime
```
>>> def largest(a, b, c):
>>>   if a >= b and a >= c:
>>>     return a
>>>   elif b >= a and b >= c:
>>>     return b
>>>   else:
>>>     return c
```

* Runtime for the first condition statements are as follows
* `a >= b` and `a >= c` are both *constant runtime*
* `return a` is *constant runtime*
* Therefore the first condition is `(constant runtime + constant runtime) * constant runtime` = `constant runtime`
* The same logic can be applied for the other 2 conditionals
* Therefore the programs runtime is `constant runtime * 3` = `constant runtime`

Note:
* Explain that we are only multipling by 2 and 3 as this is equivilent to adding them 2 and 3 times respectively

---

## Complexity Theory - Examples
* Let's consider an even more complex function and determine it's runtime
```
>>> def list_min(lst):
>>>   min_element = None
>>>   for element in lst:
>>>     if min_element is None:
>>>       min_element = element
>>>     else:
>>>       if min_element < element:
>>>         min_element = element
>>>   return min_element
```
* `min_element = None` is *constant runtime*
* `for element in lst` is *linear runtime*
* lines 4-8 are *constant runtime*
* Therefore the runtime of the loop is `linear * ((constant * constant) + (constant * constant)) = linear runtime`
* `return min_element` is *constant runtime*
* Therefore the runtime of the program is `constant + linear + constant = linear runtime`

---

<!-- .slide: data-state="title" -->

# End of
# Functions

