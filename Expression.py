# a. 15 mod 5
result_a = 15 % 5
print("a. 15 mod 5 :", result_a)

# b. 12 + 3 * 5 == 75
result_b = 12 + 3 * 5 == 75
print("b. 12 + 3 * 5 == 75 :", result_b)

# c. "PML" + "15523"
result_c = "PML" + "15523"
print("c. \"PML\" + \"15523\":", result_c)

# d. "100" + 234 (ini akan menyebabkan error karena tipe data berbeda)
try:
    result_d = "100" + 234
except TypeError:
    result_d = "Error: Cannot concatenate str and int"
print("d. \"100\" + 234:", result_d)

# e. ((11 % 3) + 2) != 8 / 2
result_e = ((11 % 3) + 2) != 8 / 2
print("e. ((11 % 3) + 2) != 8 / 2:", result_e)
