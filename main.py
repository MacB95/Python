def add(num1, num2):
 return num1 + num2

def subtract(num1, num2):
 return num1 - num2

def multiply(num1, num2):
 return num1 * num2

def divide(num1, num2):
 return num1 / num2

print ("Calculator v2")
print("______________________")

num1 = float(input("Enter a number: "))
operand = input("+, -, *, / : ")
num2 = float(input("Enter a number: "))

if operand == "+":
 print(num1, "+", num2, "=")
 result = add(num1, num2)
 print("______________________")
 print(result)
elif operand == "-":
  print(num1, "-", num2, "=")
  result = subtract(num1, num2)
  print("______________________")
  print(result)
elif operand == "*":
  print(num1, "*", num2, "=")
  result = multiply(num1, num2)
  print("______________________")
  print(result)
elif operand == "/":
  print(num1, "/", num2, "=")
  result = divide(num1, num2)
  print("______________________")
  print(result)
else: 
 print("Unknown Input")