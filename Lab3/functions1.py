# 1. A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams
def grams_to_ounces(grams):
  return 28.3495231 * grams

# 2. Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)
def centigrade(fahrenheit):
  print((5 / 9) * (fahrenheit - 32))

# 3. Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
def solve(numheads, numlegs):
  numrabbits = int((numlegs - 2 * numheads) / 2)
  numchickens = int(numheads - numrabbits)
  print(f"There are {numrabbits} rabbits and {numchickens} chickens")

# 4. You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
def filter_prime(list_str):
  l = list(map(lambda x : int(x), list_str.split(" ")))

  def is_prime(n):
    for i in range(2, int(n ** (1 / 2) + 1)):
      if n % i == 0:
        return False
    return True
  
  primes = []
  for n in l:
    if is_prime(n):
      primes.append(n)
  
  return primes

# 5. Write a function that accepts string from user and print all permutations of that string.
import itertools

def string_permutation(string):
  return list(map(lambda x : "".join(x), list(itertools.permutations(string))))
  
# 6. Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We
def reverse_string(string):
  print(" ".join(string.split(" ")[::-1]))

# 7. Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 3 and nums[i + 1] == 3:
      return True
  return False

# 8. Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
  modified_nums = []
  for n in nums:
    if n == 0 or n == 7:
      modified_nums.append(n)

  for i in range(len(modified_nums) - 2):
    if modified_nums[i] == 0 and modified_nums[i + 1] == 0 and modified_nums[i + 2] == 7:
      return True
  return False

# 9. Write a function that computes the volume of a sphere given its radius.
def sphere_volume(radius):
  return 4 / 3 * 3.14 * (radius ** 3)

# 10. Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
def unique_list(list):
  new_list = []
  for n in list:
    if new_list.count(n) == 0:
      new_list.append(n)
  return new_list

# 11. Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def check_palindrome(string):
  return string == string[::-1]

# 12. Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******
def histogram(list):
  for n in list:
    print("*" * n)

# 13. Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
import random
def guess_the_number():
  print("Hello! What is your name?")
  name = input()

  print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
  print("Take a guess.")

  num = random.randrange(1, 20)
  counter = 1
  guess = int(input())

  while guess != num:
    if guess < num:
      print("\nYour guess is too low.")
      print("Take a guess.")
      guess = int(input())
    else:
      print("\nYour guess is too high.")
      print("Take a guess.")
      guess = int(input())
    counter += 1
  print(f"\nGood job, {name}! You guessed my number in {counter} guesses!")