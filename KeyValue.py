studentId = {
    101: "Tanvir Mahmud Fahim",
    102: "Abdur Rashid",
    103: "Mahmuda Begum",
    104: "Romana Sharmin Rumki",
}

print(studentId[102])
#print(studentId[5]) will show an error

print(studentId.get(101,"Not a Valid key"))
print(studentId.get(103,"Not a Valid key"))
print(studentId.get(105,"Not a Valid key"))