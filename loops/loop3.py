# empty text variable for the loop to fill later
text = ''
# for loop,add new years to the text variable
#one year

for year in range(2019,2023):
    text = text + str(year) + '-'

# remove the last dash by using substring
text = text[0:-1]
print(text)