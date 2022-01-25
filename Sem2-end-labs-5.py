# Author: 1/25/22

# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
#
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case


# turns the number to binary and returns the count of "1"s present in it, my explanation is longer than the code.
def count_bits(n):
    return bin(n).count("1")

print(count_bits(1234) == 5)