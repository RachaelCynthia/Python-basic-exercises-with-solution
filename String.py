word = input("Enter a word to be reverse: ")

# program to check whether the string is Symmetrical or Palindrome
stringLen = len(word)
if stringLen % 2 == 0:
    firstString = word[0:stringLen // 2]
    secondString = word[stringLen // 2:]
    # print("String First Half :", firstString)
    # print("String Second Half:", secondString)
else:
    firstString = word[0:(stringLen // 2 + 1)]
    secondString = word[(stringLen // 2 + 0):]
    # print("First Half :", firstString)
    # print("Second Half :", secondString)

if firstString == secondString:
    print("Word enter is symmentrical")  #These are the ones which if you draw a line through the word on the vertical axis, both sides look identical
elif firstString == ("".join(reversed(secondString))):
    print("Word enter is Palindrome")  #A palindrome is spelled the same forward and backward
else:
    print("Word enter is neither symmentrical nor Palindrome")

# Reverse words in a given String
my_word = reversed(word)
print("".join(my_word))


# Ways to remove i’th character from string
def remove_char(s, i):

    for j in range(len(s)):
        if j==i:
            s=s.replace(s[i],"",1)
    return s
i = 2
print(remove_char(word,i-1))

#Find length of a string in python (4 ways)
print(len(word))  #Using function len

w = 0     #Using enumerate function
for i, a in enumerate(word):
    w += 1
print(w)

# program to print even length words in a string
word1 = "My father and mother are the best"
w = word1.split(" ")
for i in w:
    if len(i)%2 == 0:
        print(i)
