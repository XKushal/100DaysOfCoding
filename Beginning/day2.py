#day-2: Data types, Operations, Type Conversion, f-Strings

#String
#subscripting  = pulling out each stuff from that particular position
print("Hello"[0])

#Integer
1_2_3 #same as 123

#Float
3.14159

#Boolean
True 
False

# Typecheck type(), Typecasting = str(), float()
num_char = len(input("Whats your name?"))
print(type(num_char))
num_str = str(num_char)
print("your name has " + num_str + " Characters.")

#Adds a digit in 2 digit number
two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇

#solution1
a = float(two_digit_number) % 10
b = float(two_digit_number) / 10
print(int(a) + int(b))

#solution2
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
print(first_digit+ second_digit)

#Mathematical Operations: +,-,*,/ (division always has floating number), ** (exponent. 10^2==10**2)
# 1st input: enter height in meters e.g: 1.65
height = int(input())
# 2nd input: enter weight in kilograms e.g: 72
weight = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
print("BMI is: ", weight/(height ** 2))

#round()
print(round(8/3, 2))
#floor division
print(7//2) #result =3

#f-string = 
score  = 0 
height = 1.2
isWinning = True
print(f"your score is {score}, your height is {height} and you are winning is {isWinning}")

#number of weeks left on Earth

x = input("your age: ")
age_left = 90 - int(x)
weeks = age_left * 52
print(f"You have {weeks} weeks left.")

#tip Calculator 

print("Welcome to the tip calculator!\n")
total_bill = input("what was the total bill?")
tip = input("How much tip would you like to give? 10, 12, or 15?")
spilit = input("How many people to spilit the bill?")
total = round((float(total_bill) + (float(total_bill) * (float(tip)/100)))/float(spilit), 2)
print(f"Each person should pay: {total}")