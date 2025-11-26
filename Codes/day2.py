# Day 2 — Operators, Expressions, Truthiness, Eval Tool

# Arithmetic & boolean examples
print(5 % 2)
print(5 // 2.5)
print(True + False + True + False + False)
print(True + True + (4 * 2))

# Truthiness examples
print(bool(0), bool("32"), bool([]), bool({}))
print(bool(set()))

# Function example
def f(name):
    return name

print(f(2))

# Loop
for i in range(4):
    print(i, end=" Buck ")

print()

# Ternary operator
res = "yay!!" if 0 > 1 else "nay"
print(res)

# Data structure types
li = list()
se = set()
dic = dict()
tup = tuple()
print(type(li), type(se), type(dic), type(tup))

# Expression tester (safe eval)
expression_input = input("Enter expression: ")

try:
    result = eval(expression_input, {"__builtins__": None}, {})
except Exception:
    print("Invalid expression")
else:
    print(f"Result: {result}")
