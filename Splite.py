num = input("Enter a String number: ")
list = num.split()
sum = 0
for n in list:
    sum = sum + int(n)

print(sum)