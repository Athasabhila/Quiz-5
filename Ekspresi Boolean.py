p = 11
q = 5
r = 4

# a
result_2a = (p - r) == (r + q)
print("a. ((p - r) == (r + q)):", result_2a)

# b
result_2b = ((p % 3) + q) != (r % 2)
print("b. (((p % 3) + q) != (r % 2)):", result_2b)

# c
result_2c = (q - 3) == (p % 2 + q)
print("c. ((q - 3) == (p % 2 + q)):", result_2c)

# d
result_2d = (r + q) != ((p * 2) % 2)
print("d. ((r + q) != ((p * 2) % 2)):", result_2d)

# e
result_2e = ((q % 3) + p) > (r % 2)
print("e. ((((q % 3) + p) > (r % 2)):", result_2e)

# f
result_2f = (r + p) <= (q * 5)
print("f. (((r + p)) <= (q * 5)):", result_2f)
