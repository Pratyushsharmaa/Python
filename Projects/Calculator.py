def add(num1, num2):
  return num1+num2

def subtract(num1, num2):
  return num1-num2

def multiply(num1, num2):
  return num1*num2

def division(num1, num2):
  return num1/num2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": division
}

n1 = int(input("First number: "))
n2 = int(input("Second number: "))
for symbol in operations:
  print(symbol)
  operation_symbol = input(f"Pick an operation from the line above: ")
  calculate_function = operations[operation_symbol]
  answer = calculate_function(n1, n2)
  print(f"{n1} {operation_symbol} {n2} = {answer}")
  