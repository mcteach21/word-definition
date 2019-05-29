import aiohttp
import bs4


class DicoLink:
    _url_base = 'https://www.dicolink.com/mots/'
    _HEADERS = {'User-Agent': 'Mozilla/5.0'}

    async def get_html(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self._HEADERS) as resp:
                return await resp.text()

    async def word_definitions(self, word):
        definitions = await self.get_data(word)
        print('*******************************************************************')
        print(word.upper(), 'not found!' if len(definitions) == 0 else 'correct! ')
        if len(definitions) > 0: print(definitions)
        print('*******************************************************************')

    async def word_exist(self, word):
        definitions = await self.get_data(word)
        return len(definitions) > 0

    async def get_data(self, word):
        response = await self.get_html(self._url_base + word)
        soup = bs4.BeautifulSoup(response, "html.parser")

        # sources = soup.find_all('h3', class_='source')  # .text.strip().replace('\u2009', '')
        # print('*******************************************************************')
        # for source in sources:
        #     print(source.text.strip().replace('\u2009', ''))
        # print('*******************************************************************')
        definitions = soup.find_all('abbr', class_='')  # .text.strip().replace('\u2009', '')
        data = []
        for definition in definitions:
            data.append(definition.parent.text.strip().replace('\u2009', ''))

        return data
