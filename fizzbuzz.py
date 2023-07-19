x = int(input("Number"))

def fizzbuzz(x):
    if x % 3 == 0 and x % 5 ==0:
        print("fizzbuzz")
    elif x % 5 == 0:
        print("buzz")

fizzbuzz(x)