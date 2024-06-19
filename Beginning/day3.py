#day3: conditions (single, nested), comparison operators, logical operators
# if, else 
# if, elif, else 

# check if the number is odd or even
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if number % 2 == 0:
  print("This is an even number.")
else: 
  print("This is an odd number.")

#bmi calculator
  # Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight/(height**2)
if(bmi < 18.5):
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

#leap year
  # Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
  if year % 100 != 0:
    print("Leap year")
  else:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
else:
  print("Not leap year")

  #order pizza
  print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
total_bill = 0
if size == "S":
  total_bill = 15
  if add_pepperoni == "Y":
    total_bill += 2
elif size == "M":
  total_bill = 20
  if add_pepperoni == "Y":
    total_bill += 3
else:
  total_bill = 25
  if add_pepperoni == "Y":
    total_bill += 3

if extra_cheese == "Y":
  total_bill += 1

print(f"Your final bill is: ${total_bill}.")

#love calculator
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
true = 0
love  = 0
name1 = name1.lower()
name2 = name2.lower()
full_name = name1 + name2
true += full_name.count("t") + full_name.count("r") + full_name.count("u") + full_name.count("e")
love += full_name.count("l") + full_name.count("o") + full_name.count("v") + full_name.count("e")
total = int(str(true) + str(love))
if total < 10 or total > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")


