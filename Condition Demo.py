marks = int(input("Enter your marks: "))

the_user_is_good = True
print(the_user_is_good)

def show_grade(grade):
    print(f"You got: {grade}")

if marks>=80:
    show_grade("A+")
elif marks <80 and marks >=70:
    show_grade("A")
elif marks <70 and marks >=60:
    show_grade("A-")
elif marks >=33:
    show_grade("passed")
else:
    show_grade("failed :(")


if marks >80 or marks <33:
    print("You are very Good or Bad")
    if marks >80:
        print("Excellent")
    else:
        print("you are not so good!")
else:
    print("You are okay")


number = int(input("Enter A number: "))

check = number>=80
print(check)