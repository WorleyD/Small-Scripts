import math
while(1):
    r, t, m = input().split()
    r = float(r)
    t,m = int(t), int(m)

    if r+t+m == 0:
        break

    true = r * r * 3.141592654

    est = (m / t) * ((2*r)*(2*r))

    print(true, est)
