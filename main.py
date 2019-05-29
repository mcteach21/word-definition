from termcolor import colored

from scrabble import scrabble


def main():
    print("**************************************")
    print("Python : Samples & Tests")
    print("**************************************")


if __name__ == '__main__':  # si script courant
    main()


nb = -1
menu_color = 'blue'


def menu():
    print(colored("************** Menu *******************", menu_color))
    print(colored("1- Words (scrabble search)", menu_color))
    print(colored("2- Words Definitions", menu_color))
    print(colored("0- Quit!", menu_color))
    print(colored("***************************************", menu_color))

    global nb

    try:
        nb = int(input("choice (1-3) ==> "))
        switch_number(nb)
    except:
        error("invalide number!")
        menu()


def error(mess):
    print(colored("(x) "+mess+"! try again.", 'red'))


def all():
    menu()


def switch_number(arg):
    # dictionary
    switcher = {
        0: lambda: print("Bye!!"),
        1: scrabble(),
        # 2: init2,
        3: all,
    }
    func = switcher.get(arg, error('unknown func!'))
    print("(!) func (exec0.) ==> " + func.__name__)
    return func()


while nb != 0:
    menu()