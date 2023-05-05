
def isPrime(n):
    flag = 0
    if n == 1:
        flag = 1
    else:
        for i in range(2, n//2 + 1):
            if (n % i == 0):
                flag = 1
                break
    if flag == 0:
        return True
    else:
        return False
print(isPrime(0))


n = 4
for i in range(2, n // 2 + 1):
    print(i)

print(6//2+1)
