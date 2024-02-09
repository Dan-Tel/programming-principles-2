# 1. Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
class StringClass:
  def getString(self):
    s.string = input()
  
  def printString(self):
    print(s.string.upper())

# 2. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
class Shape:
  def area(self):
    print(0)

class Square(Shape):
  def __init__(self, length):
    self.length = length
  
  def area(self):
    print(self.length ** 2)

# 3. Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.
class Rectangle(Square):
  def __init__(self, length, width):
    super().__init__(length)
    self.width = width
  
  def area(self):
    print(self.length * self.width)

# 4. Write the definition of a Point class. Objects from this class should have a
#    - a method show to display the coordinates of the point
#    - a method move to change these coordinates
#    - a method dist that computes the distance between 2 points
class Point:
  def __init__(self):
    self.coordinates = [0, 0]

  def show(self):
    print(self.coordinates)

  def move(self, x, y):
    self.coordinates[0] = x
    self.coordinates[1] = y

  def dist(self):
    x, y = self.coordinates[0], self.coordinates[1]
    print((x ** 2 + y ** 2) ** (1/2))

# 5. Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
class Account:
  def __init__(this, owner, balance):
    this.owner = owner
    this.balance = balance
  
  def deposit(this, money):
    this.balance += money
    print(f"DEPOSIT: {money}  CURRENT: {this.balance}")
  
  def withdraw(this, money):
    if this.balance - money < 0:
      print("Sorry, you are going to withdraw more than you have on your balance")
      return
    
    this.balance -= money
    print(f"WITHDRAW: {money}  CURRENT: {this.balance}")

account = Account("Daniyar", 0)
account.deposit(5) #    DEPOSIT: 5  CURRENT: 5
account.deposit(50) #   DEPOSIT: 50  CURRENT: 55
account.withdraw(5) #   WITHDRAW: 5  CURRENT: 50
account.withdraw(500) # Sorry, you are going to withdraw more than you have on your balance
account.withdraw(5) #   WITHDRAW: 5  CURRENT: 45

# 6. Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.
import math

x = []
for i in range(1, 101):
  x.append(i)

filter_primes = list(filter(lambda n : not any(n % i == 0 for i in range(2, math.ceil(math.sqrt(n)) + 1)), x))

print(*filter_primes) # 1 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97