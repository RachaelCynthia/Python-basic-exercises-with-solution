year = {1992, 2003, 2019, 1887, 1990}
year1= {2000, 1870, 1990}

#Find the size of a Set in Python
print(len(year))

#Iterate over a set in Python
for date in year:
    print(date)

#Maximum and Minimum in a Set
print(max(year), min(year))

#Remove items from Set
year.remove(1887)
print(year)

#Check if two lists have atleast one element common
check = set(year) & set(year1)
if check:
    print("True")
else:
    print("False")
