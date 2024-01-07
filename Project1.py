"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Kaminský    
email: honza.kaminsky@gmail.com
discord: jank.1818
"""
import sys
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#variables
names = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123", "pass123"]
line = 40*"-"
num_in_list = len(TEXTS)

#condition for login
name = input("username:")
if name in names:
    index = names.index(name)
    password = input("password:")
    if password in passwords:
        if password == passwords[index]:
            print(line)
        else:
            print("Wrong password")
            sys.exit()           
    else:
        print("unregistered user, terminating the program..")
        sys.exit()
else:
    print("unregistered user, terminating the program..")
    sys.exit()

print("Welcome to app,", name)
print("We have", num_in_list, "texts to be analyzed.")
print(line)

#text selection condition
number = input(f"Enter a number between 1 and {num_in_list}: ")
if int(number) <= num_in_list:
    print(line)
else:
    print("Number is out of scope")
    sys.exit()

#variables for final output
words = []
for word in TEXTS[int(number)-1].split():
    clear_word = word.strip(",.:;'")
    words.append(clear_word)
    
num_of_words = (len(words))
num_capital_start = sum(1 for word in words if word[0].isupper())
num_capital_letters = sum(1 for word in words if word.isupper())
num_lowercase_letters = sum(1 for word in words if word.islower())
num_numbers = sum(1 for word in words if word.isdigit())
sum_of_numbers = sum(int(word) for word in words if word.isdigit())

#output
print("There are", num_of_words,"words in the selected text.")
print("There are", num_capital_start, "titlecase words.")
print("There are", num_capital_letters, "uppercase words.")
print("There are", num_lowercase_letters, "lowercase words.")
print("There are", num_numbers, "numeric strings.")
print("The sum of all the numbers", sum_of_numbers)
print(line)


#graphs
word_length_dict = {}
for word in words:
    length = len(word)
    if length in word_length_dict:
        word_length_dict[length] += 1
    else:
        word_length_dict[length] = 1
sorted_final_dict = dict(sorted(word_length_dict.items()))
#variables for final print
max_value = max(sorted_final_dict.values())
x = 0
print(f"LEN| {'OCCURENCES':<{max_value}} |NR.")
print(line)
#print of graphs
for _ in sorted_final_dict:
    num = list(sorted_final_dict.keys())[x]
    values = list(sorted_final_dict.values())[x]
    print(f"{num:2} | {'*' * values:<{max_value}} |{values}")
    x = x + 1

