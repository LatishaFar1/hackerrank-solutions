# You will be given a list of 32 bit unsigned integers. Flip all the bits (0 -> 1 and 1 -> 0) /n
# and return the result as an unsigned integer.

# EXAMPLE

# n = 9₁₀
# 9₁₀ = 1001₂. We're working with 32 bits, so:

# 0000000000000000000000001001₂ = 9₁₀
# 11111111111111111111111110110₂ = 4294967286₁₀

# Return 4294967286


# NOTES: 

# ** is an exponentiation operator. 

def flippingBits(n):
    result = 0
    for i in range(31,-1,-1):
        if n//(2**i) == 1:
            n = n - 2**i
            x = 0
        else:
            x = 1
        result += 2**i * x
    return result