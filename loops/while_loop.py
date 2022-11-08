counter = 1
# print the counter variable as long as its less or equal to 10
while counter <= 10:
    print(f'Cycle number:{counter}')
# if the counter variable is not increased by one after
# each cycle we get an infinite loop
# because counter will then remain at 1 forver and while condition is never met
    counter = counter + 1