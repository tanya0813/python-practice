#Functions for operations

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

#user input
print('Please select the operation:\n'\
      '1.Addition\n' \
      '2.Subtraction\n' \
      '3.Multiplication\n' \
      '4.Division\n')

select=int(input('Select operation from 1 to 4: '))

# Check if the selection is valid before asking for numbers
if select in [1, 2, 3, 4]:
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))

#Print the result
if select==1:
    print("Sum of two numbers is: ",add(a,b))

elif select==2:
    print("Subtraction of two numbers is: ",sub(a,b))

elif select==3:
    print("Multiplication of two numbers is: ",mul(a,b))

elif select==4:
    print("Division of two numbers is: ",div(a,b))

else:
    print('Invalid Operation. Please select a valid operation!')