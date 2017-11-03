def main():
    numterms = int(input(""))
    tosort = []
    while (numterms > 0):
    
        num = input("")
        terms = num.split("^")
        base = int(terms[0])
        terms.pop(0)
        tuple = (num, base)
        
        prod = 1
        for i in terms:
            if int(i) == 0:
                prod = 0
                break
            
            prod *= int(i)

        odd = 1
        while (prod > 0):
            if prod == 1:
                break
            
            elif prod % 2 == 0:
                base *= base
                prod = int(prod/2)
            
            else:
                odd *= base
                base *= base
                prod = int((prod - 1) / 2)
        
        if prod == 0:
            base = 1
        
        base *= odd
        tuple = (num, base)
        tosort.append(tuple)
        numterms -= 1

    tosort.sort(key=lambda tup:tup[1])
    print("Case 1:")
    for i in tosort:
        x = i[0]
        #y = i[1]
        print(x)
    
main()
