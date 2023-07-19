def hello():
    name = input("Name: ")
    print("Hello " + name)
hello()

a = int(input("A"))
b = int(input("B"))
def sum(a, b):
    return a + b
c = sum(a, b)
d = 2
e = sum(c, d)
print(e)

def duplicates(a, b, c, d):
    list = [a, b, c, d]
    for i in list:
        while list.count(i) > 1:
            list.remove(i)
    return list

def calc(a, b):
    sum = a + b
    sub = a - b
    mult = a * b
    div = a / b
    return sum, sub, mult, div
print(calc(3,5))

def list(*args):
    for i in args:
        print(i)
list(10, 20)

def bye(name, age = 1004):
    print("bye" + name)
    print(str(age) + "years old")
bye(name = "Yena", age = 1004)

def outer_fun(a,b):
    square = a ** 2
    def addition(a, b):
        return a + b
    add = addition(a, b)
    return add +7
print(outer_fun(4, 6))

def 이하은남친(verb, age = 14):
    print("이하은남친" + verb)
    print(str(age) + "years old")
이하은남친(verb = "has girlfriend", age = 14)