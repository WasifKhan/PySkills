<!-- .slide: data-state="title" -->

# Object Oriented Programming

---

## Topics
- Classes
- Python Features

---

## Classes
* Motivation
* Initialization
* Attributes
* Methods
* Inheritance

---

## Classes - Motivation
- All data types seen thus far store information useful for the computer (int, dict, etc...)
- What if we wanted to store information useful for a human (students, company financials, etc...)
- Consider a situation where we need to store information about students in a classroom
- We could have a `str` to store the name, an `int` for their age, a `list` for their grades, etc...
```
student_1_name = "Wasif"
student_1_age = 27
student_1_grades = [84, 92, 88, 72, 69]
student_2_name = "Anton"
student_2_age = 29
student_2_grades = [77, 62, 58, 62, 59]
```
- We could store this student information in a list
```
list_of_names = [student_1_name, student_2_name]
list_of_ages = [student_1_age, student_2_age]
list_of_grades = [student_1_grades, student_2_grades]
```

---

## Classes - Motivation
- To do computations such as determining the name of the oldest student would be possible, but prone to error
```
def oldest_student(list_of_names, list_of_ages, list_of_grades):
    index = 0
    while index < len(list_of_names):
        if list_of_ages[index] == max(list_of_ages):
            return list_of_names[index]
        index += 1
```
- This code assumes the lengths of each of the 3 lists passed in are the same
- This code assumes the indicies of each of the 3 lists passed in correspond to the same student
- If that changes, or someone mistakenly forgets to add an age entry for a student - this code will crash
- The problem here arises due to the information having a natural grouping associated to it and no way for Python to capture this grouping with the data types seen so far

---

## Classes - Motivation
- A <a class="tooltip" href="#">`Class`<span>The word has its roots in biology - classification of species</span></a> is a programmatically friendly way to group information and store it in a **custom data type** through the `class` syntax
```
class Student:
    pass
```
- The above code creates a custom type called `Student` similar to the `int` type
- We can now create **objects** (instances) of `Student` similar to an `int` type
```
>>> Wasif = Student()       >>> x = int()
>>> type(Wasif)             >>> type(x)
<class '__main__.Student'>  <class 'int'>
```
- The above code creates 2 objects named *Wasif* and *x* of type `Student` and `int` respectively
- The integer *initializer* can optionally consume a number to allow for variability between integer objects. A similar functionality can be achieved with classes as well

---

## Classes - Initialization
- We can initialize a custom class by defining an `__init__` method within the class
- This method should consume all the data needed to initialize an instance of the class
```
class Student:
    def __init__(self, input_name, input_age, input_grades):
        self.name = input_name
        self.age = input_age
        self.grades = input_grades
```

- We can now create meaningful instances of students
```
Wasif = Student('Wasif', 27, [84, 92, 88, 72, 69])
Anton = Student('Anton', 29, [77, 62, 58, 62, 59])
list_of_students = [Wasif, Anton]
```
- The `self` parameter refers to the variable on the left side of the initialization (*Wasif* and *Anton*)
- The `self.name = name` creates a `name` attribute in the `Student` class and binds it to the parameter passed in

---

## Classes - Initialization
- A general convention is to name attributes the same as the parameters passed to the function, but this is not necessary
```
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
# Instances of Student
Wasif = Student('Wasif', 27, [84, 92, 88, 72, 69])
Anton = Student('Anton', 29, [77, 62, 58, 62, 59])
```
- The notion of structuring your codebase through classes representing meaningful information is known as **Object Oriented Programming** (OOP)

---

## Classes - Attributes
- The benefit of OOP is that it allows related variables to be grouped together in a coherent structure
- If a variable exists within a class, it is considered an **attribute**
- Attributes are specific to each object and can be accessed with the dot(`.`) syntax
```
print(Wasif.name)
Wasif.age = 20
print(Wasif.age)
print(Anton.age)
```
- The output will be
```
'Wasif'
20
29
```
- Notice that when we changed `Wasif.age`, the change was not reflected in `Anton.age`

---

## Classes - Attributes
- We can also have attributes that persist across objects. These are denoted as **class variables**
```
class Student:
    num_students = 0
    def __init__(self, input_name, input_age, input_grades):
        self.name = input_name
        self.age = input_age
        self.grades = input_grades
        Student.num_students += 1
```
- Now we can create students and keep track of how many instances we created
```
Wasif = Student('Wasif', 27, [84, 92, 88, 72, 69])
print(Student.num_students)
Anton = Student('Anton', 29, [77, 62, 58, 62, 59])
print(Student.num_students)
```
- The output will be
```
1
2
```
- Note that class variables must be accessed through the class, not the objects

