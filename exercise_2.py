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









