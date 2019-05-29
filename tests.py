# import asyncio
# import aiohttp
# import pprint
# import time
# import bs4
#
# _url_base = 'https://www.dicolink.com/mots/'
# _HEADERS = {'User-Agent': 'Mozilla/5.0'}
#
#
# async def get_html(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url, headers=_HEADERS) as resp:
#             return await resp.text()
#
#
# async def is_correct(word):
#     definitions = await get_data(word)
#     print('*******************************************************************')
#     print(word.upper(), 'not found!' if len(definitions) == 0 else 'correct! ')
#     if len(definitions) > 0: print(definitions)
#     print('*******************************************************************')
#
#
# async def get_data(word):
#     response = await get_html(_url_base + word)
#     soup = bs4.BeautifulSoup(response, "html.parser")
#
#     # sources = soup.find_all('h3', class_='source')  # .text.strip().replace('\u2009', '')
#     # print('*******************************************************************')
#     # for source in sources:
#     #     print(source.text.strip().replace('\u2009', ''))
#     # print('*******************************************************************')
#
#     definitions = soup.find_all('abbr', class_='')  # .text.strip().replace('\u2009', '')
#
#     data = []
#     for definition in definitions:
#         data.append(definition.parent.text.strip().replace('\u2009', ''))
#
#     return data
#     # print('*******************************************************************')
#     # print(f'word : {word}', )
#     # for definition in definitions:
#     #     print(definition.parent.text.strip().replace('\u2009', ''))
#     #     # print(definition.text.strip().replace('\u2009', ''))
#     # print('*******************************************************************')
#     # pp = pprint.PrettyPrinter(indent=2)
#     # pp.pprint(definitions)
#     # pp.pprint(sources)
#
#
# if __name__ == "__main__":
#     words = ['wu', 'zulu', 'coucou']
#     loop = asyncio.get_event_loop()
#
#     # for i in range(1, 4):
#     #     html = loop.run_until_complete(get_html(url + "/?page=" + str(i)))
#     #     soup = bs4.BeautifulSoup(html, 'html.parser')
#     #     stock_list.extend(soup.find_all('a', class_='deal__discount-kz'))
#
#     try:
#         start = time.time()
#         # coroutines = [loop.create_task(get_data(word)) for word in words]
#
#         coroutines = [loop.create_task(is_correct(word)) for word in words]
#         loop.run_until_complete(asyncio.wait(coroutines))
#
#     finally:
#         loop.close()
#         print(f'durée traitement : {time.time() - start}')
# import pandas as pandas
#
# df = pandas.DataFrame({'A': [1.1, 2.7, 5.3], 'B': [2, 10, 9], 'C': [3.3, 5.4, 1.5], 'D': [4, 7, 15]}, index=['a1', 'a2', 'a3'])
# print(df)

# from sys import stdout
from time import sleep
# for i in range(1, 20):
#     stdout.write("\r%d" % i)
#     stdout.flush()
#     sleep(1)
# stdout.write("\n") # move the cursor to the next line

# import sys
# to = 20
# digits = len(str(to - 1))
# delete = "\b" * (digits)
# for i in range(to):
#    print("{0}{1:{2}}".format(delete, i, digits), end="")
#    sleep(1)
#    sys.stdout.flush()
#
# for x in range(0, 3):
#     print(x, end=" ")

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(5,2)*100, columns=["a", "b"])
print(df)