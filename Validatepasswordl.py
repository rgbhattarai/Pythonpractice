#vaidate quality and correctness of the password

password= "Rushieeeb"
email="Rushieb"
password = password.strip()
email= email.strip()

#Must not be empty
if password == "":
    print("password must not be empty")
# password must be atleast  8 character 

elif (len(password)<8):
    print ("password must be atleast 8 character")

# password must include atleast 1 uppercase
elif not any(char.isupper() for char in password):
    print("password must contains atleast one upper case ")

# password must include atleast 1 lowerrcase
elif not any(char.islower() for char in password):
    print("password must contains atleast one lowerper case ")

#must not be same as the email

elif  password == email :
    print("password and email must not be same")

#must not contain any spaces

elif not any(char.isspace() for char in password) :
    print("Password must not contain any space")

#Must start and end with letter or digit

elif not(password[0].isalnum() and password[-1].isalnum()):
    print("password must starts and ends with alphanumeric")


else:
    print("password is valid")



