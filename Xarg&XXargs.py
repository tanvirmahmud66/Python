#xargs works like tuple
def student(*details):
    print(details)

student(101,"Fahim",23)
student(102,"Ayesha")
student(103,"Raihan",24,"SUB")

def add(*number):
    sum = 0
    for num in number:
        sum = sum+num
    print(sum)

add(10,20)
add(10,20,30)
add(10,20,30,40)

#xxargs work like dictionarise

def list(**value):
    print(value)

list(id = 101, name = "Fahim")