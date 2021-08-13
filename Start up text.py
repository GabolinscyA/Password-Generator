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

#This function is where the password generates using randomizors.
def generation(password_list):
    #This line of code makes sure to clear the list so that further passwords generated on the same programme run time
    #aren't layered onto of the previous password
    password_list = []
    #The 'for i in range' uses a randomly generated number between 3 and 8 to figure out how many times to repeat the
    #letter (uppercase or lowercase), number between 0 and 9, and symbol randomized pattern. After each variable of the pattern
    #is generated, it is then placed into the password list.
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
    #Turns the characters in the password list at the end of generation into a string variable for visual and copy & pasting purposes
    str1 = ''.join(str(e) for e in password_list)
    save_password_check(str1)

#This function asks the user if they want to save the newly generated password.
def save_password_check(str1):
    print("\n")
    save_password = input("Your new password is : {} : Would you like to save this password?".format(str1))
    save_password = save_password.strip().lower()
    if save_password == "yes":
        password_saving(str1)
    elif save_password == "no":
        ignore_password_confirmation(str1)
    else:
        print("Please answer 'yes' or 'no'")
        save_password_check(str1)

#This fucnction first asks the user what the password is to be used for so that when saved in the dedicated text document
#that the password is saved to a type of word. Meaning that the user won't forget which password is for what. The function
#Then saves the password into the text document and returns the user to the main menu.
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

#This function asks the user if they are sure that they want to not save the newly generated password.
#The purpose of this function is to absolutely make sure that the user mean't to input 'no' from the previous function
def ignore_password_confirmation(str1):
    print("\n")
    ignore_confirm = input("Are you sure you wouldn't like to save the password : {} :".format(str1))
    ignore_confirm = ignore_confirm.strip().lower()
    if ignore_confirm == "yes":
        print("Returning you to the main menu now")
    elif ignore_confirm == "no":
        password_saving(str1)
    else:
        print("Please answer 'yes' or 'no'")
        ignore_password_confirmation(str1)

#This function asks the user if they are sure that they want to start generating a password
def generator_start_up_confirmation(password_list):
    print("\n")
    confirmation = input("You have chosen to start generating a new password. Are you sure you would like to continue this function?")
    confirmation = confirmation.strip().lower()
    if confirmation == "yes":
        print("Starting password generation now...")
        generation(password_list)
        main_menu(password_list)
    elif confirmation == "no":
        print("Returning you to the main menu now")
        main_menu(password_list)
    else:
        print("Please answer with 'yes' or 'no'")
        generator_start_up_confirmation(password_list)

#This is the main menu of the entire program. From this function you can access any part of the code through the 3 button input system that is in place.
def main_menu(password_list):
    print("\n")
    #Main menu text that is always displayed with the input so the user knows the acceptable inputs
    print("You have three options. Would you like to 1:Generate a new password or 2:Look at your current password list or 3:Close this program")
    startup = input("Pick 1, 2, or 3")
    startup = startup.strip().lower()
    if startup == "1":
        #Before they generate the password, the programme asks the user if they really do want to start generating a password
        generator_start_up_confirmation(password_list)
    elif startup == "2":
        #This option opens the text file dedicated to storing the past saved passwords generated by this programme and prints the contents for the user to view
        file = open("C:/Users/gabolinscya/Desktop/Passwords.txt", "r")
        lines = file.readlines()
        for line in lines:
            print(line)
        print("\n")
        print("THIS IS THE END OF THE TEXT FILE")
        print("If you wish to delete a saved password. You must do so by deleting it directly from the text document on your desktop.")
        file.close()
        main_menu(password_list)
    elif startup == "3":
        print("\n")
        print("Thank you for using this password generator!")
    else:
        #Repeats the function if the input is anything other than 1, 2, or 3. Which proofs the programme from any type of unwanted inputs
        main_menu(password_list)

#Simply a print statement and a function call to start up the programme
print("Welcome to your very own password generator!")
main_menu(password_list)
