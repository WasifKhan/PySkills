<!-- .slide: data-state="title" -->

# MVC Architecture
* The MVC architecture is a very common design pattern that lots of frameworks use.

---

## Topics
* Design Patterns
* MVC
* Example

---
## Design Patterns
* What are they?
* Lots of them!

---

## Design Patterns - What are they?
* Design patterns are common, big picture patterns of how one organizes a project
* There are many different design patterns used in various domains
* MVC is a design pattern typically used for user interfaces (like GUIs) and very often used in web development

---

## Design Patterns - Lots of them!
* There are a lot of them!
<img src="images/design_patterns.png">
(source: Wikipedia) 

---

## MVC
* Overview
* What does it stand for?
* Model
* View
* Controller

---

## MVC - Overview
* MVC is a design pattern that aims to separate the code handling data, from the user interface, and the logic
* This is a form of "Seperation of Concerns" where you break the project into smaller, mostly independent parts that can be handled individually
* This is good for teams because different people can be put on different parts of the project and work in parallel
* This also helps with reasoning about the code, as you can focus on portions of the app individually

---

## MVC - What does it stand for?
* M - Model, V - View, C - Controller
* To explain the M, V, and C, let's take the example of a forum website so we can see how everything fits in.
* A forum website allows people to have user accounts, start topics, and leave comments on the topic to have a discussion.

---

## MVC - What does it stand for?
Here is a picture that might help with the concept:
<img src="https://upload.wikimedia.org/wikipedia/commons/a/a0/MVC-Process.svg" style="width: 600px">
(source: Wikipedia)

---

## MVC - Model
* The Model of MVC is responsible for managing and manipulating the application's data (sometimes called state).
* In the forum example, the Model represents accounts, topics, and comments.
* The Model is responsible for saving the data (usually in a database) and making sure all the required fields are there
* For example, a comment needs to be associated with a topic and the user posting it. If either is missing the Model won't allow it.
<!-- 
* The Model determines the structure and representation of the data. For example the data might be a list of dictionaries or perhaps a tree strucure. The model will provide an interface (some classes or functions) for doing operations on the data.
* Another role of the model is persisting the data over time. This could be via a database or perhaps a file. The model would hide the details of connecting and talking to a database or serializing and deserializing a file, making the particular choice of persistence irrelevant to the rest of the application.
-->
<!-- * The Model is in charge of data constraints. For example a phone number must consist of only numeric digits, and an email must contain an '@' symbol followed by more characters, a '.' and then a few more characters -->

---

## MVC - View
* The V in MVC is the View, this is the part of the application responsible for displaying the data to the user.
* In the forum example, the view is the HTML and CSS (specially formated text) that displays and styles the user interface in the browser.
* The View is what the user sees and therefore should be aesthetically pleasing and well polished (designers can help tremendously with this)
<!--
* Depending on the platform, the way to build views can vary widely from text based, to drag-n-drop, to pixel manipulation.
* For example, the view on the web is a text based format (HTML/CSS), the view for a desktop application might be a GUI built by a drag-n-drop editor, and the view of a video game is a bunch of math, triangles, and pixels.
-->

---

## MVC - Controller
* Lastly the C in MVC stands for Controller, the part that takes the user input and determines what to do with it.
* In the forum example, the Controller will load comments from the Model and send it to the View for display to the user.
* The Controller will also take a user submitted comment from the View and use the Model to save it.
<!-- 
* The Controller is mainly the logic of the whole application, i.e. when a user clicks this button the view needs to change to this or the model needs to do this.
-->
* The Controller acts as a bridge between the Model and the View

---
## Example
* Terminal Teller
* Model
* View
* Controller
* Running it

---

## Example - Terminal Teller
* Let's build an application that simulates an ATM, we will call it Terminal Teller
* When Terminal Teller is run, it should ask for account number and pin, then give the user options to view balance, deposit, withdraw, and logout. We will allow the user to deposit any (positive) amount, and won't allow them to withdraw more than they have (unless you want to start adding fees<!-- 😉 -->)
* The user should be able to exit the program and later start it again and find all their money there!
* If you are feeling adventurous, after lecture you can try to add interest to the accounts.
(hint: add a timestamp to the account so you can see how much time has elapsed since last activity to calculate the interest)

---

## Example - Model
* We need to think how we are going to keep track of all the users and their balances... *think about it for a bit*
* There are a couple of solutions but let's use a dictionary of dictionaries. We will use a global variable `data` with keys as account numbers. The value for a given account will be another dictionary with keys: `'name'`, `'pin'`, and `'balance'`.
* To persist the data, we will save and load the data from a file as JSON