---

## Classes - Methods
- Classes do more than group data together
- Classes also associate code blocks that operate on the data
- A **method** is similar to a function, but it is not defined in the global namepsace
- Methods have to be called from an instance of a class
- When you implement a class, you can write your own class methods
```
class Student:
    def average(self):
	return sum(self.grades) / len(self.grades)
```

---

## Classes - Inheritance
- Classes can inherit from one another
- The best way to think of class inheritance is as a subcategory
- When class A inherits from class B, class A is a subcategory of class B
- For example, Graduate can be a subcategory of Student
```
class Graduate(Student):
    def __init__(self, name, age, grades, graduation_date):
        Student.__init__(self, name, age, grades)
        self.graduation_date = graduation_date
```
- A subclass inherits all of its parent's methods
- The `__init__()` method is inherited by default, or you can re-implement it

---

## Python Features
* Context Managers
* Exceptions
* Modules

---

## Python Features - Context Managers
- We are often times in situations where we need to leverage resources outside of our code
  - For example, needing to open a file, access a database or website
- A Context manager is a [compound statement](https://byteacademyco.github.io/Introduction-To-Python/#/1/9) that allow us to isolate some code that interacts with the outside world
- We typically do generic operations when beginning and ending the interaction with outside objects
  - For example, opening/closing a file, connecting/disconnecting to a database or website
- In situations like this, we want to isolate the code with the `with` keyword
- The `with` syntax allow some default behavior to happen upon entering and existing an indent of code

---

## Python Features - Context Managers
- When working with files, the generic operations we execute are:
  - open the file, work with the contents, close the file
- The `with` keyword allows this functionality to happen by default
```
with open('file.txt') as var:
    # work with var
```
- Upon exiting this indent, Python will automatically call `var.close()`
- Context managers don't solve any problems that cannot be solved with other methods, they are to help make our code less prone to bugs

---

## Python Features - Exceptions - Introduction

- Sometimes we may write some code that is inherently prone to error
- For example, a function that divides two numbers is prone to dividing by 0
```
def div(a, b):
    return a / b
```
- If the user enters `b=0` then the code will crash and result in a `ZeroDivisionError`
```
>>> div(10, 0)
Traceback (most recent call last):
    File "<stdin>", line 1 in <module>
ZeroDivisonError: division by zero
```
- `ZeroDivisionError` is one of many `Exceptions` Python provides for incorrect semantics

---

## Python Features - Exceptions - Catching Exceptions
- What if we wanted this function to work even when the user input 0?
- This is accomplished via the `try` and `except` syntax
```
def div(a, b):
    try:
        return a / b
    except:
        print("Cannot divide by 0")
        return None
```
- Now running the program with `b=0` will not crash the code
```
>>> div(10, 0)
Cannot divide by 0
```

---

## Python Features - Exceptions - Raising Exceptions
- We can also reformat this code to `raise` our own exception
```
def div(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by 0")
        return None
```
- This will run the same as the code above
```
>>> div(10, 0)
Cannot divide by 0
```

---

## Python Features - Exceptions - Hierarchy
- Exceptions are arranged hierarchically. The `ZeroDivsionError` can also be captured more generally in the `ArithmeticError` exception
```
def div(a, b):
    try:
        return a / b
    except ArithmeticError:
        print("Generic airthmetic error")
    except ZeroDivisionError:
        print("Cannot divide by 0")
```
- Now we will no longer be catching a `ZeroDivisionError` as it is caught in the `ArithmeticError`
```
>>> div(10, 0)
Generic arithmetic error
```
- It is a poor coding convention to have *higher level* exception handling before *lower level* handling
- A deltailed list of Python exceptions can be found [here](https://docs.python.org/3/library/exceptions.html)

---

## Python Features - Modules
- A `module` is simply a fancy name for a `.py` file. Sometimes also referred to as a `script`
- Separating code into independent chunks allows us to *modularize* our code in more coherent ways
- Say we have a file `add.py` that contains the following code
```
def add_nums(a, b):
    return a + b
```
- We can now leverage this code in another file with the `import` syntax
```
import add
print(add.add_nums(1, 2)) # Prints 3
```

---

## Python Features - Modules - Import Methods
- The `import add` line copies all the names at `global` scope into your file
- Sometimes this can be wasteful if we are dealing with large files
- To import specific global variables from a file, use the `from` syntax
- It wouldn't make much difference in the example above, but the code would look as follows
```
from add import add_nums
print(add_nums(1, 2)) # Prints 3
```

---

<!-- .slide: data-state="title" -->

# End of
# Classes and Objects

