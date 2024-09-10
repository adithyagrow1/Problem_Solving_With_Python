fruits=("apple","banana","cherry",)
print(fruits)
x=("apple","banana","cherry")
print(fruits)
print(fruits[2])
print(fruits[0:2])
print(fruits[-1])

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
"print the type of the variable"
print(type(fruits))
