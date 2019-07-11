# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import asyncio
import aiofiles
import aiomultiprocess
import aiohttp

from urllib.parse import urlparse
import multiprocessing

from concurrent.futures import ThreadPoolExecutor
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

async def run(url):
    print('Scan:'+url)
    async with asyncio.Semaphore(1000):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            try:
                async with session.get('http://'+url,timeout=15) as resp:
                    if resp.status == 200:
                        u = urlparse(str(resp.url))
                        async with aiofiles.open('alive_urllll0.txt', 'a+',encoding='utf-8')as f:
                            await f.write(u.scheme+'://'+u.netloc+'\n')
                        return
            except Exception as e:
                pass

            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
                try:
                    async with session.get('https://' + url,timeout=15) as resp:
                        if resp.status == 200:
                            u = urlparse(str(resp.url))
                            async with aiofiles.open('alive_urllll0.txt', 'a+', encoding='utf-8')as f:
                                await f.write(u.scheme + '://' + u.netloc + '\n')
                            return
                except Exception as e:
                    #print(e)
                    pass


async def main(urls):
    async with aiomultiprocess.Pool() as pool:
        await pool.map(run, urls)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    inp = '不带http的.txt'
    urls = list(set([x.rstrip('/').strip() for x in open(inp, 'r', encoding='utf-8').readlines()]))
    print('目标数量:'+str(len(urls)))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls))

