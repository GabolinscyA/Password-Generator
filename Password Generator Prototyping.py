#Declaring the 'random' and the 'secrets' operation
import random
import secrets
#creating lists so that the random operation may pick a character within the list
az_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol_list = ['`', '~', '!', '@', '$', '#', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '[', '}', ']', '|', '<', ',', '>', '.', '?', '/', ':', ';']
password_list = []
#Declaring the variable 'pattern_repeat' so that the 'for i in range' function works
pattern_repeat = random.randint(3,8)

#For function that repeats a random number of times between 3 times and 8 times (pattern_repeat).
for i in range(pattern_repeat):
    #Randomly selects a varaible/letter from the list that contains every letter in the alphebet (az_list)
    alphebet_pick = secrets.choice(az_list)
    #Generates a random boolean variable aka True or False
    capitalize_letter = random.getrandbits(1)
    #If statement that if the random boolean is True, then cappitalizes the selected alphebet letter
    if capitalize_letter == True:
        alphebet_pick = alphebet_pick.capitalize()
    #The elif statement that if the random boolean is False, keep the letter lower case
    elif capitalize_letter == False:
        alphebet_pick = alphebet_pick
    #After picking out the letter and giving it a 50/50 chance of being capital, it is then put into the password list
    password_list.append(alphebet_pick)
    #Randomly picks a number from 0 to 9 and puts it in the password list
    number_pick = random.randint(0,9)
    password_list.append(number_pick)
    #Randomly selects a varaible/symbol from the list that contains almost every symbol on the keyboard (symbol_list)
    symbol_pick = secrets.choice(symbol_list)
    #Puts the randomly selected symbol into the password list
    password_list.append(symbol_pick)
#After the 'for i in range' function finishes it job, the entire password list is print without brackets and spaces
#This allows the password to be copy and pasted for inserting it into websites
print(*password_list, sep="")
