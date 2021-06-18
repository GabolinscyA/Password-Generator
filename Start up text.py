def generation():
    passw0rds = input("Please enter a random number")
    website = input("Your new password is {}. What would you like this password to be used for?".format(passw0rds))
    file = open("C:/Users/gabolinscya/Desktop/Passwords.txt", "a")
    file.write("\n")
    file.write(website)
    file.write(":")
    file.write("\n")
    file.write(passw0rds)
    file.close()
    print("Your password has been saved in the 'Passwords' text file on your desktop")
def confirmation_check():
    print("\n")
    confirmation = input("You have chosen to start generating a new password. Are you sure you would like to continue this function?")
    confirmation = confirmation.strip().lower()
    if confirmation == "yes":
        print("Starting password generation now...")
        generation()
        options()
    elif confirmation == "no":
        print("Returning you to the main menu now")
        options()
    else:
        print("Please answer with yes or no")
        confirmation_check()
def options():
    print("\n")
    print("You have three options. Would you like to 1:Generate a new password or 2:Look at your current password list or 3:Close this program")
    startup = input("Pick 1, 2, or 3")
    startup = startup.strip().lower()
    if startup == "1":
       confirmation_check()
    elif startup == "2":
        file = open("C:/Users/gabolinscya/Desktop/Passwords.txt", "r")
        lines = file.readlines()
        for line in lines:
            print(line)
        print("\n")
        print("THIS IS THE END OF THE TEXT FILE")
        file.close()
        options()
    elif startup == "3":
        print("\n")
        print("Thank you for using this password generator!")
    else:
        options()
print("Welcome to your very own password generator!")
options()
