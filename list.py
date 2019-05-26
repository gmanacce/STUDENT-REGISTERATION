########Date 3/5/2019
########AUTHOR Geofrey Manacce

####HOW TO EDIT LIST

months = ['january','february','march','april','may','june','jully','august','september','ocober','november','december']

date_of_birth = 25

my_fiancee_date_of_birth = 28


print(months)

#how to excute a value accoding to it's position in the list
print(months[11])

my_birthday = "i was born in " + months[3].title() + " of " + str(date_of_birth) + " 1989 ."

birthday_of_my_fiancee = "My fiancee was born in " + months[7].title() + " of " + str(my_fiancee_date_of_birth) + " 1988."

print(my_birthday)

print(months[0].title())

print(my_fiancee_date_of_birth)

print(birthday_of_my_fiancee)

#######how to create list of members of the family

my_family_members = ['manacce', 'boniphace', 'Ruth', 'joyce', 'geofrey', 'janeth', 'johnson', 'robert', 'eliana', 'leoncia']

print(my_family_members)

######how to add a new member of my family after get marriage!

my_family_members.append('ausher')

print(my_family_members)

######how to replace a value or any other argument in the list

my_family_members[4] = "ng\'undineza"

print(my_family_members)

#######how to create an empty list

my_family_members = []

print(my_family_members)


#######how to add a value or a member in an empty list using append method

my_family_members.append('ZINAIDA'.title())

print(my_family_members)

#####how to add a new member/value to already listed with the respect of it's position in the list using insert method

my_family_members.insert(0 , 'paul'.title())

print(my_family_members)


#####how to delete a value or member to a certain list by using delete statement

del my_family_members[1]

print(my_family_members)

