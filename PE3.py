nums =[]
for n in range(600851475043,600851475143):
    for m in range(2,n-1):
        if n%m == 0:
            break
        else:
            nums.append(n)

for num in nums:
    if num%3 ==0:
        nums.remove(num)
    elif num%5 == 0:
        nums.remove(num)

nums = list(dict.fromkeys(nums))
            

print(nums[-1:])
