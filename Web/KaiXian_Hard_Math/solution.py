from z3 import *
import struct

# calculate e,f,d for a given input password
def calc(m):
    e = 0
    f = 0
    d = 0
    for i in xrange(0, len(m)):
        c = ord(m[i])
        e += c
        f ^= c
        d = (struct.unpack("i",struct.pack("I",(d << 0x5)&0xffffffff))[0] - d) + c - 48;
    return d,e,f

# try z3 for a given password length
def check(length):
    print("Try to find a valid password for length: {}".format(length))
    s =  Solver()
    
    # a character has to be one of: 0At3_LDfcsWrbuO
    def is_valid(x):
        return Or(
                (x == ord('0')),
                (x == ord('A')),
                (x == ord('t')),
                (x == ord('3')),
                (x == ord('_')),
                (x == ord('L')),
                (x == ord('D')),
                (x == ord('f')),
                (x == ord('c')),
                (x == ord('s')),
                (x == ord('W')),
                (x == ord('r')),
                (x == ord('b')),
                (x == ord('u')),
                (x == ord('O')))

    # dynamically create a Bit vector for the password length
    vec=""
    for i in xrange(0,length):
        vec += "pw[{}] ".format(i)

    m = BitVecs(vec, 8)

    # add the rules for the alphabet to each character
    for i in xrange(0, length):
        s.add(is_valid(m[i]))

    # init e and f with 0
    e=0
    f=0

    # perform the calculations that can be solved with z3
    # d not included
    for i in xrange(0, length):
        e += m[i]
        f ^= m[i]

    # The extracted rules
    s.add(e == 0x7B0)
    s.add(f == 0x42) 
    s.add(m[0xb] == m[0xf]) 
    s.add(m[0x13] == m[0xf]) 
    s.add(m[0x1] == m[0x0])
    s.add(m[0x4] == m[0xc])
    s.add(m[0x8] == m[0xd])

    # explorative part. Set certain values by hand
    s.add(m[0] == ord('0'))
    s.add(m[1] == ord('0'))
    s.add(m[2] == ord('b'))
    s.add(m[3] == ord('f'))
    #Guess 'u' based on the word produce
    s.add(m[4] == ord('u'))
    #Guess 's' based on the word produce
    s.add(m[5] == ord('s'))
    s.add(m[6] == ord('c'))
    s.add(m[7] == ord('A'))
    s.add(m[8] == ord('t'))
    s.add(m[13] == ord('t'))
    s.add(m[18] == ord('W'))
    s.add(m[21] == ord('L'))
    

    # check if there is a solution to those rules
    while s.check() == z3.sat:
        # get a model that satisfies the rules
        model = s.model()
        out = ""
        nope = []
        #print "\n#### Model ####"
        for i in m:
            if str(i):
                out += chr(model[i].as_long()&0xff)
            nope.append(i!=model[i])

        # prevent this solution to come up again
        s.add(Or(nope[:-1]))

        # check if the password satisfies d
        d,e,f = calc(out)
        print(length, out, hex(d),hex(e),hex(f), d == 1177935976)
        if d== 1177935976 or d == 0x4635E068:
            print(out)
            exit()
    print(s.check())

for x in [23,25,26]:
    check(x)
