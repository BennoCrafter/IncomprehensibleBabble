import random
from tqdm import tqdm

# variables

# filenames

filename_refactored_text = "OutputTxtFiles/RefeactoredText.txt"
filename_incomprehensible_text = 'OutputTxtFiles/IncomprehensibleBabble.txt'

validcharacters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                   "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

list_with_words = open('TxtFiles/words.txt').read().split("\n")
extended = True
text = " "
numberofwords = 0

auto = False
autoclearfiles = True

# personal configs
loop = 0
write_incomprehensible_into_txt = True
auto_text = True
incomprehensibletextauto = ""
write_text_into_txt = True
incomprehensibletext = None

# langauge setup

lang_codes = ["ger", "eng"]
input_language = lang_codes[0]

# create files if it doesn't exist

createfile1 = open(filename_refactored_text, 'a+')
createfile2 = open(filename_incomprehensible_text, 'a+')

# setup lanuage

if input_language == "ger":
    language = open('TxtFiles/language-input-ger.txt').read().split("\n")
if input_language == "eng":
    language = open('TxtFiles/language-input-eng.txt').read().split("\n")


def GenerateIncomprehensibleText():
    # generate incomprehensible babble
    global incomprehensibletextauto, loop
    if auto:
        loop = 10000
    for _ in tqdm(range(loop)):
        incomprehensibletextauto = incomprehensibletextauto + (random.choice(validcharacters))

    # write into write_into_file
    if write_incomprehensible_into_txt or auto:
        write_into_file = open(filename_incomprehensible_text, "w")
        write_into_file.write(incomprehensibletextauto)
        write_into_file.close()


def CheckingIncomprehnsible():
    global numberofwords, text, incomprehensibletext

    # check if words exists in incomprehensible babble and print it
    if auto_text:
        incomprehensibletext = incomprehensibletextauto

    for x in tqdm(list_with_words):
        if x in incomprehensibletext:
            numberofwords += 1
            if extended:
                text = text + x + " ;; " + str(numberofwords) + " || "
            else:
                text = text + x + " || "


# some inputs and set some variables

answer = input(language[0])
if answer.lower() == "j" or answer.lower() == "y":
    f = open(filename_refactored_text, 'r+')
    f.truncate(0)  # need '0' when using r+
    f = open(filename_incomprehensible_text, 'r+')
    f.truncate(0)  # need '0' when using r+
answer = input(language[1])

# autotext
if answer == "j" or answer.lower() == "y":
    auto_text = True
    answer = input(language[2])
    if answer.lower() == "j" or answer.lower() == "y":
        auto = True
        print(language[3])
    else:
        auto = False
        answer = input(language[4])
        loop = int(answer) + 1
        answer = input(language[5])
        if answer.lower() == "j" or answer.lower() == "y":
            write_text_into_txt = True
            print(language[3])
        else:
            write_text_into_txt = False

else:
    auto_text = False
    answer = input(language[6])
    # read incomprehensible text from txt file
    if answer == "0":
        answer = input(language[7])
        filename = answer
        incomprehensibletext = open(filename).read()
    # read incomprehensible text from input
    if answer == "1":
        answer = input(language[8])
        incomprehensibletext = answer
    answer = input(language[5])
    if answer.lower() == "j" or answer.lower() == "y":
        write_text_into_txt = True
        print(language[3])
    else:
        write_text_into_txt = False


GenerateIncomprehensibleText()
CheckingIncomprehnsible()

print(language[9] + "\n" + str(numberofwords) + "\n" + str(
    len(incomprehensibletext)) + language[10] + "\n\n\n\n" + text)

if write_text_into_txt or auto:
    # write into file

    file = open(filename_refactored_text, "w")
    file.write(text)
    file.close()
