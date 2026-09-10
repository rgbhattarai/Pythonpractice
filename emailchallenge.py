# scan emails to block unsafe data from entering you syatem

emails =['bara@gmail.com','rushie@gmail.com','drop table users;','maria@gmail.com']

for email in emails: 
    if ";" in email:
        print("sql injection suspected")
        break
    print (f'email processing:{email}')


print ('=================================')

    
#Finf the missing names

names= ['rushie','ram',None, 'hari'] 

for name in names:
    if names==None:
        print('missing name found')
        break
else:
    print("All names are available")