#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

print(admin_login("admin", "12345"))  # Output: Access granted
print(admin_login("Admin", "12345"))  # Output: Access granted
print(admin_login("user", "12345"))   # Output: Access denied
print(admin_login("admin", "54321"))  # Output: Access denied
print(admin_login("ADMIN", "12345"))  # Output: Access granted

    

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
print(hows_the_weather(35))  # Output: It's brisk out there!
print(hows_the_weather(50))  # Output: It's a little chilly out there!
print(hows_the_weather(90))  # Output: It's too dang hot out there!
print(hows_the_weather(75))  # Output: It's perfect out there!

    

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
       return "FizzBuzz"
    elif num % 3 == 0:
       return "Fizz"
    elif num % 5 ==0:
       return "Buzz"
    else :
       return num
    
print(fizzbuzz(3))    # Output: Fizz
print(fizzbuzz(5))    # Output: Buzz
print(fizzbuzz(15))   # Output: FizzBuzz
print(fizzbuzz(7))    # Output: 7
   
def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print("Invalid operation!")
        return None

