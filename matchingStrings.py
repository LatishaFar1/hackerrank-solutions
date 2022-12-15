# There is a collection of input strings and a collection of query strings. 
# For each query string, determine how many times it occurs in the list of input strings. 
# Return an array of the results.

# EXAMPLE

# strings = ['ab', 'ab', 'abc']
# queries = ['ab', 'abc', 'bc']

# results = [2,1,0]


def matchingStrings(strings, queries):
    count = []
    for query in queries:
#create a list of items in strings where item is = to query
        arr = [s for s in strings if s == query]
#add the length of that array to the count
        count.append(len(arr))
    return count 
    