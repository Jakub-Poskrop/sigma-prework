# Ask the user for the numbers in the list
list = input(
    "Enter the numbers in your list with a space in between each: ").split()
# Check if all elements in the list are numbers
if any(y.isalpha() for y in list):
    print("Error: invalid data type, input numbers only")
    exit()
# Set the initial values of max and min as the first number in the list
max, min = float(list[0]), float(list[0])
# Iterate through each number in the list
# and compare them with the values of max and min and adjust accordingly
for i in range(1, len(list)):
    if float(list[i]) > max:
        max = float(list[i])
    if float(list[i]) < min:
        min = float(list[i])
# Print the results
print(
    f"The maximum in this list is {max} and the minimum is {min}")
