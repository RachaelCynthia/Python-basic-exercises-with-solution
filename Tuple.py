#Find the size of a Tuple
coordinates = (8.2265, 5.9874)
print(len(coordinates))

#Maximum and Minimum K elements in Tuple
print(max(coordinates))
print(min(coordinates))

#Sum of tuple elements
print(sum(coordinates))

#Row-wise element Addition in Tuple Matrix
matrix = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (0)
]
for row in matrix:
    print(row)

#Create a list of tuples from given list having number and its cube in each tuple
given_set_of_numbers = [2, 3, 4, 5, 6, 7]
tuple_cube_formed = [(num, pow(num, 3)) for num in given_set_of_numbers]
print(tuple_cube_formed)
