import collections


def yes_no_prompt(question, default=None):
    if default.lower() == 'yes':
        prompt_end = '[Y/n]'
    elif default.lower() == 'no':
        prompt_end = '[y/N]'
    elif default is None:
        prompt_end = '[y/n]'
    else:
        raise ValueError("invalid default answer: '%s'" % default)
    user_input = input(question + f' {prompt_end} ').lower()
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is not None and user_input == '':
        return valid[default]
    elif user_input in valid:
        return valid[user_input]
    else:
        return yes_no_prompt(question, default)


def menu(menu_dict: dict):
    o_menu = collections.OrderedDict(sorted(menu_dict.items()))
    for key, text in o_menu.items():
        print("(" + str(key) + ")" + " " + text)

    while True:
        c = input()

        if c in menu_dict.keys():
            return c
        else:
            print("Invalid input.")


def value_question(question, type="str", default=None):
    default_prompt = ""
    if default is not None:
        default_prompt = f" [{default}] "
    while True:
        print(question + default_prompt, end='')
        choice = input()

        if choice != "":
            if type == "int" and not choice.isdigit():
                continue
            return choice
        elif default is not None:
            return default
