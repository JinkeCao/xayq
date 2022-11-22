# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 17:17:59 2022

@author: Administrator
"""

from urllib.parse import urlencode
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from func_timeout import func_set_timeout, FunctionTimedOut


from random import choice

def genHeader():
    headerset = [
        {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
         "Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/45.0.2454.101 Safari/537.36'},
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)" "Chrome/52.0.2743.116 Safari/537.36"},
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)" "Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586"},
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"},
        {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0"},
        {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"}]
    return choice(headerset)
  

@func_set_timeout(99)
def link2bso(link):
    driver = webdriver.Chrome(r'F:\Users\Administrator\Downloads\chromedriver.exe')
    driver.implicitly_wait(33)
    try:
        driver.get(link)
        # c = 0
        # sleep(9)
        # while True:
        #     # height = driver.execute_script(r'return  document.documentElement.scrollTop || window.pageYoffset || document.body.srcollTop')
        #     driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        #     sleep(1)
        #     # next_height = driver.execute_script(r'return  document.documentElement.scrollTop || window.pageYoffset || document.body.srcollTop')
        #     c += 1
        #     if c > 5: break
        #     # elif height == next_height: break
        sleep(44)
        bso = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        return bso
    except Exception as e:
        driver.quit()
        return str(e)
        

def timered_link2bso(link):
    try: bso = link2bso(link)
    except FunctionTimedOut: bso = 'TimedOut'
    except Exception as e:
        print(str(e))
        bso = str(e)
    return bso

def path_cleaner(path):
    for c in r'<>/\|:*? ': path = path.replace(c, '_')
    return path

kwd = {
# '制裁':['加征关税', '制裁', '贸易战', '出口管制', '贸易摩擦', '出口禁令', '裁决', '管制']
# ,'军事姿态':['保持警惕', '待命', '待机', '等待', '候命', '保持警觉', '整装待命']
# ,'军事援助':['支援', '援助', '护航', '庇护', '维和', '平定', '救援', '护卫', '增援', '护航舰队']
# ,'海外撤侨':['撤侨', '接回', '引渡', '海外撤侨', '引渡回国']
# ,'任务交接':['交接', '接替', '移交', '交卸', '接任', '继任']
# ,'阅兵':['阅兵','阅兵式','阅兵仪式','受阅','阅兵典礼','国庆阅兵']
# ,'调查':['军事调查','政治调查','调查','审判','考察','视察','侦察','审讯','窥察']
'武器运行状态':['退出','退役','服役','在役','退伍','列装','现役']
,'补给获取':['航行补给','海上补给','补给','后勤物资','补给品','补充物资','作战物资','补充给养']
,'法律法规':['立法','通过','表决成立','修改','修订','删改','点窜','修正','改正']
,'选举':['选举','大选','参选']
,'提名':['提名','被提名','获提名','提名名单']
,'自然灾害':['地震','森林大火','海啸','暴雪','洪涝','巨浪','海潮','大海啸','地震海啸']
,'受伤':['烧伤','受伤','烫伤','灼伤','工伤','严重烧伤','大面积烧伤']
,'死亡':['死亡','伤亡','陨命','断命','凋落','仙游','灭亡']
,'间谍行为':['信息泄露','出卖','信息外泄','隐私泄漏','资料泄露','敏感信息泄露']
,'联系':['致函','电话','贺电','贺信','电报','唁电','慰问','致信','慰问函','致电','慰问电','致贺词','问候']
,'组织机构状态':['成立','开设','设立','关门','破产','合并','退出','创建','倒闭','建设','创设','创办','兼并']
,'转移所有权':['提供','抢购','进口','出口','购买','赠送','资助','补偿','捐款', '走私', '军火走私', '抛售', '购置', '军火交易', '进出口']
# ,'制裁':['加征关税', '制裁', '贸易战', '出口管制', '贸易摩擦', '出口禁令', '裁决', '管制']
# ,'军事姿态':['保持警惕', '待命', '待机', '等待', '候命', '保持警觉', '整装待命']
# ,'军事援助':['支援', '援助', '护航', '庇护', '维和', '平定', '救援', '护卫', '增援', '护航舰队']
# ,'海外撤侨':['撤侨', '接回', '引渡', '海外撤侨', '引渡回国']
# ,'任务交接':['交接', '接替', '移交', '交卸', '接任', '继任']
# ,'阅兵':['阅兵','阅兵式','阅兵仪式','受阅','阅兵典礼','国庆阅兵']
}
kwd = {

       # '提名':['提名','被提名','获提名','提名名单']
       '自然灾害':[
           # '地震','森林大火','海啸','暴雪','洪涝','巨浪',
           '海潮','大海啸','地震海啸']
       ,'受伤':['烧伤','受伤','烫伤','灼伤','工伤','严重烧伤','大面积烧伤']
       ,'死亡':['死亡','伤亡','陨命','断命','凋落','仙游','灭亡']
       ,'间谍行为':['信息泄露','出卖','信息外泄','隐私泄漏','资料泄露','敏感信息泄露']
       ,'联系':['致函','电话','贺电','贺信','电报','唁电','慰问','致信','慰问函','致电','慰问电','致贺词','问候']
       ,'组织机构状态':['成立','开设','设立','关门','破产','合并','退出','创建','倒闭','建设','创设','创办','兼并']
       ,'转移所有权':['提供','抢购','进口','出口','购买','赠送','资助','补偿','捐款', '走私', '军火走私', '抛售', '购置', '军火交易', '进出口']
}

n = 3818

for k in kwd:
    # n = 0
    for kw in kwd[k]:
        # if n > 9:
        #     break
        for pn in range(0, 100):
            # if n > 9:
            #     break
            try:
                bso = timered_link2bso(
                    'https://so.toutiao.com/search?'
                    + urlencode(
                    {
                        'dvpf': 'pc'
                        ,'keyword': k 
                        + ' ' 
                        + kw
                        ,'pd': 'information'
                        ,'page_num': pn
                        }
                    )
                )
                sleep(19)
                for bs in bso.find_all(class_='text-ellipsis text-underline-hover'):
                    # if n > 9:
                    #     break
                    try:
                        b = timered_link2bso(
                            'https://www.toutiao.com/article/'
                            + bs['href'].split('%2Fa')[1].split('%2F')[0]
                            )
                        sleep(19)
                        sl =  [
                                ss for ss in b.find(
                                    class_='article-content'
                                    ).stripped_strings if len(
                                        ss
                                        ) > 1
                                ]
                        c = 0
                        for w in kwd[k]:
                            # if w in '\n'.join(sl)[:512]:
                            c += '\n'.join(sl)[:512].count(w)
                            if c > 2:
                                with open(
                                        'F:\\Users\\Administrator\\Documents\\14j1_军政外\\'
                                        + str(n) + '_'
                                        + path_cleaner(k) + '_'
                                        + path_cleaner(kw) + '_'
                                        + path_cleaner(sl[0]) + '.txt'
                                        , 'a'
                                        , encoding='utf8'
                                        ) as f:
                                    print(
                                        '\n'.join(sl)[:512]
                                        , file = f
                                        )
                                    n += 1
                                    break
                                    
                    except:
                        sleep(44)
                        continue
                if len(bso.find_all(class_='text-ellipsis text-underline-hover'))  < 10:
                    sleep(9)
                    break
            except:
                sleep(44)
                continue

