student ={
    "name": "Arshia",
    "age" : 26,
    "city" : "Kabul",
    "skills" : ["python", "HTML","CSS"]
}

print(student["age"])
print(student["name"])
print(student["skills"])

student["age"] = 27
print(student["age"])
student["goal"] = "billionaire"
print(student)
del student["city"]
print(student)


