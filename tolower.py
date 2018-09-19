p, t = input().split()
p, t = int(p), int(t)

count = 0

for i in range(p):
    flag = 1
    for i in range(t):
        test = input()
        for i in range(1, len(test)):
            if ord(test[i]) < 97:
                flag = 0

    if flag == 1:
        count+=1

print(count)
                

            
                        
    
