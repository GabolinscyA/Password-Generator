def generation():
    print("Please enter a random number")
    password_numb = input()
    keep_password_checK()

def keep_password_checK():
    save_password = input("Your new password is {}. Would you like to save this password?".format(password_numb))
    save_password = save_password.strip().lower()
    if save_password == "yes":
        password_saving()
    elif save_password == "no":
        save_confirmation()
    else:
        print("Please answer 'yes' or 'no'")
        keep_password_checK()

def password_saving():
    website = input("What would you like this password to be used for?")
    file = open("C:/Users/gabolinscya/Desktop/Passwords.txt", "a")
    file.write("\n")
    file.write(website)
    file.write(":")
    file.write("\n")
    file.write(password_numb)
    file.close()
    print("Your password has been saved")
    print("If you want to view your new password, type '2' in the main menu")
    print("Alternatively, you can view your password directly in the 'Passwords' text file on your desktop")

def save_confirmation():
    save_confirm = input("Are you sure you wouldn't like to save the password:{}?".format(password_numb))
    save_confirm = save_confirm.strip().lower()
    if save_confirm == "yes":
        print("Directing you back to the menu...")
    elif save_confirm == "no":
        password_saving()
    else:
        print("Please answer 'yes' or 'no'")
        save_confirmation()

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
        print("Please answer with 'yes' or 'no'")
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
