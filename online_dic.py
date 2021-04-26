# import asyncio
# import time
#
# from DicoLinkParser import dictionary_search, dictionary_exists, dictionary_exists_async
#
# print('*********************************')
# print(f"started at {time.strftime('%X')}")
#
# t1 = ['CA', 'CE', 'EA', 'EC']
# t2 = ['ACE', 'CEA', 'AEC', 'ECA', 'EAC', 'CAE']
#
#
# async def search(w):
#     time.sleep(1)
#     return await dictionary_exists_async(w)
#
#
# # async def f():
# #     global n
# #     time.sleep(1)
# #     w = t1[n]
# #     n = n + 1
# #     print(w)
# #     return await dictionary_exists_async(w)
#
#
# # async def g(w):
# #     # Pause here and come back to g() when f() is ready
# #     r = await search(w)
# #     print(w, ' ', r)
# #
# #
# # async def main():
# #     await asyncio.gather(g('CA'), g('CE'), g('EA'))
#
# async def get_result(word):
#     await asyncio.sleep(1)
#
#     x = await dictionary_exists_async(word)
#     return "Word: %s" % word + ' : ' + str(x)
#
#
# async def main():
#     for w in t1:
#         result = await get_result(w)
#         print(result)
#
#
# if __name__ == "__main__":
#
#     s = time.perf_counter()
#     asyncio.run(main())
#     elapsed = time.perf_counter() - s
#
# print(f"finished at {time.strftime('%X')}")
# print('*********************************')
#
# print(f"{__file__} executed in {elapsed:0.2f} seconds.")
