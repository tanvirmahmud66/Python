name = ["Tanvir","Rashid","Mahmuda","Rumki","Ayesha","Fahim"]
print(name)

#lenth
print(len(name))

#To add item
name.append("Tithi")
print(name)

#insert
name.insert(1,"Fahim")
print(name)

name.remove("Tanvir")
print(name)

#sotring
name.sort()#Accending
print(name)
name.reverse()#deccending
print(name)

#count same element
print(name.count("Fahim"))

name.pop()
print(name)
name.pop()
print(name)

#copy element in another list
family = name.copy()
print(family)

#index number of an element
position = family.index("Mahmuda")
print(position)

#remove all element
name.clear()
family.clear()
print(name)
print(family)

