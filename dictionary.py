car = { "brand":"ford","model":"mustang","year":1964}
print(car)
student = {"Name":"Adithya","class":"High school","subject":"python"}
print(student)
for x in student:
    print(x)
for x,y in student.items():
    print(x,"-",y)
for x in student.values():
    print(x)
car["color"] = "red"
print(car)
"pop out a particular element from a dictionary"
car.pop("model")
print(car)
"to pop out the last element from the dictionary"
car.popitem()
print(car)
"del keyword"
del student["class"]
print(student)
"to delete the entier dictionary uses del thisdict then print"
"to copy a dictionary "
mydict = car.copy()
print(mydict)