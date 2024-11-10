import time
import math
import calendar
import email
import warnings as warn
import webbrowser as web
import random
import zipfile as zip
import os
# That's all we need for the modules, as we have pretty much everything we need.
def calculate(operation, num1, num2):
    if operation == 'add' or operation == '+':
        opSys = "+"
        return num1 + num2
    elif operation == 'subtract' or operation == '-':
        opSys = "-"
        return num1 - num2
    elif operation == 'multiply' or operation == '*':
        opSys = "*"
        return num1 * num2
    elif operation == 'divide' or operation == '/':
        opSys = "/"
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return "Error: Invalid operation."

# Main script
print("Welcome to the calculator!")


# Run the system
while True:
  print("Commands: time, calc")
  command = str(input("KITSUNE-CMD: "))
  if command == "time":
    now = time.time()
    currenttime = time.strftime("%Y-%m-%d %H:%M:%S")
    print("The current time is: " + currenttime)
  elif command == "calc":
    operation = input("Enter a math operation (add, subtract, multiply, divide, +, -, *, /): ").strip().lower()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = calculate(operation, num1, num2)
    print(f"{num1} {opSys} {num2} = {result}")
    
