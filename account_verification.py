# account_verification
# this program to login account
def sign_in():
    global name 
    global password
    name = input("User Name: ")
    
    password = input("Password: ")
    print("Account successfully created")


def log_in():
    name1 = input("User Name: ")
    
    password1 = input("Password:")

    if name1 == name and password1 ==password:
        print("Login successful.")
    elif name1 == name and password1 != password:
        print("incorrect password, please try again.")
    elif name1 != name and password1 == password:
        print("incorrect user name.")
    else:
        print("Access denied.")


print("********************************")
print("***********Sign Up************")
sign_in()
print("********************************")

print("********************************")

print("************LogIn***************")

log_in()

print("********************************")
