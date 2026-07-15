# mytext = 'this is an example text for the lecture technology of circular economy!'
# First, we read text from a file, instead of typing it into the program

myin = open('input-caesar.txt', 'r')  # open a text file in read modus
mytext = myin.read()    # here, we read the entire file into the string
myin.close()

# Finished reading from file. Now start to encode.

alorg = 'abcdefghijklmnopqrstuvwxyz'
shift = 3   # shift parameter
m = ' !' # non-letter characters in text
alnew = alorg[shift:]
b = alorg[:shift]

alnew = alnew + b + m
alorg = alorg + m
newtext = ''

for a in mytext:
    # inside this loop, 'a' contains the next letter from the text
    # now, find the letter in the original alphabet
    x = 0
    for b in alorg:
        if b == a:   # letter found at position x
            newtext = newtext + alnew[x]  # new text uses same position in the shifted alphabet
        x = x + 1
        
# print(newtext)
# Instead of printing, we write the result into a file.

myout = open('output-caesar.txt', 'w')  # open a text file in write modus
myout.write(newtext)    # Here, we write the string into the file.
myout.close()
