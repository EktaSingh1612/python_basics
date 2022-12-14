# Variable - It is alike a container that holds data. It is like creating a placeholder in memory and assigning it some value.

a = 1 # 'a' is a variable that holds the address of where '1' is stored in the memory.
b= 'Virat Kohli'
c = True
d = None
e ='1'

# These are all different data types
# Data type - It specifies the type of value a variable holds. This is required in programming to do various opeerations without causing an error.
print(a) # integer
print(b) # string
print(c) # boolean
print(d) # none type
print(e) # string

'''
Built-in data types
1. Numerical data : int (1,-5,0), float ( 2.9.-3.0), complex (5+2i)
2. Text data : str (under single or double qoutes)
3. Boolean data : True and False
4. Sequence data : list, tuple
'''
# to print type of any function
print(type(a))
print('the type of a is ',type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
# to assign a type to a variable
f=complex(8,2)
print(type(f))

'''
list : ordered collection of data with elements seperated by a comma, and enclosed within square brackets [1,'this is a list', True]
Lists are mutable and can be modified after creation
'''
list1 = [8,2.3,[-4,5],['apple','banana']]
print(list1)

'''
tuple : ordered collection of  data with elements seperated by commma and enclosed within parentheses. Tuples are immutable and cannot be modified after creation ()
'''
tuple1 = (('apple','banana'),('lion','tiger'))
print(tuple1)

'''
5. Mapped data : dict

dict : it is a unordered collection of data containing a key:value pairs.
the key:value pairs are enclosed within curly brackets {key:value}
'''
dict1 = {'name':'virat', 'age':34, 'canBat':True}
print(dict1)