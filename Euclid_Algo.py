
def euclidExtended(a, b): 
    # Base Case 
    if a == 0 : 
        return b,0,1
             
    gcd,x1,y1 = euclidExtended(b%a, a)  
    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd,x,y 

def gcdBase(a, b):
    if b == 0:
        return a
    return gcdBase(b, a % b)

def modInverse(a, b):
    if gcdBase(a, b) > 1:
        #inverse does not exist
        return -1
    for X in range(1, b):
        if (((a % b) * (X % b)) % b == 1):
            return X
    return -1   

def phi(n):
    amount = 0        
    for k in range(1, n + 1):
        if gcdBase(n, k) == 1:
            amount += 1
    return amount

#main 
a, b = 10012012,2314213
g, x, y = euclidExtended(a, b) 
print("gcd(", a , "," , b, ") = ", g)

a, b = 28176412,29108188
g, x, y = euclidExtended(a, b) 
print("gcd(", a , "," , b, ") = ", g)

a, b = 38172,23812188
g, x, y = euclidExtended(a, b) 
print("gcd(", a , "," , b, ") = ", g)

a, b = 12091,24123123
i = modInverse(a,b)
print("The multiplicative inverse of 12091 mod 24123123 is ", i)

a, b = 28173928,129182771
i = modInverse(a,b)
print("The multiplicative inverse of 12091 mod 24123123 is ", i)

n = 98803519
p = phi(n)
print("Totient Functions: ", p)