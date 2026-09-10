email = "rR am"


# clean email and other empty space 
email = email.strip()


if email== "":
    print("email cannot be empty")
elif any(char.isspace() for char in email) :
    print("ghgj")
else:
    print("ppp")