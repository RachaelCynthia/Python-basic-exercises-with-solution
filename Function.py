#How to get list of parameters name from a function in Python?
def greeting(hello, sir):
    return a+b
import inspect

print(inspect.signature(greeting))

#How to Print Multiple Arguments in Python?
def introduction(name, age, state):
    print("My name is ", name + ', I am ' + age, 'years old and I am from ' + state, 'state.')
introduction("Raymond", "35", "Ondo")

#Python program to find the power of a number using recursion
def recuraion(B, P):
    if P == 0:
        return 1
    return (N*power(B, P-1))
#if __name__ == '__main__':
    B = 2
    P = 3
    print(power(B, P))


#Sorting objects of user defined class in Python
class NAME_AGE:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return str((self.name, self.age))

name_age = [NAME_AGE("Ray", 35),
            NAME_AGE("Lekan", 20),
            NAME_AGE("Bisola", 27),
            NAME_AGE("Esther", 13),
            NAME_AGE("Oyindamola", 10)
            ]
print(sorted(name_age, key=lambda x: x.age))


#Functions that accept variable length key value pair as arguments
def printKwargs(**kwargs):
    print(kwargs)

if __name__ == "__main__":
    printKwargs(Name_1='Raymond', Name_2='Akinyemi')
