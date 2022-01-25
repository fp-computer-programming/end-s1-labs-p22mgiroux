# Author: MOG 1/25/22

# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
# array = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
#
# For better understanding, please follow the numbers of the next array consecutively:
# array = [[1,2,3],
#         [8,9,4],
#         [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
#
# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.
# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].


def snail(snail_map):
# make an empty list to hold output
    array = []
# using "try" and a while loop, loop function until an error is thrown, then return the final array
    try:
        while True:
            for i, x in enumerate(snail_map):
# if it is the first list, append it as is into the "array" list
                if i == 0:
                    array.extend(x)
# if it is the last list, append its reverse to the "array" list
                elif i == len(snail_map) - 1:
                    x.reverse()
                    array.extend(x)
# if it is any other list, eg. one in the middle, only append the last list item, and remove it
                else:
                    array.append(x[-1])
                    del snail_map[i][-1]
# remove "top" and "bottom" arrays
            del snail_map[0]
            del snail_map[-1]
# for all of the middle lists, append their first digit and delete it, completing one full cycle
            for i in range(len(snail_map) - 1):
                array.append(snail_map[len(snail_map) - 1 - i][0])
                del snail_map[len(snail_map) - 1 - i][0]
# returns the array once the function can no longer cycle
    except:
        return(array)

print(snail([[1,2,3],
            [4,5,6],
            [7,8,9]]))

print(snail([[1,2,3],
            [8,9,4],
            [7,6,5]]))

print(snail([[1,2,3,4,5],
            [16,17,18,19,6],
            [15,24,25,20,7],
            [14,23,22,21,8],
            [13,12,11,10,9]]))