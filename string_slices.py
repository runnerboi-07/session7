s = "0123456789"
print(s)
print(s[1:2]) # first index is included, last index is excluded
print(s[4:7])
print(s[0:7]) # if you omit first index, it starts from the beginning
s = "I go to school early in the morning"
print(s[:20])
print(s[20:])# includes all till the end

print(s[:]) # the whole thing
print(s[::2]) # every second character; step of two
print(s[::-1]) # negative index reverts string
print("racecar"[::-1])
s = "Was it a car or a cat I saw?"
print(s.lower())
print(s[::-1])
