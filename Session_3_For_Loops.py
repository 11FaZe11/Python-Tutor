
# Loops in Python

# ============For Loops (String)============
name = "faze"

for i in name:
    print(i)            # print the characters of the string


# ============For Loops (Range)============
for i in range(5):
    print(i)  # print the values of the range


for i in range(1, 5):
    print(i)  # print the values of the range   # 1, 2, 3, 4


for i in range(1, 10, 2):
    print(i)  # print the values of the range   # 1, 3, 5, 7, 9


for i in range(10, 1, -2):
    print(i)  # print the values of the range   # 10, 8, 6, 4, 2


# ============For Loops (List)============
numbers_list = [1,2,3,4,5]

for i in numbers_list:
    print(i)        # print the values of the list  # 1, 2, 3, 4, 5


for i in range(numbers_list):   # Error because range() function takes an integer as an argument
    print(i)


for i in range(len(numbers_list)):  # Fix for the above error
    print(i)



names_list = ["faze", "abdo", "malek", "himaa", "yousef"]

for i in names_list:    # print the values of the list
    print(i)

# ============For Loops (Tuple)============

numbers_tuple = (1,2,3,4,5)

for i in numbers_tuple:     # print the values of the tuple
    print(i)


# ============For Loops (Dictionary)============
names_dict = {"faze": 1,
              "abdo": 2,
              "malek": 3,
              "himaa": 4,
              "yousef": 5}

for i in names_dict:
    print(i)        # print the keys of the dictionary


for i in range(names_dict):
    print(i)        # Error because range() function takes an integer as an argument


for i in names_dict.keys():
    print(i)        # print the keys of the dictionary


for i in names_dict:
    print(names_dict.get(i))        # print the values of the dictionary


for i in names_dict:
    print(names_dict.values())      # print the values of the dictionary


for i in names_dict:
    print(names_dict[i])            # print the values of the dictionary


for i in names_dict.values():
    print(i)                        # print the values of the dictionary

#.....................................................

for i in names_dict.items():
    print(i)                # print the key and value of the dictionary


#.......................bonus..............................
for i in names_dict.items():
    print(i[0])     # bonus         # print the key of the dictionary


for i in names_dict.items():
    print(i[1])     # bonus         # print the value of the dictionary


for i in names_dict.items():
    print(i[0], i[1])     # bonus       # print the key and value of the dictionary


for i, j in names_dict.items():
    print(i, j)     # bonus             # print the key and value of the dictionary


for i, j , x in names_dict.items():
    print(i, j)     # bonus             # Error because the number of variables is more than the number of items in the dictionary



# ============For Loops (sets)============

names_set = {"faze", "abdo", "malek", "himaa", "yousef"}

for i in names_set:
    print(i)            # print the values of the set


for i in range(names_set):   # Error because range() function takes an integer as an argument
    print(i)
# ============For Loops (Nested)============

# Define the dimensions of the rectangle

width_reg = 10
height_reg = 5

# Loop through each row in the rectangle
for i in range(height_reg):
    # Loop through each column in the current row
    for j in range(width_reg):
        print("@", end=" ")
    # Print a new line after each row
    print()

base_triangle = 10  # Define the base width of the triangle
height_triangle = 10  # Define the height of the triangle

# Print a right-angled triangle
for i in range(height_triangle):  # Loop through each row
    for j in range(i + 1):  # Loop through each column in the current row
        print("@", end=" ")  # Print @ symbol without a newline
    print()  # Print a newline after each row


# Print an equilateral triangle
for i in range(height_triangle):  # Loop through each row
    for j in range(height_triangle - i - 1):  # Print leading spaces
        print(" ", end=" ")
    for j in range(i + 1):  # Print @ symbols
        print("@", end=" ")
    print()  # Print a newline after each row


# Print an inverted right-angled triangle
for i in range(height_triangle, 0, -1):  # Loop through each row in reverse
    for j in range(height_triangle - i):  # Print leading spaces
        print(" ", end=" ")
    for j in range(i):  # Print @ symbols
        print("@", end=" ")
    print()  # Print a newline after each row


# Print an inverted equilateral triangle
for i in range(height_triangle, 0, -1):  # Loop through each row in reverse
    for j in range(height_triangle - i):  # Print leading spaces
        print(" ", end=" ")
    for j in range(2 * i - 1):  # Print @ symbols
        print("@", end=" ")
    print()  # Print a newline after each row


# Print an equilateral triangle with the apex in the middle
for i in range(height_triangle):  # Loop through each row
    for j in range(height_triangle - i):  # Print leading spaces
        print(" ", end=" ")
    for j in range(2 * i - 1):  # Print @ symbols
        print("@", end=" ")
    print()  # Print a newline after each row




# ============For Loops with If ============

number = int(input("Enter a number to show the odd and even numbers below it: "))

for i in range(number):
    if i % 2 == 0:      # if i is divisible by 2
        print(i)


for i in range(number):
    if i % 2 != 0:      # if i is not divisible by 2
        print(i)



for i in range(number):
    if i % 2 == 0:
        print(f"{i} is even")       # print the even numbers    # 0, 2, 4, 6, 8
    else:
        print(f"{i} is odd")        # print the odd numbers     # 1, 3, 5, 7, 9


###########add try and except################

try:
    number = int(input("Enter a number to show the odd and even numbers below it: "))

    for i in range(number):
        if i % 2 == 0:
            print(f"{i} is even")       # print the even numbers    # 0, 2, 4, 6, 8
        else:
            print(f"{i} is odd")        # print the odd numbers     # 1, 3, 5, 7, 9
except ValueError:
    print("Please enter a valid integer.")      # print an error message if the user enters a non-integer value


# ============For loops and pass break and continue ==============

for i in range(10):
    pass    # do nothing


for i in range(10):
    if i == 5:  # if i == 5, break the loop
        break
    print(i)


for i in range(10):
    if i == 5:   # skip the number 5
        continue
    print(i)
