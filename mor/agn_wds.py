import requests
import pymysql
import urllib.request
from bs4 import BeautifulSoup
import re
import os
import random

def getFromData(pro_id, num):
    FromData = {
        'pro_id':pro_id,
        'type':1,
        'page':1,
        'pageSize':num
    }
    return FromData

def proxyCheck():
    # 代理检验是否可用
    os.chdir(r'/Users/learnlearn/Desktop/proxy')
    fp = open('host.txt', 'r')
    ips = fp.readlines()
    proxys = list()
    for p in ips:
        ip = p.strip('\n').split('\t')
        proxy = 'http:\\' + ip[0] + ':' + ip[1]
        proxies = {'proxy': proxy}
        proxys.append(proxies)
    return proxys

def getUserList(id, num):
    # 模拟发POST请求，并获得返回的json数据
    FromData = getFromData(id, num)
    proxies = proxyCheck()
    r = requests.post('https://wds.modian.com/ajax_backer_list', data=FromData, proxies=random.choice(proxies))
    user = r.text
    user = eval(user)   # 返回的数据实际是str类型，要转换为字典类型
    user_list = user['data']
    final_list = []
    for user in user_list:
        item = tuple(user.values())
        final_list.append(item)
    print(final_list)
    return final_list

# 存入数据库
def insert_by_many(table):
    # 建立连接
    conn = pymysql.Connect(host='localhost',
                           user='root',
                           passwd='1234',
                           db='wds',
                           charset='utf8mb4')
    # 获取游标
    cur = conn.cursor()
    try:
        # 检索主键是否已存在，有就累加total_back_number数据，没有就插入
        sql = '''INSERT INTO userlist values(%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE total_back_number = total_back_number + values(total_back_number)'''
        # 批量插入
        res = cur.executemany(sql, table)    # table是list里放的tuple
        conn.commit()
        print(res)
    except Exception as e:
        print(e)
        conn.rollback()   # 失败回滚
    print('[insert_by_many executemany] total:', len(table))
    cur.close()
    conn.close()

def getUrl(html):
    # 在地址找pro_id
    pro_id = int(re.findall(r'.+_pro/([0-9]+)', html)[0])
    # 在html标签找参与人数
    # 主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=html, headers=headers)
    html_data = urllib.request.urlopen(req).read().decode('utf8')
    soup = BeautifulSoup(html_data, 'html.parser')
    join_number = str(soup.find_all('div', class_='b')[0])
    num = int(re.findall(r'<span>([0-9]+)</span>', join_number)[0])
    print(pro_id, num)
    return pro_id, num

def main():
    # html = str(input('Enter Web Address: '))
    html = 'https://wds.modian.com/show_weidashang_pro/4785'
    pro_id, num = getUrl(html)
    userlist = getUserList(pro_id, num)
    insert_by_many(userlist)

if __name__ == "__main__":
    main()