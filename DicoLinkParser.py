from html.parser import HTMLParser
import urllib.request as urllib2
from termcolor import colored

lstSources = []
lstDefinitions = {}


class DicoLinkParser(HTMLParser):
    sectionTag = 'div'
    sourceTag = 'h3'
    definitionTag = 'li'

    insideSection = False
    insideSource = False
    insideDefinition = False

    currentDefinitions = []

    num_source = 0
    menu_color_1 = 'red'
    menu_color_2 = 'green'

    # def __init__(self):
    #     print('body of the constructor')
    #     # self.lstSources.clear()
    #     # self.lstDefinitions.clear()

    @staticmethod
    def attrs_match(attrs, attr_name, attr_value):
        for names, values in attrs:
            if names == attr_name and values == attr_value:
                return True
        return False

    def error(self, message):
        print('Error : ', message)

    def handle_starttag(self, tag, attrs):
        if tag == self.sectionTag and self.attrs_match(attrs, 'class', 'guts active'):
            self.insideSection = True

        if self.insideSection:
            if tag == self.sourceTag and self.attrs_match(attrs, 'class', 'source'):
                self.insideSource = True
                # self.lstSources = []

        if self.insideSection:
            if tag == self.definitionTag:  # and self.attrs_match(attrs, 'class', 'source'):
                self.insideDefinition = True
                # self.lstDefinitions = {}

    def handle_endtag(self, tag):
        if tag == self.sectionTag:
            self.insideSection = False
        if tag == self.sourceTag:
            self.insideSource = False
            self.num_source = self.num_source + 1
            self.currentDefinitions = []
        if tag == self.definitionTag:
            self.insideDefinition = False

    def handle_data(self, data):
        if self.insideSection:
            if self.insideSource:
                lstSources.append(data)
                # print('source : ', data)

        if self.insideDefinition:
            self.currentDefinitions.append(data)
            lstDefinitions[self.num_source] = self.currentDefinitions
            # print('définition : ', data)

    def print_result(self):
        for i in range(0, len(lstSources)):
            print(colored(lstSources[i], self.menu_color_1))
            for definition in lstDefinitions.get(i + 1):
                print('\t', colored(definition, self.menu_color_2))
                # print('\t', definition)

        # print(self.lstSources)
        # print(self.lstDefinitions)

    def word_exist(self):
        return len(lstDefinitions) > 0


def _init():
    lstSources.clear()
    lstDefinitions.clear()


def dictionary_search(word):
    # _init()
    # parser = DicoLinkParser()
    # html_page = urllib2.urlopen('https://www.dicolink.com/mots/' + word)
    # html_content = str(html_page.read().decode('utf-8'))
    # # print(html_content)
    # parser.feed(html_content)

    parser = create_parser(word)
    if parser.word_exist():
        print('******************************************')
        print(word.upper(), ' - Definition(s) : ')
        print('******************************************')
        parser.print_result()
        print('******************************************')
    else:
        print(word, ' not found!')


def create_parser(word):
    _init()
    _parser = DicoLinkParser()
    html_page = urllib2.urlopen('https://www.dicolink.com/mots/' + word)
    html_content = str(html_page.read().decode('utf-8'))
    _parser.feed(html_content)
    return _parser


def word_exists(word):
    if word is None:
        return False

    parser = create_parser(word)
    return parser.word_exist()

    # try:
    #     parser = DicoLinkParser()
    #     html_page = urllib2.urlopen('https://www.dicolink.com/mots/' + word)
    #     html_content = str(html_page.read().decode('utf-8'))
    #     parser.feed(html_content)
    #
    #     return parser.word_exist()
    # except ValueError:
    #     print('error: ' + ValueError)
    #     return False


async def dictionary_exists_async(word):
    parser = DicoLinkParser()
    html_page = urllib2.urlopen('https://www.dicolink.com/mots/' + word)
    html_content = str(html_page.read().decode('utf-8'))
    parser.feed(html_content)

    # print('\t', word, ' ==>', parser.is_found())
    return parser.word_exist()


if __name__ == '__main__':
    dictionary_search('xi')
