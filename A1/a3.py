def find_min_num(z):
    num = 1
    count = 0

    while True:
        temp = num
        while temp % 5 == 0:
            count += 1
            temp //= 5
        if count >= z:
            return num
        num += 1

n = 6
print(find_min_num(n))
