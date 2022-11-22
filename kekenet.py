

# from json import dumps
from random import choice
from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup
from time import sleep#, mktime, strptime
# from uuid import uuid5, NAMESPACE_DNS
# from urllib.parse import urlencode
# import datetime
# from re import findall
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def genHeader():
    headerset = [
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
            }
        , {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
            }
        , {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
            }
        ]
    return choice(headerset)

def link2bs(link):
    req = Request(
        link
        , headers=genHeader()
        )
    try:
        res = urlopen(
            req
            , timeout = 59
            ).read()
    except Exception as e:
        res = str(e)
        pass
    finally:
        sleep(9)
        return BeautifulSoup(
            res
            , features="lxml"
                )

def path_cleaner(path):
    for c in r'<>/\|:*? ': path = path.replace(c, '_')
    return path

for i in range(1,13):
    try:
        if i == 12:
            l = 'https://www.kekenet.com/Article/16653/'
        else:
            l = 'https://www.kekenet.com/Article/16653/List_' + str(i) + '.shtml'
        for i1, i3 in [
                [
                    i2.a['href']
                    , i2.get_text().strip()
                    ]
                for i2 
                in link2bs(l).find_all('ul')[-3].find_all('h2')
                ]:
            try:
                p = 'F:/Users/Administrator/Music/kekenet/' + path_cleaner(i3) + '.mp3'
                urlretrieve(
                    link2bs(
                        'https://www.kekenet.com/'
                        + link2bs(i1).find(
                            'span'
                            , style='margin-top:15px;'
                            ).a['href']
                        ).find_all(
                            'a'
                            , style='color:#195A94;'
                            )[1]['href']
                    , filename=p
                    )
                sleep(9)
            except Exception as e:
                print(
                    str(
                        e
                        )
                    )
                sleep(9)
                continue
    except Exception as e:
        print(
            str(
                e
                )
            )
        sleep(9)
        continue
