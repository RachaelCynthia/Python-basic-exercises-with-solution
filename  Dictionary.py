name_age ={'Ray': 32,
           'Eric': 19,
           'Cynthia': 27,
           'Ifedayo': 16,
           'Esther': 12,
           'Lekan': 22
           }
#Sort Python Dictionaries by Key or Value
print(sorted(name_age.keys()))

#Handling missing keys in Python dictionaries
print(name_age.get('Esther', 'Not Found'))
print(name_age.get('Rachael', 'Not Found'))

#Python dictionary with keys having multiple inputs


#program to find the sum of all items in a dictionary
print(sum(name_age.values()))

#program to find the size of a Dictionary
print(len(name_age))
