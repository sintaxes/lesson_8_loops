# Create a program witch takes 5 different (minmum)  variables containing strings for username and password.
# The string should look like : "username='', password=''; username='',password='';....etc"
# Start Endless loop allowing to enter username and password and 
# check ff credentials are correct stop endless loop and print greeting message, otherwise print 'wrong credentials' and ask to enter password and username again. 
# The program should show numbers of times you tried to enter both credentials.

# For storing account information use dict , all data should be lowercase. and extra symbols (@, %, $ etc and numbers). 
# If in password numbers or symbols are not provided, the program should add additional value to dictionary as a value, names 'improved password'


print("You will need to enter five user names and passwords")

credentials_list = {}

for enter in range(2):
    username = input(f"Enter user name {enter+1}: ")
    password = input(f"Enter user password {enter+1}: ")
    credentials_list[username] = password

print("Now you will need to enter user name and correct password you eneterd before")


while True:
    login_username = input("Enter your user name: ")
    login_password = input("enter your password: ")

    if login_username in credentials_list and credentials_list[login_username] == login_password:
        print("Your credentials are correct")
        break
    else:
        print(" Your credentials are not correct, try again. ")





print("You will need to enter five user names and passwords")


input_string = input ("username='qwerty', password='as0dfg'; username='zxcvbn', password='bnm'")
input_string=input_string.replace(" ","").lower()
input_list = input_string.split(";")

credentials = {}
symbols_in_passwords = "!@#$%^&*()_+,.<>/?0123456789"

for user_list in input_list:
    elems_list=user_list.split(",")
    username=elems_list[0].replace('username=','').replace("'",'')
    password=elems_list[1].replace("password=",'').replace("'",'')
    char_flag = False
    for char in symbols_in_passwords:
        if char in password:
            char_flag = True
    if char_flag == True:
        credentials[username]=password        
    else:        
        print("You password is too weak")
    



while True:
    login_username = input("Enter your user name: ").lower()
    login_password = input("Enter your password: ").lower()

    if login_username in credentials and credentials[login_username] == login_password:
    # if login_username in credentials.keys() and credentials[login_username] == login_password:
        print("Your credentials are correct")
        break
    else:
        print(" Your credentials are not correct, try again. ")
    








