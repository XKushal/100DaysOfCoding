# day 1: learning printing, debugging, string manipulation, variables

#print() function
print("A 'single quote' inside a double quote")
print('A "double quote" inside a single quote')
print("Alternatively you can just \"escape\" the quote")

#input() and len() function
print('Hello! ' + input("Whats your name?"))
num1 = int(input())
num2 = int(input())
print("multiply: " , num1*num2)
print("no. of letters: ", len(input()))

#variables
name = input("whats your name?")
print("Your name is: ", name)