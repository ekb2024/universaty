number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = []
not_primes =[]
is_prime = 11

for i in number:
    for j in number:
        if i % j != 0 and i != 1:
             is_prime = True
        elif i % j == 0 and i != 1 and j != 1 and i != j:
             is_prime = False
             break

    if is_prime == True:
        primes.append(i)
    if  is_prime == False:
        not_primes.append(i)

print(primes)
print(not_primes)






