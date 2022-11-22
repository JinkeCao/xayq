# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from func_timeout import func_set_timeout, FunctionTimedOut
import datetime
import os
from bs4 import BeautifulSoup
from json import dump
import requests

@func_set_timeout(180)
def link2ps(link):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(99)
    try:

        driver.get(link)
        sleep(1)
        r = driver.page_source
    except Exception as e:
        r = str(e) 
    finally:
        driver.quit()
    return r

def timered_link2ps(link):
    try: ps = link2ps(link)
    except FunctionTimedOut: ps = 'TimedOut'
    except Exception as e:
        ps = str(e)
        # bso = str(e)
    return ps
        
d = []
with open(
        'jkbdc.txt'
        , encoding = 'utf8'
        ) as f:
    for l in f:
        ls = l.strip().split('\t')
        d.append(
            {
                'department':ls[0]
                , 'symptom':ls[1]
                , 'href':ls[2]
                }
            )
for dd in d:
    sleep(9)
    try:
        l = []
        for bs in BeautifulSoup(
                link2ps(
                    dd['href']
                )
                ,features="lxml"
            ).find_all(class_='health-dict__overview__text health-dict__overview__texts__text'):
            l.append(
                [
                    'h1'
                    , bs.get_text()[:2]
                    ]
                )
            l += [
                  [
                    p.name
                    , p.get_text().strip()
                    ] for p in bs.find_all(
                        [
                            'p'
                            ,'li'
                            ,'h2'
                            ,'h3'
                            ]
                        ) 
                  ]
        dd['text']=l
        del dd['href']
        with open(
                'jiankang_baidu_20221109.json'
                , 'a'
                , encoding = 'utf8'
                ) as f:
            dump(
                dd
                , fp = f
                , ensure_ascii= False
                , indent=True
                )
            print(
                ''
                ,file=f
                )
    except:
        continue
        
        
