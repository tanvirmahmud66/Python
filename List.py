subject = ["C","C++","Java","Python"]
print(subject)
print(subject[0])
print(subject[2])
print(subject[1:])#will show from index[1] to all
print(subject[-1])#will show from reverse
print(subject[-2])
print(subject[-1:])
#check it is into the list or not
print("Python" in subject) # will show...True
print("Scala" in subject)#False
print("C#" not in subject)#true

#to add more
newSubject = subject+["Scala","C#"]
print(newSubject)
print("Python" in newSubject) # will show...True
print("Scala" in newSubject)#true
print("C#" not in newSubject)#true