---

## Example - Model - Setup Load
* Make a file `ttrader/model.py` and we will start with the `load` function that will load the data from a `bank.json` into a global `BANK` variable.
```
import json
BANK_FILE = 'bank.json'
BANK = {}
def load():
    global BANK
    with open(BANK_FILE, 'r') as f:
        BANK = json.load(f)
```
**Note&#58;** we need to use the `global` keyword here, else the data will just be loaded into a local variable and will only be available inside that function.
* This function will need to be called when our program first starts, we will keep this in mind for now and come back to it later.

---

## Example - Model - Account Class
* We will use an `Account` class to represent the accounts. It should have an account number, name, pin, and balance, so we will start with this:
```
class Account:
    def __init__(self, acct_num, name, pin, balance):
        self.account_number = acct_num
        self.name = name
        self.pin = pin
        self.balance = balance
```
* Note&#58; we will rarely use the constructor outside of `model.py` and instead use class methods to create `Account` objects.

---

## Example - Model - Account.save
* Next we want our account's to be able to save.
* To do this we will add our account info to the `BANK` and then dump the `BANK` as JSON to the file.
```
def save(self):
    info = {"name": self.name, "pin": self.pin, "balance": self.balance}
    # add info dictionary to BANK dictionary
    BANK[self.account_number] = info
    # now save to a file
    with open(BANK_FILE, 'w') as f:
        json.dump(BANK, f)
```
This definition is inside our `Account` class
* Notice we open the file in **write** mode, not append mode, think about why that is...
* If we appended the JSON data then that would no longer be valid JSON. For example the file might have `{...}{...}` if we append, which is not valid JSON.

---

## Example - Model - Account.new
* Now we need a way to create a new account.
* We do not want to use the constructor because the controller will not know what to use as a unique account number.
* Instead we will make a class method that takes a `name` and `pin` and creates the account with a unique number for us.
```
import math # <- this at the top of the file, rest in Account class
@classmethod
def new(cls, name, pin):
    # generate a probably unique account number
    account_num = round(math.random()*1e7)
    while account_num in BANK: # ensure it's unique
        account_num = round(math.random()*1e7)
    # now make the account object
    acct = Account(account_num, name, pin, 0)
    acct.save() # make sure it's saved in the BANK
    return acct # new Account object ready for use
```

---

## Example - Model - Account.login
* Next we need a way to login a user via account number and pin.
* This will also be a class method because a successful login should return an account object with all of it's data loaded. information.
```
@classmethod
def login(cls, acct_num, pin):
    if acct_num in BANK:
        if BANK[acct_num]['pin'] == pin:
            # create and return the Account object
            name = BANK[acct_num]['name']
            balance = BANK[acct_num]['balance']
            acct = Account(acct_num, name, pin, balance)
            return acct
    # failed either condition return None
    return None
```

---

## Example - Model - acct.deposit
* Now we need a way to `deposit` money into an account.
* This will be a function on the account object responsible for updating the balance and saving it.
```
def deposit(self, amount):
    self.balance += amount
    self.save()
```

---

## Example - Model - acct.withdraw
* Lastly we will need a `withdraw` function.
* This will also be a function on the account object, and it will be responsible for updating the balance.
* However, `withdraw` should not allow a negative balance, and should return `False` that way the controller can display an insufficient funds message.
```
def withdraw(self, amount):
    if amount <= self.balance:
        self.balance -= amount
        self.save() # remember to save, else free money
        return True # successful withdraw
    # else amount > balance so overdraft
    return False
```
* If you are feeling adventurous, change your bank's policy to allow for small overdrafts but with a fee added.

---

## Example - View - The Logon Prompt
* The view, `ttrader/views.py` should contain some simple functions that display the various prompts.
* The view functions should return the user input(s).
* We will start with what `ttrader` first shows, `logon_prompt`:
```
def logon_prompt():
    menu = """
    1) Create Account
    2) Login
    3) Exit
    """
    print(menu)
    choice = input('What do you want to do? ')
    return choice
```

---

## Example - View - The New User Prompt
* Next we need a way to handle new user creation.
```
def new_user_prompt():
    name = input('Enter your name: ')
    pin = input('Enter your pin: ')
    return [name, pin]
```
* A nice feature would be to ask for the pin twice to verify the user typed it correctly. Try to add this on your own.
---

