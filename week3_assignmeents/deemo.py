def count_divisors(n):

    divisors = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors += 2
            if i**2 == n:
                divisors -= 1
    return divisors

def find_triangle_number(n):

    num = 0
    i = 1
    while True:
        num += i
        if count_divisors(num) > n:
            return num
        i += 1

x = find_triangle_number(500)
print(x)