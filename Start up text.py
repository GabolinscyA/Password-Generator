# Declaring the 'random' and the 'secrets' operation
import random
import secrets
# Creating lists so that the random operation may pick a character within the list
az_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
symbol_list = ['`', '~', '!', '@', '$', '#', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '[', '}', ']', '|',
               '<', ',', '>', '.', '?', '/', ':', ';']
password_list = []
# Declaring the variable 'pattern_repeat' so that the 'for i in range' function works
pattern_repeat = random.randint(3, 8)

def generation(password_list):
    for i in range(pattern_repeat):
        alphebet_pick = secrets.choice(az_list)
        capitalize_letter = random.getrandbits(1)
        if capitalize_letter == True:
            alphebet_pick = alphebet_pick.capitalize()
        elif capitalize_letter == False:
            alphebet_pick = alphebet_pick
        password_list.append(alphebet_pick)
        number_pick = random.randint(0, 9)
        password_list.append(number_pick)
        symbol_pick = secrets.choice(symbol_list)
        password_list.append(symbol_pick)
    str1 = ''.join(str(e) for e in password_list)
    print(str1)
    keep_password_checK(str1)

def keep_password_checK(str1):
    print("\n")
    save_password = input("Your new password is {}. Would you like to save this password?".format(str1))
    save_password = save_password.strip().lower()
    if save_password == "yes":
        password_saving(str1)
    elif save_password == "no":
        save_confirmation(str1)
    else:
        print("Please answer 'yes' or 'no'")
        keep_password_checK(str1)


def password_saving(str1):
    website = input("What would you like this password to be used for?")
    file = open("C:/Users/gabolinscya/Desktop/Passwords.txt", "a")
    file.write("\n")
    file.write(website)
    file.write(":")
    file.write("\n")
    file.write(str1)
    file.close()
    print("\n")
    print("Your password has been saved")
    print("\n")
    print("If you want to view your new password, type '2' in the main menu")
    print("Alternatively, you can view your password directly in the 'Passwords' text file on your desktop")


def save_confirmation(str1):
    save_confirm = input("Are you sure you wouldn't like to save the password:{}:?".format(str1))
    save_confirm = save_confirm.strip().lower()
    if save_confirm == "yes":
        print("Directing you back to the menu...")
    elif save_confirm == "no":
        password_saving(str1)
    else:
        print("Please answer 'yes' or 'no'")
        save_confirmation(str1)


def confirmation_check(password_list):
    print("\n")
    confirmation = input(
        "You have chosen to start generating a new password. Are you sure you would like to continue this function?")
    confirmation = confirmation.strip().lower()
    if confirmation == "yes":
        print("Starting password generation now...")
        generation(password_list)
        options(password_list)
    elif confirmation == "no":
        print("Returning you to the main menu now")
        options(password_list)
    else:
        print("Please answer with 'yes' or 'no'")
        confirmation_check(password_list)


def options(password_list):
    print("\n")
    print(
        "You have three options. Would you like to 1:Generate a new password or 2:Look at your current password list or 3:Close this program")
    startup = input("Pick 1, 2, or 3")
    startup = startup.strip().lower()
    if startup == "1":
        confirmation_check(password_list)
    elif startup == "2":
        file = open("C:/Users/gabolinscya/Desktop/Passwords.txt", "r")
        lines = file.readlines()
        for line in lines:
            print(line)
        print("\n")
        print("THIS IS THE END OF THE TEXT FILE")
        file.close()
        options(password_list)
    elif startup == "3":
        print("\n")
        print("Thank you for using this password generator!")
    else:
        options(password_list)


print("Welcome to your very own password generator!")
options(password_list)
