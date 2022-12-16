# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero./n
#  Print the decimal value of each fraction on a new line with 6 places after the decimal.

# EXAMPLE

# arr = [1,1,0,-1,-1]
# There are n=5 elements, two positive, two negative and one zero. 
# Their ratios are 2/5 = 0.400000, 2/5 = 0.400000  and 1/5 = 0.200000. 
# Results are printed as: 
# 0.400000 
# 0.400000
# 0.200000

def plusMinus(arr):
#initiating the pos, neg, and zero variables = 0
    positive = 0
    negative = 0
    zero = 0
# loop through the the beginning (0) to the end (length) of the array
    for i in range(0, len(arr)):
#if i is greater than 0, increase positive by one
        if arr[i] > 0:
            postive += 1
#if i is less than 0, increase negative by one
        elif arr[i] < 0:
            negative += 1
#if i is neither pos or neg, increase 0 by one
        else:
            zero += 1
#print positive, neg, and zero divided by the number of elements in the array(length)
    print(positive/len(arr))
    print(negative/len(arr))
    print(zero/len(arr))