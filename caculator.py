print("Welcome to Jenny's caculator/n")

# get x and y from users
# define as integer
variable = int(input("What is your first number?"))
variable = int(input("What is your second number?"))

# get add, subtract, multiply or divide
math = input("What would you like to do with these numbers")

#if add, subtract, muntiply, or divide, computer answer
if math == "add":
    print(x + y)
if math == "subtract":
    print(x - y)
if math == "multiply":
    print(x * y)
if math == "divide":
    print(x / y)

    x = 5
    for i in range(3):
        x = x +1