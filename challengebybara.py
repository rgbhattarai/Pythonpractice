# Emial must not be empty so for that we need to clean email because email empty but with only space will also gives valid email


email = "*ushie@.com "

if email== "":
    print("email cannot be empty")
else: 
    print("email is validated")

# clean email and other empty space 
email = email.strip()
if email== "":
    print("email cannot be empty")

# email  must contain a . and @ 
elif not ("." in email and "@" in email):
    print("email must contain . and @")

#email must contain exactly one @ symbol 

elif email.count("@") != 1:
    print("email must contain only one @")

# email must contain .com, .net or .org
elif not email.endswith((".com", ".org",".net")):
    print("email must ends with .com, .net or .org")

    # email must me longer than 254 character 
elif len(email)>254:
    print("email must not be longer than 254")

# email must starts and ends with letter and digit

elif not (email[0].isalnum() and email[-1].isalnum()):
    print("email must starts and ends with letter or digit")

else: 
    print("email is valid")

 