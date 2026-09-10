# create a new dict 

user = {'id': 1, 'name': 'John', 'age': 30, 'City': 'Berlin' }

New_user = {
    k: v.upper()#Expression
   for k, v in user.items() #loop
    if isinstance(v, str)#filter 
}
print (New_user)