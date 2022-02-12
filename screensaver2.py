# matrix-like screen saver second strategy

import random
import string
import time

# general constants 
COLS = 280
DELAY = 0.100
LIMIT = 10000
QWERTY = string.ascii_letters + string.digits

# probability constants
IMPROVE = 65
THRESHOLD = 97
UPLIMIT = 100

def setFirst( ):
    v = []
    for col in range(COLS):
        if random.randint(0,1):
            v.append(True)
        else:
            v.append(False)
    return v

def setPos( prev ):
    cur = []
    for i in range( COLS - 1 ):
        prob = prev[i] * IMPROVE + random.randint( 0, UPLIMIT)
        if prob >= THRESHOLD:
            cur.append(True)
        else:
            cur.append(False)
    return cur

t = 0
seed = setFirst()
while t < LIMIT : 
    line = ""
    seed = setPos( seed ) 
    for b in seed:
        if b:
            line = ''.join( (line, random.choice(QWERTY)) )
        else: 
            line = ''.join( (line, " ") ) 
    print(line)
    t = t + 1
    time.sleep(DELAY)
