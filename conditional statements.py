a = 300
b = 33
c = 100
if b>a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
"Logical and in CS "
if a>b and c>a:
    print("Both conditions are true")
def find_largest(a, b, c):
    if a > b and a > c:
        largest = a
    elif b > a and b > c:
        largest = b
    else:
        largest = c
    return largest
a = 100
b = 140
c = 120
result = find_largest(a, b, c)
print(f"The largest number is {result}")




