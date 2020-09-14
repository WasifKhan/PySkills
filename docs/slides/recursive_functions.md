<!-- .slide: data-state="title" -->

# Recursive Functions

---

## Topics
- Introduction to Recursion
- Complexity Analysis
- Interview Problems

---

## Introduction to Recursion
- Definitions
- Sum List

---

## Introduction to Recursion - Definitions
- ***Recursion*** is when something is defined in terms of itself, or something of the same type

---

## Introduction to Recursion - Definitions
- Fibonacci numbers are a simple example of recursion
- The first and second Fibonacci numbers are both 1:
- Fib(1) = 1, Fib(2) = 1
- Each Fibonacci number after that is the sum of the two Fibonacci numbers preceeding it:
- Fib(n) = Fib(n-1) + Fib(n-2)
- This is a recursive definition, because fibonacci numbers are defined in terms of other fibonacci numbers
- This definition gives the following sequence of numbers:
- 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

---

## Introduction to Recursion - Definitions
- A recursive definition always has two aspects: a ***base case***, and a ***recursive case***
- A ***base case*** is the part of the definition that is not self-referential:
- Fib(1) = 1, Fib(2) = 1
- A ***recursive case*** is the part of the definition that is self-referential:
- Fib(n) = Fib(n-1) + Fib(n-2)

---

## Introduction to Recursion - Definitions
- A ***recursive function*** is a function that calls itself in its body
- A recursive function has base cases and recursive cases
- Every recursive function needs a conditional statement to separate the base cases from the recursive cases
- The conditional branches where the function does not call itself are the base cases
- The conditional branches where the function does call itself are the recursive cases

---

## Introduction to Recursion - Sum List
- Python can sum all the values in a list
- `sum([1,2,3,4])` evaluates to `10`
- This functionality can be implemented manually using a recursive function
```
def sum_list(list):
    if not list:
        return 0
    return list[0] + sum_list(list[1:])
```
- The base case is when the input is an empty list
- The recursive case is when the input is a non-empty list

---

## Introduction to Recursion - Sum List
- Each recursive step does a little bit of work
- The recursion stops once it reaches the base case
- This recursive case: `return list[0] + sum_list(list[1:])`
- And this base case: `return 0`
- Leads to this computation:
```
sum_list([1, 2, 3, 4])
=> 1 + sum_list([2, 3, 4])
=> 1 + 2 + sum_list([3, 4])
=> 1 + 2 + 3 + sum_list([4])
=> 1 + 2 + 3 + 4 + sum_list([])
=> 1 + 2 + 3 + 4 + 0
=> 1 + 2 + 3 + 4 
=> 1 + 2 + 7
=> 1 + 9
=> 10
```

---

## Introduction to Recursion - Sum List
- Simple recursive functions can be written non-recursively with a loop
```
def sum_list(list):
    sum = 0
    for element in list:
        sum += element
    return sum
```
- This is called an iterative solution, as opposed to a recursive solution
- Any iterative solution can be written recursively, but the opposite is not true
- Complex recursive functions can not be written iteratively
- Being comfortable with both approaches is important for software developers

---

## Complexity Analysis
- Sum List
- Fibonacci

---

## Complexity Analysis - Sum List
- The previous recursive solution to `sum_list` is very slow:
```
def sum_list(list):
    if not list:
        return 0
    return list[0] + sum_list(list[1:])
```
- At every recursive step, the slice `list[1:]` is evaluated
- Python slices lists by making a copy
- Making a copy takes linear time, O(n) for a list of length n, at every single recursive step
- There are n recursive steps, each recursive step takes O(n) time
- Therefore the total runtime is quadratic: O(n<sup>2</sup>)

---

## Complexity Analysis - Sum List
- Quadratic runtime is very slow
- The problem is copying the list at every recursive step
- A much faster solution modifies the original list instead of making copies:
```
def sum_list(list):
    if not list:
        return 0
    return list.pop() + sum_list(list)
```
- `list.pop()` takes constant time, so now there is O(1) work done at every recursive step
- There are n recursive steps, therefore the total runtime is linear: O(n)

---

## Complexity Analysis - Sum List
- The previous solution removes elements from the list as it processes them
- Sometimes this is a problem, and the list has to remained unchaged
- It's possible to achieve linear runtime, without destroying the list, using a helper function:
```
def sum_list(list):
    list_copy = list[:]
    return sum_list_helper(list_copy)
```
```
def sum_list_helper(list):
    if not list:
        return 0
    return list.pop() + sum_list(list)
```

---

## Complexity Analysis - Sum List
- `sum_list` creates a copy of the list that can be destroyed without affecting the original list
- Making the copy takes linear time
- `sum_list_helper` sums the list using the destructive method, which takes linear time
- In total, the whole function still takes linear time, while preserving the original list
- Using a helper function for pre-processing is a common pattern in recursive problems

---

## Complexity Analysis - Fibonacci
- `fibonacci` is a function that takes in a positive integer n, and returns the nth Fibonacci number:
```
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
```
- The base case is when n is 0 or 1
- The recursive case is when n > 1

