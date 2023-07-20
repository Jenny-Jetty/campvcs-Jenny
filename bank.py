greeting = input("Greeting: ")

def bank(greeting):
    if greeting == "hello":
        print("$0")
    elif greeting == "hey":
        print("$100")   
    else:
        print("$20")
bank(greeting)