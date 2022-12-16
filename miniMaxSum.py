# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# EXAMPLE

# arr = [1,3,5,7,9]

# the minimum sum is 1 + 3 + 5 + 7 = 16 
# the maximum sum is 3 + 5 + 7 + 9 = 24

# The function prints 16 & 24

def miniMaxSum(arr):
    #sort the array from smallest to largest
    arr.sort()
    #find the minimum sum by adding the first four values
    min = sum(arr[:4])
    #find the maximum sum by adding the last four values
    max = sum(arr[1:])
    #print both numbers
    print(min,max)
