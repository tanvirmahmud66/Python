
import math

user_number = int(input("Upper limit for prime: "))

def prime(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

for i in range(1,user_number+1):
    if prime(i):
        print(i)


