from html.parser import HTMLParser
import urllib.request as urllib2


class DicoLinkParser(HTMLParser):
    sectionTag = 'div'
    sourceTag = 'h3'
    definitionTag = 'li'

    insideSection = False
    insideSource = False
    insideDefinition = False

    lstSources = []
    lstDefinitions = {}
    currentDefinitions = []
    num_source = 0

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
                self.lstSources = []

        if self.insideSection:
            if tag == self.definitionTag:  # and self.attrs_match(attrs, 'class', 'source'):
                self.insideDefinition = True
                self.lstDefinitions = {}

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
                self.lstSources.append(data)
                # print('source : ', data)

        if self.insideDefinition:
            self.currentDefinitions.append(data)
            self.lstDefinitions[self.num_source] = self.currentDefinitions
            # print('définition : ', data)

    def print_result(self):
        for i in range(0, len(self.lstSources)):
            print(self.lstSources[i])
            for definition in self.lstDefinitions.get(i + 1):
                print('\t', definition)

    def word_exist(self):
        return len(self.lstDefinitions) > 0


def dictionary_search(word):
    parser = DicoLinkParser()
    html_page = urllib2.urlopen('https://www.dicolink.com/mots/' + word)
    html_content = str(html_page.read().decode('utf-8'))
    # print(html_content)
    parser.feed(html_content)
    if parser.is_found():
        print(word.upper())
        parser.print_result()
    else:
        print(word, ' not found!')


def word_exists(word):
    if word is None:
        return False

    try:
        parser = DicoLinkParser()
        html_page = urllib2.urlopen('https://www.dicolink.com/mots/' + word)
        html_content = str(html_page.read().decode('utf-8'))
        parser.feed(html_content)

        return parser.word_exist()
    except ValueError:
        print('error: '+ValueError)
        return False



async def dictionary_exists_async(word):
    parser = DicoLinkParser()
    html_page = urllib2.urlopen('https://www.dicolink.com/mots/' + word)
    html_content = str(html_page.read().decode('utf-8'))
    parser.feed(html_content)

    # print('\t', word, ' ==>', parser.is_found())
    return parser.is_found()


if __name__ == '__main__':
    dictionary_search('wu')
