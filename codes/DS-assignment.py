import os

def sort_integers(list): # function to sort algorithm
  size = len(list) # find the size of list
  for val in range (size):
    smallest = val   #set the first value to be the smallest
    for j in range(val+1, size):
      if list[j]<list[smallest]:
        smallest = j
    list[val], list[smallest]=list[smallest],  list[val]   # swap positions if any value smaller than smallest
  print("Integers Sorted")


def create_result(list, file): #this function is to print results
  folder_path='../sample_results'
  file_name=os.path.splitext(file)[0]+"_result.txt"
  print(file_name)
  file_path=os.path.join(folder_path,file_name)

  file = open(file_path, 'w') 
  for item in list:
      file.write(str(item)+"\n")
  file.close()
  print("Result Printed")


def find_integers_in_files(directory):  #This function reads text files in a directory, extracts integers from each line, and stores them in a list.
  for filename in os.listdir():
    if filename.endswith(".txt"):  # Check if the file is a text file
      print(filename)
      integers=[]
      filepath = os.path.join(directory, filename)
      with open(filepath, 'r') as f:
        for line in f:
          # Split the line into words
          words = line.split()
          c=0
          for word in words:
            # Try converting the word to an integer
            try:
              integer = int(word)
              if integer in integers:
                continue
              else:
                c+=1
                if c>1:
                  integers.pop()
                  break
                integers.append(integer)
            except ValueError:
              pass  # Ignore non-integer strings

      sort_integers(integers)
      print(integers)
      create_result(integers,filename)

# Get to the current directory
os.chdir('/ds-ssignment/codes')

directory = '../sample_inputs'
print("I surely passed here first")


# Find integers in text files
find_integers_in_files(directory)

