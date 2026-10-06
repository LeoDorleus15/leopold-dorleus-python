#Section 1

name = 'Leopold'
age = 27
height = "6.1"
is_student = True


print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

# Section 2
name = input("Please enter your name: ")
Year_of_birth = input('Please enter the year you were born: ')
conv_age = int(Year_of_birth)
year_current = 2026
age = year_current - conv_age
print(f'Hello, {name}! You are approximately {age} years old.')


# Section 3
minimum_wage = input("Please enter how much you get paid: ")
hours_worked = input("Please enter how much hours you work: ")
minimum_wage = float(minimum_wage)
hours_worked = float(hours_worked)
monthly_salary = minimum_wage * hours_worked
print(f'As a full time employee, I make ${monthly_salary} a month')

# Section 4
item = 'iphone_18'  
price = 1999
quantity = 5
total = price * quantity
print('======================')
print('  Christmas Gift    ')
print('======================')
print('Item :  ',item)
print('Price :$   ',price)
print('Quantity :  ',quantity)
print("Total :  $",total)
print('======================')

# Section 5
name = input("Please enter your name: ")
hometown = input('Please enter where youre from: ')
favorite_hobby = input('Please enter your hobby: ')
fun_fact = input('Please enter a fun fact about you: ')
Year_of_birth = input('Please enter the year you were born: ')
conv_age = int(Year_of_birth)
year_current = 2026
age = year_current - conv_age
print("╔══════════════════════════════╗")
print(f"     PROFILE:  {name}")
print("╚══════════════════════════════╝")
print(f"Hometown:    {hometown}")
print(f"Hobby:       {favorite_hobby}")
print(f"Fun Fact:    {fun_fact}")
print(f"Age:         {age}")
print("================================")
