######19/05/2019
######Geofrey Manacce
######using a key to get a value from a dictionary

###create a dictionary of terms

terms = {'variables' : 'represents or refers to a value stored in memory'}

print(terms['variables'])
print('\n')
print('down is the alternative to retrive a value from a dictionary')

#########altenatives 

terms = {}

terms['variables'] = 'represents or refers to a value stored in the memory'
terms['integer'] = 'a whole number'

print(terms['variables'])
print(terms['integer'])

########The other way to retrive value from the dictionary by using the Get method
###using the get() method
print('how to retrive a value from a dictionary\n')
term = {'integer' : 'a whole number'}
print(term.get('integer'))
print('how to retrive a value which is not in the dictionary\n')
print(term.get('float',' not in the dictionary'))

#########how to edit and delete value in  dictionary

terms = {'integer' : 'is the number that contain a decimal place'}
print(terms)

####how to edit a value or add a value in the dictionary
terms = {'variables': 'is the number that contain a decimal place', 'integer': 'a whole number'}
print(terms)

###how to delete a value from the dictionary
terms = {'variables': ' is the number that contain a decimal place', 'integer': 'a whole number'}
del terms['variables'] 

print(terms) 


        



