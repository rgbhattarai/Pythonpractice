# Store application log messages into file

def write_log (message):
    with open (r"C:\Users\bhatt\OneDrive\Desktop\Python_learning\app.log", 'a') as file:
        file.write(message + "\n")


write_log ("App started ")