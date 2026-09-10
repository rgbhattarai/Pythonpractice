# Validate the Quality and correctness of the email value


#email must not be empty
email = "rushie@jj.net "

if email== " ":
    print("Must enter valid email ID")
else: 
    print("valid email ID")
if "." and "@" in email:
    print("correct email ID")
else: 
    print("enter . and @ in email")
if email.endswith(".com" or ".org" or ".net"):
    print("Email looks great")
if len(email)>254:
    print("email length shouild be less than 254 character")
if (email.startswith(str) or email.startswith(int)) and  (email.endswith(str) or email.endswith(int)):
    print("great perfect email yo hoo")
else:
    print("email conformation failed")








 
