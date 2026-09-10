# check if user name is not empty and age is greater than or equal to 18

username = "ru"
age = 18 

print(username != " " and age >= 18)

# check if the password is 8 character long and doesnot have have any space 

password = "rushieeb"

print (len(password) ==8  and  " " not in password)

#check if user email is not empty contains @ ends with .com

email = "fghhg@gmail.com"

print (email != " " and "@" in email and email.endswith (".com"))

#check if username is string , is not none and longer than 5 character 

usernames= "rush"

print(type(usernames)== str and usernames is not None  and len(usernames)>=5)

#check if user is either a admin or moderator and either they are not banned or they have verified thier email

user = "admin"
isbanned= False
isverified = True

print((user=="admin" or user== "moderator") and (user!= isbanned or user==isverified))

