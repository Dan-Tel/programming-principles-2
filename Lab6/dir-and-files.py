import os

# 1. Write a Python program to list only directories, files and all directories, files in a specified path.
def list_dir_and_files(path):
  dir_and_files = os.listdir(path)
  only_dir = list(filter(lambda x : os.path.isdir(x), dir_and_files))
  only_files = list(filter(lambda x : os.path.isfile(x), dir_and_files))

  print("Only directories:", only_dir, sep="\n", end="\n\n")
  print("Files and all directories:", dir_and_files, sep="\n", end="\n\n")
  print("Only files:", only_files, sep="\n")

# 2. Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
def check_for_access(path):
  print("Existence:", os.access(path, os.F_OK))
  print("Readability:", os.access(path, os.R_OK))
  print("Writability:", os.access(path, os.W_OK))
  print("Executability:", os.access(path, os.X_OK))


# 3. Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
def check_path(path):
  if os.access(path, os.F_OK):
    directory, filename = os.path.split(path)
    print("Filename:", filename)
    print("Directory:", directory)
  else:
    print("The path does not exist")

# 4. Write a Python program to count the number of lines in a text file.
def number_of_lines(path):
  f = open(path)
  print(len(f.readlines()))
  f.close()

# 5. Write a Python program to write a list to a file.
def write_list(l, path):
  f = open(path, "w")
  f.write(str(l))
  f.close()

# 6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
def generate_files(path):
  for i in range(65, 65 + 26):
    f = open(os.path.join(path, f"{chr(i)}.txt"), "w")

# 7. Write a Python program to copy the contents of a file to another file
def copy_files(base_path, target_path):
  base = open(base_path)
  target = open(target_path, "w")
  target.write("".join(base.readlines()))
  base.close()
  target.close()

# 8. Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
def delete_file(path):
  if os.access(path, os.F_OK):
    os.remove(path)
  else:
    print("The path does not exist")