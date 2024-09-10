fruits = ["apple","banana","cherry"]
print(fruits)
print(fruits[2])
print(fruits[0:2])
print(fruits[-1])
"change the item value"
fruits[1]= "blackcurrant"
print(fruits)
"loop through a list"
for x in fruits:
    print(x)
"check if item exists"
if "kiwi" in fruits:
    print("yes,kiwi is present in the list")
else:
    print("No,kiwi is not present in the list")
"list length"
print(len(fruits))
"Add items"
fruits.append("orange")
print(fruits)
"remove items"
fruits.remove("apple")
print(fruits)
"pop"
fruits.pop()
print(fruits)
"deleting"
del fruits[0]
print(fruits)
fruits.append("Apple, banana,cherry")
print(fruits)
"del will clear the entir list"
"clear method"
fruits.clear()
print(fruits)
fruits.append("Apple,banana,Cherry,Orange,Blackcurrant")
print(fruits)
"copying of list"
mylist = fruits.copy()
print(mylist)
"copy of list using list"
mylist = list(fruits)
print(mylist)
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

