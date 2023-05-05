#number one (a)

n = 0
for i in range(401):
    n = i + n
print(n)

#number one (b)

n = 400
mySum = (n*(n+1))/2
print(mySum)

#number two(a)

print([i for i in range(2, 51)])

#or

nums = []
for i in range(2, 51):
    nums.append(i)
print(nums)

#number two (b)
print([i for i in range(1, 8)])

#number three (a)

print([i for i in range(60, 401) if i % 3 == 0 and i % 4 == 0])

#number three (b)

n = 0
for i in range(10, 23):
    n = i + n
print(n)

#number four (a)

for i in range(2, 51, 2):
    print(i)

#number four (b)
for i in range(20, 1, -2):
    print(i)