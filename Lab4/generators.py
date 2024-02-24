# 1. Create a generator that generates the squares of numbers up to some number N.
def generate_squares(N):
  for i in range(1, N + 1):
    yield i ** 2

# 2. Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def generate_even(n):
  for i in range(0, n + 1, 2):
    yield i

print(*generate_even(int(input())), sep=",")

# 3. Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def generate_divisible(n):
  for i in range(0, n + 1, 12):
    yield i

# 4. Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
  for i in range(a, b + 1):
    yield i ** 2

for i, square in enumerate(squares(int(input()), int(input()))):
  print(square)

# 5. Implement a generator that returns all numbers from (n) down to 0.
def generate_decrement(n):
  for i in range(n, -1, -1):
    yield i