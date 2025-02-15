s = "hello"
print(dir(s)) # list of methods
useful_methods = [m for m in dir(s) if "__" not in m]
print(useful_methods)

print(help(s.capitalize))
print(s.capitalize())

print("HELLO".casefold()) # same as .lower()
print("hello".center(50, "*"))

print("I see a little dove".count("e")) # how many times does "e" appear
print("bananananananananana".count("ana"))
x = "I don't cook nor complain"
print(f"There are {x.count("o")} o's inside '{x}'")
print("hello".find("l")) # tells you position of letter at lowest index
print("hello0000000oooooollloooo".find("l", 10)) # after position 10

s = "bob goes home to meet bob so they can take their bob and go bobing"
pos = 0
while True:
    start = s.find("bob", pos)
    if start == -1:
        break
    print("found bob on position", start)
    pos = start + 1

# index is weaker than find - tells you first index
# join - creates string out of a list

items = ["cat", "rat", "mouse", "house"]
print(" ".join(items)) # takes a filler first
print("I LIKE to got HIKIng".lower().upper())
print("I like to go skiing".title())
# replace - replaces item w/ item inside the string
print("I like to go skiing".replace("i", "1").replace("e", "3"))

# split - makes a list of the string by splitting by the delimiter
print("I like to skiing".split(" "))