"""
This is an example for text decryption - for the lecture 'Modelling and Simulation'
This version takes an encrypted message (Caesar shift, lower case and capital letters) 
and applies every possbile shift (26). Output is written to a text file.
First, we read text from a file, instead of typing it into the program.

Uwe Reimer, Emden, October 2025
"""

infile = "message2.txt"
outfile = "out-message2.txt"


myin = open(infile, 'r')  # open a text file in read modus
mytext = myin.read()    # here, we read the entire file into the string
myin.close()

newtext = ''

def mydec(mytext, shift):
    # This is a function to dencode text.
    global newtext
    
    alorg = 'abcdefghijklmnopqrstuvwxyz'
    m = ' .,?!' # non-letter characters in text
    # First, we shift the positions
    alnew = alorg[shift:]
    b = alorg[:shift]
    alnew = alnew + b 
    alorg = alorg
    
    # Here, we add the second alphabet in capital letters
    # The simple way: alorg2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alorg2 = alorg.swapcase()   # this functions swaps the letters
    
    # Now, we repeat the shifting in position
    alnew2 = alorg2[shift:]
    b = alorg2[:shift]
    alnew2 = alnew2 + b
    
    # Finally, we add the non letter characters to the small alphabet
    alnew = alnew + m
    alorg = alorg + m
    
    for a in mytext:
        # inside this loop, 'a' contains the next letter from the text
        # We created a small and capital alphabet. For decryption we need to test, if the character is small or capital and search in the respective alphabet
        if a.isupper():
            x = 0
            for b in alorg2:             
                if b == a:   # letter found at position x
                    newtext = newtext + alnew2[x]  # new text uses same position in the shifted alphabet
                x = x + 1
        
        else:           # search in lower case alphabet (this also includes non letter characters)  
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
