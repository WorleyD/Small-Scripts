import sys
count = 1
for i in sys.stdin:
    nums = list(map(int, i.split()))
    nums = nums[1:]
    
    x = min(nums)
    y = max(nums)
    r = y-x

    print("Case %d: %d %d %d" % (count, x, y, r))
    count+=1
