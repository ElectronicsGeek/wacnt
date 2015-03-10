from string import ascii_lowercase

# String to decrypt
string = "tqnm qa tqsm i pczzqkivm"

def caesar(rot, s):
    
    outstr = "" # Sentry variable
    s = s.lower()

    for char in s:
        if char == " ":
            outstr += " "

        position = ascii_lowercase.find(char)
        
        # '.find(x)' returns -1 if it can't find 'x'
        if position != -1:

            # Modulo used to 'wrap around' if the index yielded is
            # greater than 26.
            slice = (position + rot) % len(ascii_lowercase)

            outstr += ascii_lowercase[slice]

    return outstr

# Iterate through all possible 'rotations'
for n in range(26):
    print "ROT-" + str(n) + ": " + caesar(n, string)       

### ANSWER:
# life is like a hurricane
