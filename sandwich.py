import re
from constants import *

def print_menu():
    """
    if customer ask, print out the menu
    """
    print(MENU)


def ignore_unvalid_words(sentence):
    """
    filter user request by eliminating invalid words
    :param sentence: user request
    :return: sentence after filtering
    """
    for word in UNVALID_WORDS:
        sentence = sentence.replace(word, "")
    return sentence


def choose_sandwich(need):
    need = need.lower()
    need = ignore_unvalid_words(need)

    sandwich = ""
    desc = ""
    while not sandwich:
        for key in SANDWICHES.keys():
            if key.lower() in need:
                sandwich = SANDWICHES[key][0]
                desc = SANDWICHES[key][1]
                return sandwich, desc
        if not sandwich:
            need = input("Sandwich not found, please reenter:\n" + "\n".join(SANDWICH_LIST) + "\n")
            need = need.lower()
            need = ignore_unvalid_words(need)


def choose_bread(need, sandwich):
    need = need.lower()
    need = ignore_unvalid_words(need)

    bread = ""
    for key in BREADS.keys():
        if key.lower() in need:
            bread = BREADS[key]
            return bread

    while not bread:
        prompt = "Either bread not found or not specified. " \
                 f'This sandwich usually comes with {SANDWICHES[sandwich][2]} bread. ' \
                 f'Press return to accept this choice of bread, or choose one of the other alternatives: \n'
        sublist = list(BREAD_LIST)
        sublist.remove(SANDWICHES[sandwich][2])
        cnt = 1
        for option in sublist:
            prompt += str(cnt) + f". {option} bread.\n"
            cnt += 1
        number = input(prompt)
        # press enter
        if not number:
            bread = SANDWICHES[sandwich][2]
        elif int(number) - 1  < len(sublist):
            bread = sublist[int(number) - 1]

    return bread


def choose_spread(need, sandwich):
    need = need.lower()
    need = ignore_unvalid_words(need)

    spread = ""
    for key in SPREADS.keys():
        if key.lower() in need:
            spread = SPREADS[key]
            return spread

    while not spread:
        prompt = "Either spread not found or not specified. " \
                 f'This sandwich usually comes with {SANDWICHES[sandwich][3]} spread. ' \
                 f'Press return to accept this choice of spread, or choose one of the other alternatives: \n'
        sublist = list(SPREAD_LIST)
        sublist.remove(SANDWICHES[sandwich][3])
        cnt = 1
        for option in sublist:
            prompt += str(cnt) + f". {option} spread.\n"
            cnt += 1
        number = input(prompt)
        # press enter
        if not number:
            spread = SANDWICHES[sandwich][3]
        elif int(number) - 1 < len(sublist):
            spread = sublist[int(number) - 1]

    return spread


def parse_options(need):
    need = need.lower()
    need = ignore_unvalid_words(need)

    inches = 6
    if (re.search("12.*?inch", need) or re.search("twelve.*?inch", need)
            or re.search("1.*?foot", need) or re.search("one.*?foot", need)):
        inches = 12

    toasted = False
    if ("toast" in need) and (re.search("(no|non|not|do.*?t|without)\s+toast", need) is None):
        toasted = True
    # delete substring "don't/do not toast" in order not to confuse "exceptions"
    need = re.sub("(no|non|not|do.*?t|without)\s+toast(ed)?", "", need)

    double_spread = False
    if re.search("(double|2x|twice|2)\s+spread", need):
        double_spread = True

    return inches, toasted, double_spread, need


def parse_exce(need, desc):
    need = need.lower()
    need = ignore_unvalid_words(need)

    exce = ""
    invalid_exce = IRRE_EXCE
    for item in EXCEs:
        # search for valid exceptions
        if re.search(f"(no|hold|do.*?t\s+(want|need)|leave|remove|without).*?"
                     f"{item}\w*?(\s*$|\s*(with|too|also|and|,|\.))", need):
            # replace from right to left
            need = need[::-1]
            item = item[::-1]
            need = re.sub(f"(^\s*|(htiw|oot|osla|dna|,|\.)\s*)\w*?{item}.*?"
                          f"(on|dloh|(tnaw|deen)\s+t.*?od|evael|evomer|tuohtiw)", "", need)
            need = need[::-1]
            item = item[::-1]
            # need = re.sub(f"(no|hold|do.*?t\s+(want|need)|leave|remove|without).*?"
            #               f"{item}\w*?(\s*$|\s*(with|too|also|and|,|\.))", "", need)
            if item in desc.lower():
                exce += "no " + item + "\n"
            else:
                # irrelevant exception
                invalid_exce += "no " + item + "\n"

    # extra exception list
    irre = re.findall("(no|hold|do.*?t\s+(want|need)|leave|remove|without).*?"
                      "(\w+?)(\s*$|\s*(with|too|also|and|,|\.))", need)
    if irre:
        for item in irre:
            invalid_exce += "no " + item[2] + "\n"
    if invalid_exce == IRRE_EXCE:
        invalid_exce = ""
    return exce, invalid_exce


