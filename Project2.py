import random

"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jan Kaminský    
email: honza.kaminsky@gmail.com
discord: jank.1818
"""
def pozdrav():
    separator = 47 * "-"
    print("Hi, there!", 
        separator, 
        "I've generated a random 4 digit number for you.", 
        "Let's play a bulls and cows game.",
        separator,
        "Enter a number:",
        separator, 
        sep="\n")

def random_number():
    "Create random 4 digit number. Every number in will be unique"
    unique_digits = random.sample(range(1,10), 4)
    random_number = ""
    for cislo in unique_digits:
        random_number += str(cislo) 
    return int(random_number)
       
def guess_number():
    """User will choose 4 digit number which cannot start with 0 and every digit has to be unique."""
    correct = True
    while correct == True:
        guessed_number = input(">>> ")
        my_set = set()
        if (guessed_number.isdigit() == True) and len(guessed_number) == 4 and int(guessed_number) in range(1000, 9999):
            for digit in str(guessed_number):
                my_set.add(digit)
            if len(my_set) != 4:
                print("Some digit is there more than once.")
            else:
                correct = False
        else:
            print("Wrong number.")
    return int(guessed_number)

def make_list(number):
    """This function make list from number.
    Example: input is 2017 -> [2, 0, 1, 7] """
    number_list = []
    for f in str(number):
        number_list.append(int(f))
    return number_list

def bandc(randnum, guessnum):
    """Return dictionary with number of bulls and cows. If number is on exactly same index in both,
    than is it bull. If it is there, but on different index, than it is cow.
    Example: Random number is 2017, Guessed number is 6147
        Result will {"bulls" : 1, "cows" : 1}"""
    bullsandcows = {"bulls" : 0, "cows" : 0}
    for index in range(4):
        if guessnum[index] == randnum[index]:
            bullsandcows["bulls"] += 1
        elif guessnum[index] in randnum:
            bullsandcows["cows"] += 1
    return bullsandcows

def bullsandcows():
    """This will run whole program"""
    pozdrav()
    randnum = make_list(random_number())
    answer = True
    guesses = 0
    while answer == True:
        guesses += 1
        separator = 47 * "-"
        guessnum = make_list(guess_number())
        dictionary = bandc(randnum, guessnum)
        if dictionary["bulls"] == 1 and dictionary["cows"] == 1:
            print(dictionary["bulls"], "bull", dictionary["cows"], "cow")
        elif dictionary["bulls"] == 1 and dictionary["cows"] != 1:
            print(dictionary["bulls"], "bull", dictionary["cows"], "cows")
        elif dictionary["bulls"] != 1 and dictionary["cows"] == 1:
            print(dictionary["bulls"], "bulls", dictionary["cows"], "cow")
        elif dictionary["bulls"] == 4:
            answer = False
            print("Correct, you've guessed the right number")
            print(f"in {guesses} guesses!")
        else:
            print(dictionary["bulls"], "bulls", dictionary["cows"], "cows")
        print(separator)
              
bullsandcows()

       



