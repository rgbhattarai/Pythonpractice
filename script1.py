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

data = [10,40,40,40,30,30]

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

## Max count

data = [10,20,20,30,31,39]

for x in data:
     max=0
     if max>x:
         max=x

print ('max number:', x)

##Min value

print(d1)

## repeated number in dic
maxk = 0
max_num = 0
for key in d1:
    value = d1[key]
    if value> maxk:
        maxk = value
        max_num = key
print ('max value:', max_num, value)

## count number of vowel
input = 'Hello World'
count = 0
vowel = ['a','e','i','o','u']
for ch in input:
    print (ch)
    if ch in vowel:
     count = count+1
print (count)

## iterate on two list

list1 = ['a','b','c']
list2 = [1,2,3]
d={}
for i in range(len(list2)):
    value1 = list1[i]
    value2 = list2[i]
    d[value1]= value2
print (d)