## Example - View - The Login Prompt
* Also we need to allow users to login.
```
def login_prompt():
    account_num = input('Enter your account number: ')
    pin = input('Enter your pin: ')
    return [account_num, pin]
```

---

## Example - View - Login Fail Message
* We need to handle if the user inputs the wrong account number or pin.
```
def login_fail():
    print('Incorrect account number or pin! Please try again')
```

---

## Example - View - Welcome Message
* Welcome the user.
```
def welcome(acct):
    print(f'Welcome! Account #{acct.account_number}')
```

---

## Example - View - Main Account Screen
* The screen for when they are logged in.
```
def account_prompt():
    menu = """
    1) Show balance
    2) Deposit
    3) Withdraw
    4) Logout
    """
    print(menu)
    choice = input('Enter your choice: ')
    return choice
```

---

## Example - View - Show Balance
* For the "Show balance" option:
```
def show_balance(acct):
    print(f'Account #{acct.account_number} has a balance of ${acct.balance}')
```

---

## Example - View - Deposit Screen
* A way to get their deposit.
```
def deposit_prompt():
    amount = float(input('How much would like to deposit? $'))
    return amount
```
* Currently, if the user types an invalid number it will crash Terminal Teller, after lecture try to fix this. You should display an error message and ask until a valid number is supplied.

---

## Example - View - Withdraw Screen
* A way to withdraw.
```
def withdraw_prompt():
    amount = float(input('How much would like to withdraw? $'))
    return amount
```
* Same as the `deposit_prompt`, fix what happens if the user gives an invalid number.

---

## Example - View - Insufficient Funds
* An insufficient funds message if they try to withdraw too much.
```
def display_not_enough():
    print('Sorry you don\'t have sufficient funds for that withdraw')
```

---

## Example - View - Logout Message 
* And finally a logout message.
```
def logout_screen():
    print('See you later!')
```

---

## Example - Controller
* Now we move on to the controller. Really there are 2 loops for this application. The logon loop and the account loop.
* In the logon loop the app asks the user if they want to create an account, login, or exit. It needs to be a loop because the user might type their pin wrong and needs multiple attempts. It is also a loop because after a logged in user logs out, they should return to the logon screen.
* The account loop is where the user goes after they have either logged in or just created an account. Here the app asks if they want to see their balance, deposit, withdraw, or logout. It is a loop because the user might want to do many things while they are logged in (for example check balance, deposit, check balance, logout).
* So the overall structure will be a `logon_loop` that runs indefinitely until exit, and an `account_loop` that is called by the `logon_loop` so that when it returns we are back in the `logon_loop`.

---

## Example - Controller - Setup
* Before we start the `logon_loop` and `account_loop` make sure to import the `Account` class from `model` and the `view` module.
* Create a file `ttrader/controller.py` with the following:  

```
from model import Account
import view

def logon_loop():
    pass

def account_loop(acct): # takes in an account object
    pass
```

---

## Example - Controller - Logon Loop
* In `ttrader/controller.py` the `logon_loop` needs to show the logon screen and handle the user's choice. We want this to loop until the user exits (`3`).
* The other options should call `account_loop` passing in the account object.
```
def logon_loop():
    choice = None
    while choice != '3':
        choice = views.logon_prompt()
        if choice == '1':
            [name, pin] = views.new_user_prompt()
            acct = Account.new(name, pin)
            account_loop(acct)
        if choice == '2':
            [acct_num, pin] = views.login_prompt()
            acct = Account.login(acct_num, pin)
            if acct != None:
                account_loop(acct)
            else:
                views.login_fail()
```

---

## Example - Controller - Account Loop
* Similar to `logon_loop`, the `account_loop` needs to keep getting and handling the user's choice until they choose to logout (option `4`).
```
def account_loop(acct):
    choice = None
    while choice != '4':
        choice = views.account_prompt()
        if choice == '1':
            views.display_balance(acct)
        if choice == '2':
            amount = model.deposit_prompt()
            acct.deposit(amount)
        if choice == '3':
            amount = model.withdraw_prompt()
            # if the withdraw fails, display not enough
            if not acct.withdraw(amount):
                views.display_not_enough()
    views.logout_screen() # say bye
```

---

## Example - Running it
* Lastly we want to setup a `main.py` so we can run our app with `python3 main.py`
* We will need `main.py` to do 2 things: `load` the model data and start the controller's `logon_loop`
```
import model
import controller
# initially load the saved data
models.load()
# start the logon_loop to get everything working
controller.logon_loop()
```
* That's it! Play around with Terminal Teller and make those fixes as exercises. 
