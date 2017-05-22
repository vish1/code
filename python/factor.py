from math import sqrt

number = 600851475143

for i in range(2, int(sqrt(number))):
    if number%i == 0:
        notprime=0
        for j in range(2, int(sqrt(i))):
            if i%j == 0:
                notprime = 1
                break
        if notprime == 0:
            factor = i
            
        
        
print factor
