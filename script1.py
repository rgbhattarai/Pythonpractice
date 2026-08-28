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

data = [10,20,20,30,31,39]

count =0
counts = 0
occurence=[]
for x in data:
    if x==20:
       count = count + 1
       occurence.append(count)
    if x==30:
       counts = counts + 1
       occurence.append(counts)
print(20,count, 30, counts)
print(occurence)

d1={}
for x in data:
    if x in d1:
     d1[x] = d1[x]+1
    else:
     d1[x]=1
print (d1)













