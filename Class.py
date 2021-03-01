class Person:
    def __init__(self,person_name: str,year_of_birth: int,height: int= None):
        self.__name = person_name
        self.__date_of_birth = year_of_birth
        self.__height = height

    def get_year_of_birth(self):
        return self.__date_of_birth

    def get_name(self):
        return self.__name

    def __has_any_number(self,string):
        return "0" in string

    def set_name(self,new_name):
        if self.__has_any_number(new_name):
            print("Sorry! Person name can't have number")
            return
        self.__name = new_name

    def get_summary(self):
        return f"Name: {self.__name}, Date of Birth: {self.__date_of_birth}, Height: {self.__height if self.__height is not None else 'Invalid'}"


person_list = [Person("Tanvir",1990,72),
               Person("Mahmud",1989,32),
               Person("Ayesha",1999,25),
               Person("Fahim",1997,50),
               Person("Abdur Rashid",1952),
               Person("Mauhmuda begum",1954)]

# for person in person_list:
#     if person.get_year_of_birth() is not None and person.get_year_of_birth() <= 1990:
#         print(person.get_summary())

class Student(Person):
    def __init__(self,person_name: str, year_of_birth: int, Student_id: str, email:str):
        super().__init__(person_name, year_of_birth)
        self.mail = email
        self.id = Student_id

    def get_summary(self):
        return f"Name:{self.get_name()}, email: {self.mail},Birth: {self.get_year_of_birth()}"

    def __str__(self):
        return self.get_summary()

    def __repr__(self):
        return self.get_summary()


student1 = Student("A",1990,"CSE-06607742","tanvirmahmudfahim1313@gmail.com")
print(student1)
student1.set_name("Tanvir Mahmud Fahim")
print(student1)



