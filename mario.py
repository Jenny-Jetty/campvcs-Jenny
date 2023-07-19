# get the height from the user
# make height into an integer

# for i in range(height)
# start with 7 spaces and 1 hash

h = int(input("Height"))

for i in range(1,h+1):
    print(i)

for i in range(1,h+1):
    print(" "*(h-i)+"#"*i)