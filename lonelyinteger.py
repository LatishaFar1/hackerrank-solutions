# Given an array of integers, where all elements but one occur twice, find the unique element.

# EXAMPLE

# a = [1,2,3,4,3,2,1]

# the unique element is 4

def lonelyinteger(array):
    #initialize a dictionary to store the count of each integer
    integer_counts = {}
    #iterate through the array and update the count of each integer in the dictionary
    for integer in array:
        if integer in integer_counts:
            integer_counts[integer] += 1
        else: 
            integer_counts[integer] = 1
    #iterate through the dictionary and return the integer that occurs only once.
    for integer, count in integer_counts.items():
        if count == 1:
            return integer
     #This solution has a time complexity of O(n), where n is the number of elements in the array./n
     # It uses a dictionary to store the count of each element, and then it iterates through the dictionary to find the element that occurs only once.


