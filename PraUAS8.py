def mystery(n, m):
    p = 0
    e = 0
    iteration = 0  
    print("Iteration | p  | e")
    print("===================")
    print(f"{iteration:9} | {p}  | {e}")

    while n > 0:
        p = n - m
        e = p + m
        iteration += 1
        print(f"{iteration:9} | {p}  | {e}")
        n -= 1

    return e

print('8. Fungsi mystery(4, 3):',mystery(4,3))