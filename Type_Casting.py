'''
In Python user
input function input()
always take input
as a String
but when we need to take a number
we have to use type casting
'''
#we can type cast when we taking input
num1 = int(input("Enter 1st Number: "))
num2 = input("Enter 2nd Number: ")#normal way

#sum will be automatically change from String to int
result = num1 + int(num2) #num2 type casting
print("Sum Result Is: ",result)

result = num1 - int(num2)
print("Sub Result Is: ",result)

'''
if we not type cast when 
we taking input from
user thn we have to 
so many time use type 
casting when we 
need this variable
'''

n1 = int(input("Enter Another 1st Number: "))
n2 = int(input("Enter 2nd Number: "))

res = n1 + n2
print("Sum: ",res)

res = n1 - n2
print("Sub: ",res)

res = n1 * n2
print("Mul: ",res)

res = n1 / n2
print("Div: ",res)

res = n1 % n2
print("Rim: ",res)
