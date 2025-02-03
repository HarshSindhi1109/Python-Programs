import ast

a = ast.literal_eval(input("Enter first number="))
b = ast.literal_eval(input("Enter second number="))

print(a + b)

'''
ast.literal_eval() safely evaluates strings containing Python literals (like numbers, strings, lists, etc.).
It converts the input to the appropriate type automatically.
'''