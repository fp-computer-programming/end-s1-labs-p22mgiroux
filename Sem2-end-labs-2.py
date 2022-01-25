# Author: MOG 1/25/22

# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
#
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]


def move_zeros(array):
# holds number of zeros found
    n = 0
    for i in range(len(array)):
# uses the number of zeros found to edit the searched index to offset their deletion
        if array[i-n] == 0:
# remove the zero and tack it on to the end
            array.pop(i-n)
            array.append(0)
# add to number of found zeros
            n += 1
# return
    return array

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))