def new_password():
    passw0rds = input("Please enter a random number")
    website = input("What would you like this password to be used for?")
    file = open("C:/Users/gabolinscya/Desktop/Passwords.txt", "a")
    file.write("\n")
    file.write(website)
    file.write(":")
    file.write("\n")
    file.write(passw0rds)
    file.close()
    print("Your password has been saved in the 'Passwords' text file on your desktop.")
    password_ask()

def password_ask():
    password_gen = input("Would you like to generate a new password? Please answer 'yes'or 'no'")
    password_gen = password_gen.strip().lower()
    if password_gen == "yes":
        new_password()
    elif password_gen == "no":
        print("Thank you for using my password generator!")
    else:
        print("Please answer yes or no")
        password_ask()

password_ask()
