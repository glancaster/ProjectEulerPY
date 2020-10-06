

n = 0
n2 = 0
num = []
while n <4000000:
    num.append(n)
    nf = n2 + n
    n = n2
    n2 = nf 
    n +=1
nums = num[2:]

evens = []
for x in nums:
    if x%2 == 0:
        evens.append(x)

print(evens)
print(sum(evens))


