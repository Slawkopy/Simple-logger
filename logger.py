"""
Run "pip install colorama"
before running progrem
"""
import os, colorama, datetime

colorama.init(convert=True) # Init colorama with windows conversion (for colors)
print(colorama.Fore.GREEN, colorama.Back.BLACK, end="", sep="") # Print special color characters

print("Logger") # Print title
email = input("Your email: ") # Ask for e-mail
password = input("Your password: ") # Ask for password

filename = "log.txt" # Defile log filename

"""
If file does not exist - create new
Else append to old file
"""
if not os.path.isfile(filename):
    with open(filename, "w") as f:
        write_log(f)
else:
    with open(filename, "a") as f:
        f.write("\n")
        write_log(f)
        

def write_log(file):
    file.write(f"{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}: {email} // {password}\n")  
