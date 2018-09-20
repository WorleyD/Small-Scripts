for i in range(int(input())):
    stops = int(input())

    passengers = 0
    for i in range(stops):
        passengers = (passengers*2) + 1

    print(passengers)
