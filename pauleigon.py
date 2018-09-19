N, paul, opp = input().split()
N, paul, opp = int(N), int(paul), int(opp)

turn = (paul + opp) // N

if turn % 2 == 0:
    print("paul")
else:
    print("opponent")
