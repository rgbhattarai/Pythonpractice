
##Write a program to reverse a string without using slicing.
##Example: Input: “python” Output: “nohtyp

input12='Python'
reverse =' '

for x in input12:
    reverse = x+reverse
print (reverse)

##Find the first non-repeating character in a string.
##Input: “programming” Output: “p”

inputs = 'programming'


for ch1 in inputs:
    count=0
    for ch2 in inputs:
       if ch1==ch2:
           count=count+1
    if count==1:
     print (ch1)
     break

##Check if a string is a palindrome.
#Example: Input: “madam” Output: True

text = 'madam'
reverse=''
for x in text:
    reverse = x+reverse

if reverse==text:
   print('is it pallindrome:',True )
else:
   print(False)

##Count the frequency of each character in a string.
##Example: Input: “hello” Output: h:1 e:1 l:2 o:1

text1= 'hello'
text_output = {}
count=0
for x in text1:
    if x in text_output:
        text_output[x] =text_output[x]+1

    else:
        text_output[x]=1
print(text_output)

##Remove duplicate characters from a string while preserving order.
##Example: Input: “programming” Output: “progamin”

input1= 'programming'
input2=''
output1=''

for ch in input1: ##p,r
    if ch not in output1:
        input2 = input2+ch  ##prog,
    output1=output1+ch #prog

print(input2)

##Remove duplicates from a list without using set().
##Example: Input: [1,2,2,3,4,4] Output: [1,2,3,4]

input3= [1,2,2,3,4,4]
output2=[]
for n in input3:
    if n not in output2:
        output2.append(n)
print(output2)

##Find the second largest number in a list.
##Example: Input: [10,20,5,30,25] Output: 25

input4=[10,20,5,30,25]

input4.sort()
print (input4[-2])

##Find all duplicate elements in a list.
##Example: Input: [1,2,3,2,4,5,1] Output: [1,2]

input5= [1,2,3,2,4,5,1]
output3=[]
count = 0

for  x in input5:
    if x not in output3 and input5.count(x)>1:
     output3.append(x)

print (output3)

##Rotate a list by K positions.
##Example: Input: [1,2,3,4,5], K=2 Output: [4,5,1,2,3]

input6= [1,2,3,4,5]
k=2
output4= input6[-k:] + input6[:-k]

print(output4)

##Find the intersection of two lists.
##Example: Input: [1,2,3,4] [3,4,5,6]
##Output: [3,4]
input7= [1,2,3,4]
input8=[3,4,5,6]
output5=[]

for x in input7 :  ##1
    for y in input8:  ## 1
      if x==y:
        output5.append(x)
print(output5)

##Count frequency of elements in a list using a dictionary.
##Example: Input: [1,2,2,3,3,3] Output: {1:1, 2:2, 3:3}

input9= [1,2,2,3,3,3]
output6={}

for x in input9:
    if x in output6:
        output6[x]= output6[x]+1
    else:
        output6[x]=1
print(output6)

##Find the key having the maximum value.
##Example: {“A”:100,“B”:500,“C”:300}
##Output: B

input10={'A':100,'B':500,'C':300}
max=0
max_key=''
for x in input10:
    if input10[x] >= max:
        max = input10[x]
        max_key = x
print (max_key)

##Reverse a dictionary.
##Example: {“a”:1,“b”:2}
##Output: {1:“a”,2:“b”}

input11= {'a':1,'b':2}
rev_output={}

for x in input11:
    rev_output[input11[x]] = x
print(rev_output)

##Merge two dictionaries.
##Example: d1={“a”:1} d2={“b”:2}
##Output: {“a”:1,“b”:2}

d1={'a':1}
d2={'b':2}
d={}

for x in d1:
    d[x] = d1[x]
for x in d2:
    d[x] = d2[x]
print(d)

##Count word frequency in a sentence using dictionary.
##Example: Input: “python is good python is easy”
##Output: { “python”:2, “is”:2, “good”:1, “easy”:1 }

input12='python is good python is easy'
input13 = input12.split()
output7={}

for x in input13:
    if x in output7:
        output7[x]= output7[x]+1

    else:
        output7[x]=1
print(output7)

##Print the following pattern:
##   **
for x in range(2):
    y='*'
print(y,end='')
print(" ")

##Print multiplication table of a given number.
##Example: Input: 5
##Output: 5 x 1 = 5 … 5 x 10 = 50
table_output=0
for x in range(10):
    table_output=  table_output+5
    print(table_output)

##Find factorial using for loop.
##: 5 Output: 120
factorial = 1
for x in range(1,6):
    factorial = factorial * x
    print(factorial)

##Find all prime numbers between 1 and 100.

for x in range (1,101):
    count = 0

    for y in range(1, x+1):
        if x%y==0:
            count =count+1

    if count==2:
     print(x ,'is prime number')
##Generate Fibonacci series up to N terms.
##Example: Input: 8
##Output: 0 1 1 2 3 5 8 13

number = 8
a=0
b=1
for x in range(0, number+1 ):
    fibonacci  = a+b
    a=b
    b=fibonacci
    print(fibonacci)