---

## Complexity Analysis - Fibonacci
- The time it takes to calculate the nth Finoacci numbers is the sum of the times it takes for the previous two
- The full derivation is beyond the scope of this course, but this relationship results in exponential runtime
- For the nth Fibonacci number, the function will take O(2<sup>n</sup>) time
- This is absurdly slow
- To calculate the 100th Fibonacci number would take longer than the age of the universe
- This can be sped up to linear time using Dynamic Programming, which will be covered in the Algorithms section

---

## Interview Problems
- Convert Decimal String to Integer
- Convert Hexadecimal String to Integer

---

## Interview Problems - Convert Decimal String to Integer
- Decimal notation is the familiar way to write integers
- Decimal notation uses a base of 10
- Decimal notation uses 10 digits: 0-9
- 5729 in decimal notation represents:
- 9\*10<sup>0</sup> + 2\*10<sup>1</sup> + 7\*10<sup>2</sup> + 5\*10<sup>3</sup>
- Each digit counts a power of ten
- The rightmost digit is understood to be the ***least signficant digit***
- It counts the smallest power of 10: 10<sup>0</sup>
- The leftmost digit is understood to be the ***most signficant digit***
- It counts the largest power of 10, which is implied by the number of digits

---

## Interview Problems - Convert Decimal String to Integer
- Problem: Write a recursive function `string_to_int` that converts a decimal notation string to an integer
- Strategy: Handle negative integers separately, use a helper function for recursion
- A dictionary mapping characters to digit values is needed:
```
char_to_digit_value = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}
```

---

## Interview Problems - Convert Decimal String to Integer
- Implementation:
```
def string_to_int(string):
    if string[0] == "-":
        return -1 * string_to_int_helper(string[1:], 0)
    return string_to_int_helper(string[:], 0)
```
```
def string_to_int_helper(string, partial_result):
    if not string:
        return partial_result
    partial_result = 10 * partial_result + char_to_digit_value[string[0]]
    return string_to_int_helper(string[1:], partial_result)
```

---

## Interview Problems - Convert Decimal String to Integer
- This a step by step trace of what's happening when `string_to_int_help` is called:
```
string_to_int_helper("5729", 0)
=>
partial_result = 10 * 0 + 5 = 5
string_to_int_helper("729", 5)
=>
partial_result = 10 * 5 + 7 = 57
string_to_int_helper("29", 57)
=>
partial_result = 10 * 57 + 2 = 572
string_to_int_helper("9", 572)
=>
partial_result = 10 * 572 + 9 = 5729
string_to_int_helper("", 5729)
=>
5729
```

---

## Interview Problems - Convert Decimal String to Integer
- Python has a built in way to do type conversions:
- `int("5729")` evaluates to the integer `5729`
- `str(5729)` evaluates to the string `"5729"`

---

## Interview Problems - Convert Hexadecimal String to Integer
- Hexadecimal notation is used widely in software engineering
- Hexadecimal notation is an alternative to decimal notation
- Hexadecimal uses base 16 instead of base 10 to denote numbers
- Decimal notation has 10 digits: 0-9
- Hexadecimal notation has 16 hexits: 0-9, a-f
- Just like decimal, the leftmost hexit is most significant
- The rightmost hexit is least significant

---

## Interview Problems - Convert Hexadecimal String to Integer
- This is a Python dictionary for converting characters to their hexit values:
```
char_to_hexit_value = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15
}
```

---

## Interview Problems - Convert Hexadecimal String to Integer
- 0x is prepended to hexadecimal numbers for disambiguation
- Recall that each digit in decimal notation counts powers of 10
- Each hexit in hexadecimal notation counts powers of 16
- This can be used to convert from hexadecimal to decimal notation
- 0x1a5c represents:
- c\*16<sup>0</sup> + 5\*16<sup>1</sup> + a\*16<sup>2</sup> + 1\*16<sup>3</sup>
- = 12\*16<sup>0</sup> + 5\*16<sup>1</sup> + 10\*16<sup>2</sup> + 1\*16<sup>3</sup>
- = 6748
- Notice that 6748 is not equal to 0x6748

---

## Interview Problems - Convert Hexadecimal String to Integer
- Problem: Write `hex_to_int` which takes in a positive integer represented in a hexadecimal notation string, and output an integer
- The strategy is similar to the previous problem:
```
def hex_to_int(hex_string):
    if hex_string[0:2] == "0x":
        return hex_to_int_helper(hex_string[2:], 0)
    else:
        raise TypeError
```
```
def hex_to_int_helper(hex_string, partial_result):
    if not hex_string:
        return partial_result
    partial_result = 16 * partial_result + char_to_hexit_value[hex_string[0]]
    return hex_to_int_helper(hex_string[1:], partial_result)
```
- `hex_to_int` raises an error is "0x" isn't prepended to the input
- This will be explained thoroughly in tomorrow's lecture

---

<!-- .slide: data-state="title" -->

# End of
# Recursive Functions

