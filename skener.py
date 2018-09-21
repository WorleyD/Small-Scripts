x,y,xs,ys = map(int, input().split())
for i in range(x):
    row = input()
    newrow = [0]*x
    for i in range(len(row)):
        newrow[i] = row[i]*ys
    for i in range(xs):
        print(''.join(newrow))
