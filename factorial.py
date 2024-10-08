"factorial of a given number"
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
user_input = int(input("Enter a integer: "))
if user_input >= 0:
    print(f"The factorial of {user_input} is {factorial(user_input)}")
else:
    print("Please enter a integer.")