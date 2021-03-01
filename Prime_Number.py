num = int(input("Enter a number to check Prime or not: "))
count = 0
for x in range(2,num):
    if num%x==0:
        count += 1
        break
if count == 0:
    print(f"Prime Number:{num}")
else:
    print(f"Not Prime Number:{num}")