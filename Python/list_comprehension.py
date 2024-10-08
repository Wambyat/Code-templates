# This is just basic list comprehension.
import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Generates a list of primmes from 1 to 99
S = [i for i in range(0,100) if is_prime(i)]

# This loads the entire list into memeory. If that's not required do this:
S2 = (i for i in range(0,100) if is_prime(i))

# This creates a iterator. This is MUCh better for fuctions that just iterate thru the list and nothing else.
print(sum(S2))

print(S)
print(S2)

# This will throw an error as S2 is done iterating.
# print(next(S2))

S2 = (i for i in range(0,100) if is_prime(i))
print(next(S2))
