from datetime import date
# Ask the user for their birthday and then convert it into 3 different
# variables for the day, month and year.
birthday = input("Enter your birthday in the format DD/MM/YYYY: ")
# Use a try and except to ensure the input is in a valid format
try:
    birth_day = int(birthday.split("/")[0])
    birth_month = int(birthday.split("/")[1])
    birth_year = int(birthday.split("/")[2])
except:
    print("Error: Invalid format for birthday given.")
    exit()
# Get today's date
today = date.today()
# The age is the different in years
age = today.year - birth_year
# Check if the birthday has passed this year,
# if not take away 1 from the year difference
if (birth_month, birth_day) > (today.month, today.day):
    age -= 1

print(f"You are {age} years old!!")
