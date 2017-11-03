#This problem is currently the highest difficulty one available on Kattis
#solution ran valid for multiple tests before exceeding time limit 
#program would not work for negative exponents, does not need to according to problem specifications
#Link to problem: https://open.kattis.com/problems/towers

def main():
    numterms = int(input(""))   #get the number of terms to be inputted
    tosort = []                 
    while (numterms > 0):       #for each term
    
        num = input("")         #get the term and split it by any '^'
        terms = num.split("^")  #add terms to array
        base = int(terms[0])    #save the first index as our base, and pop it from list
        terms.pop(0)
        tuple = (num, base)     
        
        prod = 1                #start out product at one
        
        #apply exponentiation by squaring, which is 
        
        for i in terms:         #for each term still left in array (which is now all our exponents)
            if int(i) == 0:
                prod = 0        #if theres a 0, the whole term will become 0
                break
            
            prod *= int(i)      #compute product of all non-zero terms (we now have one large exponent)

        odd = 1                 
        while (prod > 0):       #while our product is non-zero
            if prod == 1:
                break
            
            elif prod % 2 == 0:#if product is divisible by two, square our base and half the exponent
                base *= base
                prod = int(prod/2)
            
            else:              #if product is odd, save current base (will be multiplied at end)
                odd *= base    #then square base and half our (product - 1) 
                base *= base
                prod = int((prod - 1) / 2)
        
        if prod == 0:          #if product was 0, set our base to 1 (x^0 = 1)
            base = 1
        
        base *= odd            #multiply by odd (either 1 (unchanged) or a saved base if exponent was odd)
        tuple = (num, base)    #save final value along with initial expression to a tuple
        tosort.append(tuple)   #add tuple to a list
        numterms -= 1           

    tosort.sort(key=lambda tup:tup[1])  #sort list of tuples by calculated value
    print("Case 1:")                    #Print for Kattis output formatting
    for i in tosort:                    #print each expression, now in sorted order
        x = i[0]
        print(x)
    
main()
