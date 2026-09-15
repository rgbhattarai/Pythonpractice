##Write a Python function to find the maximum and minimum elements in a given list.

input = [3,1,4,1,5,9]

## Find max and min element
max = 0


for x in input:
    if x>max:
     max = x
min = input[0]
for y in input:
    if y<min:
     min = y
print(max,min)

#Write a Python function to remove duplicates from a list while preserving the order.

Inputs= [1, 2, 2, 3, 4, 4, 5]
outputs = []
for x in Inputs:
    if x not in outputs:
     outputs.append(x)
print (outputs)

##Write a Python function to find the intersection of two lists.
input1= [1, 2, 3, 4]
input2= [3, 4, 5, 6]
output12=[]

for i in input1:
  if i in input2:
    output12.append(i)
print(output12)