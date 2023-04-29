def factor(num):
    x = 1
    for i in range(1, num + 1):
        x *= i
    return str(x)

def adder(num_str):
    num_lst = [int(x) for x in num_str]
    return sum(num_lst)

print(adder(factor(100)))