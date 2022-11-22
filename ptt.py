# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:55:18 2022

@author: ckcao
"""

from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from func_timeout import func_set_timeout, FunctionTimedOut
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from opencc import OpenCC


@func_set_timeout(200)
def link2bso(link):
    driver = webdriver.Chrome(
        r'F:\Users\Administrator\Documents\jkbd\chromedriver.exe'
        )
    driver.implicitly_wait(50)
    try:

        driver.get(link)
        sleep(9)
        try:
            a = ActionChains(driver)
            b = driver.find_element(
                By.XPATH
                , '/html/body/div[2]/form/div[1]/button'
                )
            a.click_and_hold(b).pause(1).release().pause(1).perform()
        except:
            pass
        finally:
            sleep(9)
            bso = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        return bso
    except Exception as e:
        print(0, str(e))
        driver.quit()
        return str(e) 

def timered_link2bso(link):
    try: bso = link2bso(link)
    except FunctionTimedOut: bso = 'TimedOut'
    except Exception as e:
        print(1, str(e))
        bso = str(e)
    return bso

def path_cleaner(path):
    for c in r'<>/\|:*? ': path = path.replace(c, '_')
    return path

c = OpenCC('t2s')
for i in range(598, 0, -1):
    n = 1
    try:
        for r in timered_link2bso(
            'https://www.ptt.cc/bbs/Military/index'
            + str(i)
            + '.html'
            ).find_all(class_='r-ent'):
            try:
                bs = timered_link2bso(
                    'https://www.ptt.cc'
                    + r.find('a')['href']
                    )
                with open(
                        r'F:\Users\Administrator\Documents\2022认知组前瞻预研\ptt'
                        + '\\'
                        + str(i)
                        + '-'
                        + str(n)
                        + '-'
                        + c.convert(
                            path_cleaner(
                                r.find('a').get_text()
                                )
                            )
                        + '.txt'
                        , 'a'
                        , encoding='utf8'
                        ) as f:
                    print(
                        c.convert(
                            bs.find(
                                class_='bbs-screen bbs-content'
                                ).get_text()
                            )
                        , file=f
                        )
                    n+=1
                sleep(50)
            except Exception as e:
                print(2, str(e))
                sleep(100)
                continue
    except Exception as e:
        print(3, str(e))
        sleep(100)
        continue

    
