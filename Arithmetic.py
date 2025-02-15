# arithmetic Operations in Python 
# integer 

print('Addition:', 1+2 )
print('Substraction:', 2-1)
print('Multipication:', 2*1)
print('Division:', 6/2)
print('Division:', 7/2)
print('Exponential:', 3**2)

# floating numbers
print('Floating Number, PI' 3.14 )
print('Floating Number, Gravity' 9.81 )

# Complex numbers
print('Complex number:', 1+ 1j)
print('Multiplying Complex  Number: ',  (1+1j) * (1-1j))

# Declaring the variable at the top the top first

a= 3# a is a variable name and 3 is an integer data type
b= 2# b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result of to a variable
total = a+b
dif = a-b
product = a*b
division = a/b
reminder = a % b
floor _division = a// b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function to avoid overriding built-in functions
print(total ) # if you don't label your print with some string, you never know where is the result is coming
print('a +b = ', total)
print('a - b = ', diff)
print('a *b = ', product)
print('a /b = ', division)
print('a % b = ', reminder )
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together 
num_one = 3
num_two = 4

# Arithmetic operations 
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with labels 
print('total: ', total)
print('difference: ', diff)
print('product:', product)
print('division: ', div)
print('remainder: ', remainder)

# Calculating area of a circle 
radius = 10
area_of_circle = 3.14 * radius ** 2
print('Area of a circle:', area_of_circle )

# Calculating area of a rectangle 
length = 10
width = 20
area_of_rectangle = length * width 
print('Area of rectangle: ', area_of_rectangle)

# Calculating a weight of an object 
mass = 75
Gravity = 9.81
weight = mass * Gravity
print(weight , 'N')


print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison 
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Abdulkadir', 'A' in 'Abdulkadir') # True - A found in the string
print('B in Abdulkadir ', 'B' in 'Abdulkadir') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False





