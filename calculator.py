a = input("enter first value: ")
a_digit = int(a)

operation = input("enter operation: ")

b = input("enter second value: ")
b_digit = int(b)

if operation == '+':
    result = a_digit + b_digit
elif operation == '-':
    result = a_digit - b_digit
elif operation == 'x':
    result = a_digit * b_digit
elif operation == '/':
    result = a_digit / b_digit


print(result)
