num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
'''
if num1 > num2:
    print(num1)
else:
    print(num2)
'''
#ternary Opertator
max = num1 if num1 > num2 else num2
print("Maximum: ",max)
