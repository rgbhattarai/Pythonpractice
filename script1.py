# practice python

x = 5
y = 'john'
print(x)
print(y)

## Casting - to specify the datatype of the variable
x = str(3)
y= int(3)
z = float (3)
print (x,y,z)

## to get the type of the data

print (type(x),type (y), type (z))

## variable names are case sensitive -- A will not overwrite A

A = 'ram'
a = 'sita'

print (A,a)

# unpack collection - collection of value in list
# or tuple python allows you to extract the value which is called unpacking
Fruits = ['apple','banana','cherry']
x,y,z=Fruits
print (x,y,z)

## Global variable in python are variable created outside the function
## and can be used in both  inside and outside

x= 'awesome'

def myfunc():
    print('Python is'+' '+ x)

myfunc()

## python slicing strings
b = "Hello, World!"
print(b[10:13])
print(b[:13])
b = "Hello, World!"
print(b[:8])
print(b[5:-5])


