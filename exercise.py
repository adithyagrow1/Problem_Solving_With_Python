"List Average"
"Write a program that calculates the average of a list of numbers."
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print(f"Average: {average}")
"Unique Items in List"
"Create a program that takes a list of integers and returns a list of unique integers."
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)
"Count Occurrences"
"Write a program that counts how many times each element appears in a list."
fruits = ["apple", "banana", "apple", "orange", "banana"]
fruit_count = {fruit: fruits.count(fruit) for fruit in set(fruits)}
print(fruit_count)
"Tuple Swap"
"Create a program that swaps the first and last elements of a tuple."
def swap_tuple(t):
    return (t[-1],) + t[1:-1] + (t[0],)

my_tuple = (1, 2, 3, 4, 5)
swapped = swap_tuple(my_tuple)
print(swapped)
"Set Intersection"
"Write a program that finds the intersection of two sets."
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
intersection = set_a & set_b
print(intersection)
"Dictionary Lookup"
"Create a program that retrieves a value from a dictionary using a key."
student = {"name": "Alice", "age": 20, "major": "Biology"}
key = "age"
print(f"{key}: {student[key]}")
"Merge Dictionaries"
"Write a program that merges two dictionaries and handles duplicate keys by keeping the values from the second dictionary."
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)
"List Reversal"
"Create a program that reverses a list without using the built-in reverse method."
numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
print(reversed_list)
print("Absolute Path:", absolute_path)

# appending content to file
try:
    with open(absolute_path,'a') as file:
        file.write("welcome to python scriptng \n")

        with open(absolute_path,'r') as file:
            content = file.read()
            print(content)
except Exception as e:
    print("Error:")
