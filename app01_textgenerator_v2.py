import random, string

vowels = "aeioyu"
consonants = "bcdfghjklmnpqrstvwxz"
letters = string.ascii_lowercase


letter_input_1 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
letter_input_2 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
letter_input_3 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")


print (letter_input_1, letter_input_2, letter_input_3)

def get_letter(letter_input):
    if letter_input == 'v':
        return random.choice(vowels)
    elif letter_input == 'c':
        return random.choice(consonants)
    elif letter_input == 'l':
        return random.choice(letters)
    else:
        print ("wrong input")
        return '0'

def generator():
    letter1 = get_letter(letter_input_1)
    letter2 = get_letter(letter_input_2)
    letter3 = get_letter(letter_input_3)

    name = letter1 + letter2 + letter3
    return name


for i in range(20):
    print (generator())