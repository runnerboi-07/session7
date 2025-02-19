# Q1 - What does the code print
hi = "Hello"
who = "World"
print(hi + " " + who)
# Concatenates the two strings with a space in between

print(hi + who[:3] + who[4:])
# Prints hi; prints characters 0, 1 and 2 of who and then only the last (4th) character

print(hi + " " + who[:3] + who[4:])
# Same as before, but with the space added in the string

print((hi + who).upper())
# No space and all upper case

print("racecar"[::-1])
# Prints the text in reverse; inverts the text

print((3 * (hi + " ") + 5 * (who + ",")).replace(","," ").split(" "))
# Prints 3 'Hello' and 5 'World'; the World initially had a comma, but these are replaced with spaces; Turned into a list using .split(); One empty entry at the end
print(['Hello', 'Hello', 'Hello', 'World', 'World', 'World', 'World', 'World', ''])

# Q2 - Read a string. Check if the string is a palindrome. First remove all punctuation marks. The check should be case insensitive.
# Test with: “Yo, banana boy!” “A nut for a jar of tuna.”
punctuation = ";:,.'!?-=()/"
words = str(input("Input your text: "))

checker = [] # Empty list to add new text without punctuations
for word in words.lower():
    if word in punctuation:
        word = ""
        checker.append(word)
    else:
        checker.append(word)
checker = " ".join(checker)
checker = checker.replace(" ", "")

# Testing checker after inverting text
if checker == checker[::-1]:
    print("This text is a palindrome")
else:
    print("Not a palindrome")



