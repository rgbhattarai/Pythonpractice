
## String function practice

a= 'hello World'
print(a.upper())  ## upper() method change it to uppercase
print(a.lower()) ## lower() change it to lower case

b= ' hello world!  '
print(b.strip()) ## The strip() method removes any whitespace from the beginning or the end:

# The replace() method replaces a string with another string:
print(b.replace('h','j'))

##Flatten a Nested List Write a Python function to flatten a nested list  Input: [[1, 2], [3, 4], [5]]
##0utput: [1, 2, 3, 4, 5]*/

Input= [[1,2],[3,4],[5]]
output=[]

for i in Input :
    output.extend(i)
print(output)


##Merge Two Sorted Lists
##Write a Python function to merge two sorted lists into a single sorted list.
##Input: [1, 3, 5], [2, 4, 6]
##Output: [1, 2, 3, 4, 5, 6]

Input11= [1,3,5]
Input22= [2,4,6]
output12=[]

for x in Input11 ,  Input22:
         if
          output12.append(x)
        else :
            output.append(y)
print(output12)




 ##Find All Pairs in a List that Sum to a Specific Value
####Write a Python function to find all pairs in a list that sum to a specific value.
#3Input: [1, 2, 3, 4, 5], Sum=6
##Output: [(1, 5), (2, 4)]
Input3=[1, 2, 3, 4, 5]
output3=[]
Sum =6

for x in Input3:
  for y in Input3:
    if  x+y==Sum :
        print(x,y)
        break




