n1 = int(input("Enter num1: "))
n2 = int(input("Enter num2: "))
n3 = int(input("Enter num3: "))

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)

ch = 'w'
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("Vowel")
else:
    print("Consonant")
