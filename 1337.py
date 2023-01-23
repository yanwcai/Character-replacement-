

# BTW, LOL, OMG, FYI, AFAIK
# by the way, laughing out loud, oh my god, for your information
# as far as i know
import string
        
def toacronyms(s):
    for i in range(len(s)-1):
        if s[i] == "B":
            if s[i:i+10] == "BY THE WAY":
                s = s[:i]+"BTW"+s[i+10:]
                return s
        else:
            if s[i] == "L":
                 if s[i:i+17] == "LAUGHING OUT LOUD":
                     s = s[:i]+"LOL"+s[i+17:]
                     return s
            else:
                if s[i] == "O":
                    if s[i:i+9] == "OH MY GOD":
                        s = s[:i]+"OMG"+s[i+9:]
                        return s
                else:
                    if s[i] == "F":
                        if s[i:i+20] == "FOR YOUR INFORMATION":
                            s = s[:i]+"FYI"+s[i+20:]
                            return s
    return s

def tohomoglyphs(s):
    for i in range(len(s)-1):
        if s[i] == "B":
            s = s[:i]+"|3"+s[i+1:]
        else:
            if s[i] == "H":
                s = s[:i]+"|-|"+s[i+1:]
            else:
                if s[i] == "K":
                    s = s[:i]+"|<"+s[i+1:]
                else:
                    if s[i] == "A":
                        s = s[:i]+"@"+s[i+1:]
    return s

def main():
    s = input("please input a string: ")
    # remove punctuation
    s = s.translate(str.maketrans('', '', string.punctuation))
            
    # replace lowercase letters to uppercase letters
    stringUpper = s.upper()
    print(stringUpper)
    stringUpper = toacronyms(stringUpper)
    print(tohomoglyphs(stringUpper))
       
    
main()

        
    
