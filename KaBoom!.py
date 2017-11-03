#Problem was located on ACM ECNA Regional Practice Problems, question will be provided once available.
#Problem mostly tied into high school physics/math. Some trig and dynamics equations were used.
#Comments will be updated to better reflect question once available

import math

def main():
    xm, vx, vy, xa, va, tk = (map(int, input().split())) #get all necessary input

    xd = float(xm + vx*tk - xa)      #calculate x and y distance
    yd = float(vy*tk - 16*tk*tk)

    hypd = (xd*xd + yd*yd)**0.5       #calculate hypoteneuse

    t = hypd/va                       #calculate time and angle  
    a = math.degrees(math.asin(yd/hypd)) 
    
    #if we can not destroy the missile (would have needed to fire before it launched, or their missile has already landed)
    if (t > tk or yd <= 0):
        print("start running")      #sound alarm
    else:
        print(tk-t, a)              #otherwise print when to shoot our missile, and the angle to shoot it at

main()
