from agents import function_tool

@function_tool
def plus(a:int ,b:int):
    return f"Your answer is {a + b}"

@function_tool
def subtract(a:int ,b:int):
    return f"Your answer is {a - b}"

@function_tool
def multiply(a:int ,b:int):
    return f"Your answer is {a * b}"

@function_tool
def divide(a:int ,b:int):
    return f"Your answer is {a / b}"

