#ask the user for two numbers
number_1 = int(input('Enter a number: '))
number_2 = int(input('Enter another number: '))
# divide the first number by the second number

result = float(number_1 / number_2)
print(result)

# if the user inputs text,print a message,invalid inputs
if type(number_1) == str or type(number_2) == str:
    print(f'Invalid inputs')    
#if the user divides by zero, print "cannot divide by zero".use exception handling(try/except)
elif number_2 == 0:
    try:
        number_1 / number_2
    except ZeroDivisionError:
        print(f'Cannot divide by zero')