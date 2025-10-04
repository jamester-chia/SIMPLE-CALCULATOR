# num_one = int(input("input a number: "))
# operation = input("input an operation: ")
# num_two = int(input("input a number: "))

def calc():
  num_one = int(input("input a number: "))
  operation = input("input an operation: ")
  num_two = int(input("input a number: "))
  if operation == "+":
    result = (num_one + num_two)
    return result
  if operation == "-":
    result = (num_one - num_two)
    return result
  if operation == "*":
    result = (num_one * num_two)
    return result
  if operation == "/":
    result = (num_one / num_two)
    return result
  if operation == "**":
    result= (num_one ** num_two)
    return result 
    
  else:
    print("syntax error")


result = calc()
print(result)



