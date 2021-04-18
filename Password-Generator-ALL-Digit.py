#!/usr/bin/env python3

import random

# Main Function Start Here
def shuffle(string):
    tmpList = list(string)
    random.shuffle(tmpList)
    return ''.join(tmpList)

# you can also add more variables to generate more digit password
uppercaseLetter1 = chr(random.randint(65,100))
uppercaseLetter2 = chr(random.randint(65,100))
uppercaseLetter3 = chr(random.randint(65,100))
uppercaseLetter4 = chr(random.randint(65,100))
uppercaseLetter5 = chr(random.randint(65,100))
uppercaseLetter6 = chr(random.randint(65,100))
uppercaseLetter7 = chr(random.randint(65,100))
uppercaseLetter8 = chr(random.randint(65,100))
uppercaseLetter9 = chr(random.randint(65,100))
uppercaseLetter10 = chr(random.randint(65,100))

#Random Passord Generat Start Here
password = (uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + uppercaseLetter5 + uppercaseLetter6 + uppercaseLetter7 +
uppercaseLetter8 + uppercaseLetter9 + uppercaseLetter10)
password = shuffle(password)

#Program Output Start Here
print(password)
