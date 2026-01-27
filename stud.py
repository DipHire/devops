print("\n ------- Student Registration Form --------\n")

name = input("Enter Name: ")                     
age = int(input("Enter Age: "))                  
gender = input("Enter Gender: ")                 
mobile = input("Enter Mobile Number: ")          
branch = input("Enter Branch: ")                 
email = input("Enter Email ID: ")                
address = input("Enter Address: ")               
pin = input("Create a PIN: ")                    

print("\n Student Registration Successfully Completed !\n")

login_pin = input("Enter PIN to verify: ")

if login_pin == pin:
    print("\n ------- Student Registration Form --------\n")
    print(f"Name    : {name}")
    print(f"Age     : {age}")
    print(f"Gender  : {gender}")
    print(f"Mobile  : {mobile}")
    print(f"Branch  : {branch}")
    print(f"Email   : {email}")
    print(f"Address : {address}")
else:
    print("\nWrong PIN")