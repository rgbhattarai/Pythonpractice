#clean an email and split it into username and domain


def write_log (message):
    with open (r"C:\Users\bhatt\OneDrive\Desktop\Python_learning\app.log", 'a') as file:
        file.write(message + "\n")


write_log ("App started ")

def clean_split_email(email):
    cl_email = email.strip().lower()

    username, domain = cl_email.split("@")
    return {'username': username , 'domain': domain}

#print(clean_split_email ("rushie@gmail.com"))

# check if email is valid 

def is_valid_email (email): 
    return '@' in email and '.' in email
    

#print (is_valid_email("rushiegmail.com"))
#print (is_valid_email("rushie@gmail.com"))
def process_user_email(email):
    write_log ("App Started")
   
    if not is_valid_email (email):
        write_log (f'invalid email recieved: {email}')

    else: 
        clean_email =  clean_split_email(email)
        write_log (f'processed email {clean_email}')

    write_log ("App stopped")

email = input ("please enter email address: ")
process_user_email(email)