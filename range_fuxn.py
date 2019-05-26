#### 11 / 05 / 2019
#### Author Geofrey Manacce
#### Using the range fuction

#### suing the range fuction

for value in range(1,6):
	print(value)

print("The end of the fist loop")

for month in range(1,13):
	print(month)
print("The start of second for loop")

###HOW TO CONVERT LIST

numbers = list(range(1,101))
print(numbers)

print("THE END OF NUMBERS" + "\n")

odd_numbers = list(range(1,201,2))
print(odd_numbers)

print("THE END OF OOD NUMBERS" + "\n")

number = list(range(2,201,4))
print(number)

print("The end of the list number" + "\n")

squares = []
for value in range(1,101):
	square = value**2
	squares.append(square)
print(squares)

print("The end of the for loop function " + "\n")
####simple opperations withn list

digits = list(range(1,101))

print(sum(digits))
print("\n")

print(min(digits))
print("\n")

print(max(digits))
print("end of this part" + "\n")


##### HOW TO SLICING OF A LIST

birthday_months = ['january','february', 'match', 'april', 'may','june','july','august','september','october','november','december']
print(birthday_months[0:2])
print(birthday_months[3:9])
print(birthday_months[3:])
print(birthday_months[0:])
print(birthday_months[-12])
print(birthday_months[:8])
print(birthday_months[7:12])
print(birthday_months[5:11])
print("The end of the slicing program" + "\n")

#####LOOPING THOUGH A SLICE WITH A FOR LOOP

print("Here are the last four birthday_months of my friends")

for birthday_month in birthday_months[:3]:
	print(birthday_month.title() + "\n")

print("My friends born in middle of the year")

for month_day in birthday_months[5:8]:
	print(month_day.title() + "\n")

###### how to copy a list
months_of_the_year = birthday_months[:]
print(months_of_the_year )
