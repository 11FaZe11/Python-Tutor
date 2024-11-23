# ============Ints============

x_int = 42      # int

y_int = -73     # int

print(x_int)    # 42

print(y_int)    # -73


################################################################


# ============Floats============

x_float = 42.0    # float

y_float = 73.0    # float

print(x_float)    # 42.0

print(y_float)    # 73.0


################################################################


# ============Sting============

x_sting = "Hello"     # str

y_sting = 'World'     # str

print(x_sting)        # Hello

print(y_sting)        # World

print(x_sting + " " + y_sting)    # Hello World

print(x_sting, y_sting)           # Hello World

print(f"{x_sting} {y_sting}")     # Hello World

print(x_sting + y_sting)          # HelloWorld


################################################################


# ============Boolean============


x_boolean = True    # bool

y_boolean = False   # bool

print(x_boolean)    # True

print(y_boolean)    # False


################################################################


# ============List============


x_list = [1, 2, 3, 4, 5]    # list

y_list = ["Hello", "World"]  # list

print(x_list)    # [1, 2, 3, 4, 5]

print(y_list)    # ['Hello', 'World']

print(x_list[0])    # 1

print(y_list[1])    # World

print(x_list[1:3])    # [2, 3]

print(y_list[0:2])    # ['Hello', 'World']

print(x_list + y_list)    # [1, 2, 3, 4, 5, 'Hello', 'World']


# ============List Operations============


# Creating a list
my_list = [1, 2, 3, 4, 5]

# Append: Add an element to the end of the list
my_list.append(6)
print(my_list)  # [1, 2, 3, 4, 5, 6]

# Extend: Add all elements of a list to the end of the list
my_list.extend([7, 8])
print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8]

# Insert: Insert an element at a specific position
my_list.insert(0, 0)
print(my_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Remove: Remove the first occurrence of an element
my_list.remove(3)
print(my_list)  # [0, 1, 2, 4, 5, 6, 7, 8]

# Pop: Remove and return an element at a specific position (default is the last element)
popped_element = my_list.pop()
print(popped_element)  # 8
print(my_list)  # [0, 1, 2, 4, 5, 6, 7]

# Clear: Remove all elements from the list
my_list.clear()
print(my_list)  # []

# Index: Return the index of the first occurrence of an element
my_list = [1, 2, 3, 4, 5]
index = my_list.index(3)
print(index)  # 2

# Count: Return the number of occurrences of an element
count = my_list.count(3)
print(count)  # 1

# Sort: Sort the list in ascending order
my_list.sort()
print(my_list)  # [1, 2, 3, 4, 5]

# Reverse: Reverse the elements of the list
my_list.reverse()
print(my_list)  # [5, 4, 3, 2, 1]

# Copy: Return a shallow copy of the list
my_list_copy = my_list.copy()
print(my_list_copy)  # [5, 4, 3, 2, 1]


# ============Tuple============


x_tuple = (1, 2, 3, 4, 5)    # tuple

y_tuple = ("Hello", "World")  # tuple

print(x_tuple)    # (1, 2, 3, 4, 5)

print(y_tuple)    # ('Hello', 'World')

print(x_tuple[0])    # 1

print(y_tuple[1])    # World

print(x_tuple[1:3])    # (2, 3)

print(y_tuple[0:2])    # ('Hello', 'World')

print(x_tuple + y_tuple)    # (1, 2, 3, 4, 5, 'Hello', 'World')


# ============Dictionary============


x_dict = {
    "name": "Abdo",
    "age": 18,
}    # dict

y_dict = {
    "name": "Malek",
    "age": 8,
}    # dict

print(x_dict)    # {'name': 'Abdo', 'age': 18}

print(y_dict)    # {'name': 'Malek', 'age': 8}

print(x_dict["name"])    # Abdo

print(y_dict["age"])    # 8

print(x_dict.keys())    # dict_keys(['name', 'age'])

print(y_dict.values())    # dict_values(['Malek', 8])

print(x_dict.items())    # dict_items([('name', 'Abdo'), ('age', 18)])



# ============Set============ Advanced



# # ============If============


x_if = int(input("Enter a number: "))

if x_if > 5:
    print("x_if is greater than 5")

elif x_if == 5:
    print("x_if is equal to 5")

elif x_if == 6:
    print("x_if is less than 6")

else:
    print("x_if is less than 5")


# ============If with or and not ============


y_if = int(input("Enter a number: "))

if y_if > 5 or y_if < 15:
    print("y_if is greater than 5 or less than 15")

elif not y_if == 5:
    print("y_if is not equal to 5")

elif y_if > 10 and y_if >0:
    print("y_if is greater than 10 and greater than 0")

else:
    print("y_if is equal to 5")


# ============Nested If============


z_if = int(input("Enter a number: "))

if z_if > 5:
    if z_if > 10:
        print("z_if is greater than 10")
    else:
        print("z_if is less than 10 but greater than 5")



# ============Switch============


argument = int(input("Enter a number: "))

switcher = {
    0: "Zero",
    1: "One",
    2: "Two",
}

print(switcher.get(argument, "Invalid number"))



# ============Calculator============


print("""Select operation: 
1. Add")
2. Subtract)
3. Multiply)
4. Divide)
5. Power""")

choice = input("Enter choice (1/2/3/4/5): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif choice == '2':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif choice == '3':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error! Division by zero.")

elif choice == '5':
    result = num1 ** num2
    print(f"{num1} ^ {num2} = {result}")
else:
    print("Invalid input")