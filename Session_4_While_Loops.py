#============While Loops============

i = 0
while i < 10:
    print(i)
    i = i + 1
    #i += 1

##

j = 0
while j > 10:
    print(j)
    j += 1

# ============While True============

while True:
    print("This will print forever")

##

while 1==1:
    print("This will print forever")

##

while 1 < 2:
    print("This will print forever")

# ============While False============

while False:
    print("This will not print")

##

while 1 > 2:
    print("This will not print")

# ============While with else============
i = 0
while i < 10:       # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    print(i)
    i += 1
else:
    print("i is no longer less than 10")

# ============While with String ============

name = "faze"
i = 0               # f a z e
while i < len(name):
    print(name[i])
    i += 1

# ============While with List ============

names_list = ["faze", "abdo", "malek", "himaa", "yousef"]
i = 0
while i < len(names_list):
    print(names_list[i])
    i += 1

# ============While with Tuple ============
numbers_tuple = (1,2,3,4,5)
i = 0
while i < len(numbers_tuple):
    print(numbers_tuple[i])
    i += 1

# ============While with Dictionary ============
names_dict = {"faze": 1,
              "abdo": 2,
              "malek": 3,
              "himaa": 4,
              "yousef": 5}
i = 0
while i < len(names_dict):
    print(names_dict[i])
    i += 1

# ============While with sets============

names_set = {"faze", "abdo", "malek", "himaa", "yousef"}
i = 0
while i < len(names_set):
    print(names_set[i])
    i += 1

# ============While with if============

i = 0
while i < 10:
    if i == 5:
        print("i is 5")
    print(i)
    i += 1

# ============While with if and break============

i = 0
while i < 10:       # 0, 1, 2, 3, 4, 5
    print(i)
    if i == 5:
        break
    i += 1


##

i = 0
while i < 10:
    if i == 5:
        print("i is 5")
        break
    print(i)
    i += 1


##

i = 0
while i < 10:           # 0, 1, 2, 3, 4, 5
    print(i)
    if i == 5:
        break
    i += 1
else:
    print("i is no longer less than 10")

# ============While with if and continue============

i = 0
while i < 10:       # 0, 1, 2, 3, 4, 6, 7, 8, 9
    i += 1
    if i == 5:
        continue
    print(i)

##

i = 0
while i < 10:           # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    i += 1
    if i == 5:
        continue
    print(i)
else:
    print("i is no longer less than 10")

##

# ============While with try============
i = 0
while i < 10:
    try:
        print(i)
        i += 1
    except:
        print("An error occurred")
        break

##

try:
    i = 0
    while i < 10:
        print(i)
        i += 1
except:
    print("An error occurred")


# ============Examples============

correct_username = "faze"
correct_password = "faze._11"

entered_username = input("Enter your username: ").lower()
entered_password = input("Enter your password: ")

if entered_username == correct_username and entered_password == correct_password:
    print(f"""
    Access granted
    Welcome to the system, {correct_username.capitalize()}
    """)
else:
    print("Access denied")
    print("Please try again")


##

correct_username = "faze"
correct_password = "faze._11"

while True:
    try:
        entered_username = input("Enter your username: ").lower()
        entered_password = input("Enter your password: ")

        if entered_username == correct_username and entered_password == correct_password:
            print(f"""
            Access granted
            Welcome to the system, {correct_username.capitalize()}
            """)
            break
        else:
            print("Access denied")
            print("Please try again")
            print()
    except Exception as e:
        print(f"An error occurred: {e}")
        break


##

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

print(f"The result is: {result}")


##

while True:
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."
        else:
            result = "Invalid operator!"

        print(f"The result is: {result}")

        another = input("Do you want to perform another calculation? (yes/no): ").lower()
        print()
        if another != 'yes':
            break

    except ValueError:
        print("Invalid input! Please enter numeric values for numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")


