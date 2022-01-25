# Author: MOG 1/15/22

# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
#
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
#
# The following are examples of expected output values:
#
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3


def bound(n):
# constraining rgb values
    if n < 0:
        n = 0
    elif n > 255:
        n = 255
    return n

# converts big numbers (>9) to letters
def convert(n):
    if n == 0:
        n = "0"
    elif n == 10:
        n = "A"
    elif n == 11:
        n = "B"
    elif n == 12:
        n = "C"
    elif n == 13:
        n = "D"
    elif n == 14:
        n = "E"
    elif n >= 15:
        n = "F"
    else:
        n = str(n)
    return n

def rgb(r, g, b):
# gets values for rgb, uses convert function, and formats them for the return statement
    r1 = bound(r) // 16
    r2 = bound(r) % 16
    
    g1 = bound(g) // 16
    g2 = bound(g) % 16
    
    b1 = bound(b) // 16
    b2 = bound(b) % 16
    
    return convert(r1) + convert(r2) + convert(g1) + convert(g2) + convert(b1) + convert(b2)

#This is so inneficient

print(rgb(254,253,252))
print(rgb(255,255,255))
print(rgb(1,2,3))