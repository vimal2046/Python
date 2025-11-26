# Day 1 — Basics: Data Types, type(), id(), input(), slicing

# Variables of different types
num = 1
num1 = 3.00
var = "Hydra"
var1 = True
c1 = 3 + 4j
value = None

print(f"value is {num}, type: {type(num)}, id: {id(num)}")
print(f"value is {num1}, type: {type(num1)}, id: {id(num1)}")
print(f"value is {var}, type: {type(var)}, id: {id(var)}")
print(f"value is {var1}, type: {type(var1)}, id: {id(var1)}")
print(f"value is {c1}, type: {type(c1)}, id: {id(c1)}")
print(f"value is {value}, type: {type(value)}, id: {id(value)}")

# Safe integer input + sum
input1 = input("Enter an integer: ")
input2 = input("Enter another integer: ")

if input1.isdigit() and input2.isdigit():
    a = int(input1)
    b = int(input2)
    print(f"{a} + {b} = {a + b}")
else:
    print("Invalid input")

# String slicing
word = "PythonBootCamp"
print(word[:3])      # first 3 chars
print(word[-4:])     # last 4 chars
print(word[3:8])     # index 3 to 8
print(word[::-1])    # reverse
print(word[6:10])    # Boot
