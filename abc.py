nums = list(map(int, input().split()))
order = input()

nums.sort()

a = nums[0]
b = nums[1]
c = nums[2]

for i in order:
    if i == "A":
        print(a,end="")
    if i == "B":
        print(b,end="")
    if i == "C":
        print(c, end="")
    print(" ", end="")

