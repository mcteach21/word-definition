from termcolor import colored
from DicoLinkParser import dictionary_search

menu_color = 'yellow'


def word_definition():
    word = input("mot recherché : ")
    dictionary_search(word)


def main():
    print(colored('**************************************', menu_color))
    print(colored('Python : Online Dico.', menu_color))
    print(colored('**************************************', menu_color))
    word_definition()


if __name__ == '__main__':
    main()
