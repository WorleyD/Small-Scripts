
import math

def main():
    xm, vx, vy, xa, va, tk = (map(int, input().split()))

    xd = float(xm + vx*tk - xa)
    yd = float(vy*tk - 16*tk*tk)

    hypd = (xd*xd + yd*yd)**0.5

    t = hypd/va
    a = math.degrees(math.asin(yd/hypd))

    if (t > tk or yd <= 0):
        print("start running")
    else:
        print(tk-t, a)

main()
