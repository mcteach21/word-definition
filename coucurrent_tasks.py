import asyncio
import time
from html.parser import HTMLParser

from DicoLinkParser import DicoLinkParser
import urllib.request as urllib2


class DicoParser(HTMLParser):
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

    # def __init__(self):

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

    async def is_found(self):
        return await len(self.lstSources) > 0

    async def word_exist(self, word):
        return len(self.lstDefinitions)>0


async def _search_task(word):
    # print(f'search..{word}')
    # dico = DicoLink()
    # result = await dico.word_exist(word)

    parser = DicoParser()
    html_page = urllib2.urlopen('https://www.dicolink.com/mots/' + word)
    html_content = str(html_page.read().decode('utf-8'))
    parser.feed(html_content)

    found = await parser.word_exist(word)
    print(f'word {word} : {str(found)}')


def event_loop_concurrent_tasks():
    words = ['zulu', 'wu', 'kk', 'coucou']

    try:
        loop = asyncio.get_event_loop()

        coroutines = [loop.create_task(_search_task(word)) for word in words]
        loop.run_until_complete(asyncio.wait(coroutines))

    finally:
        loop.close()


# async def create_concurrent_tasks():
#     task1 = asyncio.create_task(_task(1))
#     task2 = asyncio.create_task(_task(2))
#
#     await task2
#     await task1


if __name__ == "__main__":
    print(f"started at {time.strftime('%X')}")
    # asyncio.run(create_concurrent_tasks())

    # event_loop_concurrent_tasks()

    print(f"finished at {time.strftime('%X')}")
