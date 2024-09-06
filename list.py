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