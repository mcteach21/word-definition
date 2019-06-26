import sys

from termcolor import colored

from scrabble import scrabble


def main():
    print("**************************************")
    print("Python : Samples & Tests")
    print("**************************************")


if __name__ == '__main__':  # si script courant
    main()

nb = -1
menu_color = 'yellow'


def menu():
    print(colored("************** Menu *******************", menu_color))
    print(colored("1- Words (scrabble search)", menu_color))
    print(colored("2- Word Definition", menu_color))
    print(colored("0- Quit!", menu_color))
    print(colored("***************************************", menu_color))

    global nb

    try:
        nb = int(input("your choice (1-3) : "))
        func = switch_function(nb)
        if not callable(func):
            error('unknown function')
            menu()
        else:
            print('function (exec.) : ', func.__name__)
            func()
    except:
        error("invalide number!")
        menu()


def error(mess):
    print(colored(mess + " try again.", 'red'))


# def all():
#     menu()
def bye():
    print(colored("***************************************", menu_color))
    print("Bye!!")
    print(colored("***************************************", menu_color))


def word_definition():
    print("definition..")


def switch_function(arg):
    switcher = {
        0: bye,
        1: scrabble,
        2: word_definition,
        3: lambda: print("not implemented yet!!")
    }
    _func = switcher.get(arg, 'unknown function!')
    return _func


while nb != 0:
    menu()
