a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

count = 0
while (1):
    if b-a == c - b and b - a == 1:
        break
    
    if b - a < c - b:
        a = b+1
        a,b = b,a
    else:
        c = b-1
        c,b = b,c
    count+=1

print(count)
    
