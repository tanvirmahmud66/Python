
# def even(number):
#     if number%2==0:
#         return True
#     else:
#         return False
#
# even_number = []
# starting = 0
# user_input = int(input("Limit: "))
# while starting <= user_input:
#     if even(starting):
#         even_number.append(starting)
#     starting = starting + 1
#
# for value in range(0,user_input+1):
#     if even(value):
#         even_number.append(value)
#
# print(f"even nnumber =  {even_number}")
# print(len(even_number))


grocery = ["rice","Tomato","potato","water","ginger","onion","ladies Finger"]
#
# for item in grocery:
#     if item == "potato":
#         continue
#     if item == "onion":
#         break
#     print(item)


# for i in range(0,10,3):
#     print(i)

for i in range(0,len(grocery)):
    print(grocery[i])