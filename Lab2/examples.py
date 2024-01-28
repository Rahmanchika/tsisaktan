
# Python Examples from W3Schools by aktan

# Booleans
print(True)
print(False)
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Operators
# Arithmetic Operators
print(10 + 5)  # Addition
print(10 - 5)  # Subtraction
print(10 * 5)  # Multiplication
print(10 / 5)  # Division
print(10 % 5)  # Modulus
print(10 ** 5) # Exponentiation
print(10 // 5) # Floor division

# Assignment Operators
x = 5
x += 3
print(x)
x *= 3
print(x)

# Comparison Operators
print(x == 8)
print(x > 7)
print(x < 11)

# Logical Operators
print(x > 3 and x < 10)
print(x > 3 or x < 4)
print(not(x > 3 and x < 10))

# Identity Operators
print(x is 5)
print(x is not 5)

# Membership Operators
print(3 in [1, 2, 3])
print(4 not in [1, 2, 3])

# Bitwise Operators
print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(~5)
print(5 << 2)
print(5 >> 2)

# Lists
mylist = ["apple", "banana", "cherry"]
print(mylist)
print(mylist[1])
mylist[1] = "blackcurrant"
print(mylist)
for x in mylist:
    print(x)

# Tuples
mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(mytuple[1])
for x in mytuple:
    print(x)

# Sets
myset = {"apple", "banana", "cherry"}
print(myset)
for x in myset:
    print(x)

# Dictionaries
mydict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(mydict)
print(mydict["model"])

# If...Else
a = 33
b = 200
if b > a:
    print("b is greater than a")

# While Loops
i = 1
while i < 6:
    print(i)
    i += 1

# For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
