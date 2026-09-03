
##Write a program to reverse a string without using slicing.
##Example: Input: “python” Output: “nohtyp

input='Python'
reverse =' '

for x in input:
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
num=input4[0]
nums=input4[0]
count=0

for x in input4:
    
    if x>num and x> num+1:
        nums = x

