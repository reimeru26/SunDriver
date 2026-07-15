"""
This is an example for text decryption - for the lecture 'Modelling and Simulation'
This version takes an encrypted message (Caesar shift, lower case alphabet only) 
and applies every possbile shift (26). Output is written to a text file.
First, we read text from a file, instead of typing it into the program.

Uwe Reimer, Emden, October 2025
"""

infile = "message1.txt"
outfile = "out-message1.txt"

myin = open(infile, 'r')  # open a text file in read modus
mytext = myin.read()    # here, we read the entire file into the string
myin.close()

newtext = ''

def mydec(mytext, shift):
    # This is  a function to dencode text.
    global newtext
    
    alorg = 'abcdefghijklmnopqrstuvwxyz'
    m = ' !' # non-letter characters in text
    alnew = alorg[shift:]
    b = alorg[:shift]

    alnew = alnew + b + m
    alorg = alorg + m
    
    for a in mytext:
        # inside this loop, 'a' contains the next letter from the text
        # now, find the letter in the original alphabet
        x = 0
        for b in alorg:
            if b == a:   # letter found at position x
                newtext = newtext + alnew[x]  # new text uses same position in the shifted alphabet
            x = x + 1

shift = 1

while shift < 26:
    newtext = newtext + str(shift) + ' \n'  # here, we add the number and a special character (newline)
    mydec(mytext, (-1) * shift )
    shift = shift + 1
    newtext = newtext + '\n  -----------------------  \n'  # we add two more newline to better read the results


myout = open(outfile, 'w')  # open a text file in write modus
myout.write(newtext)    # Here, we write the string into the file.
myout.close()
