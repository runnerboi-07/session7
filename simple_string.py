s1 = "banana"
s2 = 'banana'
print(s1, s2)
s1 = 'And John asked: "How are you?". "I\'m good"' # \ to escape; to use delimiter same as string delimiter
print(s1)
s1 = "I can print \""
print(s1)

# indexing starts from zero
s = "0123456789"
print(s[1], s[7], s[9])
print(s[-1], s[-4])
print(f"The length is {len(s)}") # len() to find length
