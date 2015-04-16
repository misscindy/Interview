'''
Basic Facts
The Operators:

x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
x >> y
Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
x & y
Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
x | y
Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
~ x
Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
x ^ y
Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0,
and it's the complement of the bit in x if that bit in y is 1.
Just remember about that infinite series of 1 bits in a negative number, and these should all make sense.

https://wiki.python.org/moin/BitManipulation
https://wiki.python.org/moin/BitArrays



'''


def tricks():
    x = 11
    print "^ ops, 0 retrieve a bit, 1 gets complement of a bit"
    print "x ^ 0s : x", x ^ 0, bin(x)
    print "x ^ 1s : ~x", x ^ (15), bin(x ^ (15))

    print "x ^ x  : 0", x ^ x

    print "============================================="

    print "& ops, 0 clears a bit, 1 keeps the bit"
    print "x & 0s : 0", x & 0, bin(x & 0)
    print "x & 1s : x", x & (15), bin(x & (15))
    print "x & x  : x", x & x

    print "============================================="

    print "|  ops, 0 keeps the bit, 1 set the bit to 1"
    print "x | 0s : x", x | 0, bin(x | 0)
    print "x | 1s : 1", x | (15), bin(x | (15))
    print "x | x  : x", x | x

########################################
#               OPS                    #
########################################


# Get bit
def get_nth_bit(x, n):
    #              zeroth
    # 1  1  0  1  1  0
    #       1  0  0  0
    # 0  0  0  0  0  0 -> 0

    return 1 if (x & (1 << n) != 0) else 0


# Set Bit
def set_nth_bit(x, n):
    return x | (1 << n)


# Clear Bit
def clear_nth_bit(x, n):
    mask = ~(1 << n)
    return x & mask


def clear_left_to_i(x, n):
    # inclusive
    # clear from most significant bit to ith
    mask = (1 << n) - 1
    return x & mask


#TODO: lookup and complete function
#def clear_i_to_0(x, n):


# Update Bit

def update_bit(x, n, v):
    # clear nth bit
    x &= ~(1 << n)
    # set nth to v
    return x | (v << n)


# calculates the number of 1s in a binary number
def hamming_weight(x):
    count = 0
    while x:
        x &= (x - 1)
        count += 1
    return count

if __name__ == '__main__':
    tricks()
    test_cases = [
        (0, 4, 1),

    ]
    #for x, n, v in test_cases:


