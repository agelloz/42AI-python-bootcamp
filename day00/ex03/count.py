import sys
import string

def text_analyzer(text = ""):
    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
    if (text == ""):
        sys.stdout.write('What is the text to analyse?\n>> ')
        text = input()
    if (text == ""):
        exit()
    upper = 0
    lower = 0
    punct = 0
    spaces = 0
    i = 0

    for c in text:
        if (c.isspace()):
            spaces += 1
        if (c.isupper()):
            upper += 1
        if (c.islower()):
            lower += 1
        if (c in string.punctuation):
            punct += 1
        i += 1

    print("The text contains " + str(i) + " characters:")
    print("- " + str(upper) + " upper letters")
    print("- " + str(lower) + " lower letters")
    print("- " + str(punct) + " punctuation marks")
    print("- " + str(spaces) + " spaces")
