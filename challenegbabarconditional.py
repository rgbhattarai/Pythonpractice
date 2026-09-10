# next way of writing checking each and every condition 
email = "*Rushie@@.co "
valid=True


# clean email and other empty space 
email = email.strip()

if email== "":
    print("email cannot be empty")
    valid=False

# email  must contain a . and @ 
if not ("." in email and "@" in email):
    print("email must contain . and @")
    valid=False

#email must contain exactly one @ symbol 

if email.count("@") != 1:
    print("email must contain only one @")
    valid=False

# email must contain .com, .net or .org
if not email.endswith((".com", ".org",".net")):
    print("email must ends with .com, .net or .org")
    valid=False

    # email must me longer than 254 character 
if len(email)>254:
    print("email must not be longer than 254")
    valid=False

# email must starts and ends with letter and digit

if not (email[0].isalnum() and email[-1].isalnum()):
    print("email must starts and ends with letter or digit")
    valid=False

if valid:
    print("email is valid")