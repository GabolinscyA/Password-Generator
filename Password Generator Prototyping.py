import random
import secrets
az_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol_list = ['`', '~', '!', '@', '$', '#', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '[', '}', ']', '|', '<', ',', '>', '.', '?', '/', ':', ';']
password_list = []

for i in range(3,9):
    alphebet_pick = secrets.choice(az_list)
    capitalize_letter = random.getrandbits(1)
    if capitalize_letter == True:
        alphebet_pick = alphebet_pick.capitalize()
    elif capitalize_letter == False:
        alphebet_pick = alphebet_pick
    password_list.append(alphebet_pick)
    number_pick = random.randint(0,9)
    password_list.append(number_pick)
    symbol_pick = secrets.choice(symbol_list)
    password_list.append(symbol_pick)
print(password_list)





#pattern_repeat = random.randint(3,8)
#print(pattern_repeat)
