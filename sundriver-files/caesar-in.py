mytext = 'this is an example text for the lecture technology of circular economy!'
alorg = 'abcdefghijklmnopqrstuvwxyz'
# shift = 3
alnew = 'defghijklmnopqrstuvwxyzabc'

alorg = alorg + ' !'
alnew = alnew + ' !'

newtext = ''

for a in mytext:
    # inside this loop, 'a' contains the next letter from the text
    # now, find the letter in the original alphabet
    x = 0
    for b in alorg:
        if b == a:   # letter found at position x
            newtext = newtext + alnew[x]  # new text uses same position in the shifted alphabet
        x = x + 1
        
print(newtext)