def parse_need(need):
    """
    identify all needs from the user
    :param need: user input
    :return: order detail
    """
    sandwich, desc = choose_sandwich(need)
    bread = choose_bread(need, sandwich)
    spread = choose_spread(need, sandwich)
    # options
    inches, toasted, double_spread, need = parse_options(need)
    # exceptions
    exce, invalid_exce = parse_exce(need, desc)

    return sandwich, desc, bread, spread, inches, toasted, double_spread, exce, invalid_exce


def print_order(sandwich, desc, bread, spread, inches, toasted, double_spread, exce, invalid_exce):
    print("Order detail:\n")
    print(f"1. Sandwich: {sandwich}\n")
    print(f"2. Usual ingredients: {desc}\n")
    print(f"3. Bread-type: {bread}\n")
    print(f"4. Spreads: {spread}\n")
    options = str(inches) + " inches," + ("" if toasted else "non") + " toasted" + \
              (", double spread" if double_spread else "")
    print(f"5. Options: {options}\n")
    print(f"6. Exceptions: {exce}\n")
    print(f"Irrelevant exceptions: {invalid_exce}")
    print()


def confrim(sandwich, desc, bread, spread, inches, toasted, double_spread, exce, invalid_exce):
    """
    after analyzing user input, print out the order detail and provide chances for user to modify
    his/her original request.
    """
    print_order(sandwich, desc, bread, spread, inches, toasted, double_spread, exce, invalid_exce)

    command = "placeholder"
    while command:
        command = input("Hi, is this what you are ordering? Press enter to confirm.\n"
          "Otherwise, enter one of 1,3,4,5,6 and reenter.\n\n")
        if not command:
            break
        if command == '1':
            need = input("Please choose a new sandwich:\n" + "\n".join(SANDWICH_LIST) + "\n")
            sandwich, desc = choose_sandwich(need)
            # update exceptions when sandwich changes
            old_exce = ",".join((exce + invalid_exce).split("\n"))
            exce, invalid_exce = parse_exce(old_exce, desc)
        elif command == '3':
            need = input("Please choose a new bread type:\n" + "\n".join(BREAD_LIST) + "\n")
            bread = choose_bread(need, sandwich)
        elif command == '4':
            need = input("Please choose a new spread type:\n" + "\n".join(SPREAD_LIST) + "\n")
            spread = choose_spread(need, sandwich)
        elif command == '5':
            need = input("Please input new customized options, including:\n"
                         "6 inches/1-foot(12 inches), toasted or not, double spreads.\n")
            inches, toasted, double_spread, need = parse_options(need)
        elif command == '6':
            need = input("Please input new exceptions, including:\n"
                         "no onions, hold the mayo, no tomatoes.\n")
            exce, invalid_exce = parse_exce(need, desc)
        print_order(sandwich, desc, bread, spread, inches, toasted, double_spread, exce, invalid_exce)


if __name__== "__main__":
    need = input('hello, what do you want to eat today?\n')
    need = need.lower()
    need = ignore_unvalid_words(need)

    is_print_menu = False
    for word in MENU_WORD:
        if word in need:
            is_print_menu = True
    if is_print_menu:
        print_menu()

    if is_print_menu:
        need = input('Hi, here is the menu, what do you want to eat?\n')
        need = need.lower()
        need = ignore_unvalid_words(need)

    sandwich, desc, bread, spread, inches, toasted, double_spread, exce, invalid_exce = parse_need(need)

    confrim(sandwich, desc, bread, spread, inches, toasted, double_spread, exce, invalid_exce)

    print("Thank you for ordering! Please stand by, your sandwich is coming soon!")