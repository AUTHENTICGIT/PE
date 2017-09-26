import requests
import os
from bs4 import BeautifulSoup
import random

def scrapyProxy():
    # 在一个网站（国内高匿代理IP）中爬取代理
    os.chdir(r'/Users/learnlearn/Desktop/proxy')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
    url = 'http://www.xicidaili.com/nn/1'
    s = requests.get(url, headers=headers)
    soup = BeautifulSoup(s.text, 'lxml')
    ips = soup.select('#ip_list tr')
    fp = open('host.txt', 'w')
    for i in ips:
        try:
            ipp = i.select('td')
            ip = ipp[1].text
            host = ipp[2].text
            fp.write(ip)
            fp.write('\t')
            fp.write(host)
            fp.write('\n')
        except Exception as e:
            print('no ip !')
    fp.close()

def proxyCheck():
    # 代理检验是否可用
    os.chdir(r'/Users/learnlearn/Desktop/proxy')
    url = 'https://www.baidu.com'
    fp = open('host.txt', 'r')
    ips = fp.readlines()
    proxys = list()
    for p in ips:
        ip = p.strip('\n').split('\t')
        proxy = 'http:\\' + ip[0] + ':' + ip[1]
        proxies = {'proxy': proxy}
        proxys.append(proxies)
    for pro in proxys:
        try:
            s = requests.get(url, proxies=pro)
            print(s)
        except Exception as e:
            print(e)
    return proxys

def getUserList(FromData):
    # 模拟发POST请求，并获得返回的json数据
    proxys = proxyCheck()
    print(proxys)
    print(random.choice(proxys))
    r = requests.post('https://wds.modian.com/ajax_backer_list', data=FromData, proxies=random.choice(proxys))
    user = r.text
    print(user)
    user = eval(user)   # 返回的数据实际是str类型，要转换为字典类型
    user_list = user['data']
    final_list = []
    for user in user_list:
        item = tuple(user.values())
        final_list.append(item)
    print(final_list)
    return final_list

def main():
    html = 'https://wds.modian.com/show_weidashang_pro/6195'
    FromData = {
        'pro_id':6195,
        'type':1,
        'page':1,
        'pageSize':30   #631
    }
    # scrapyProxy()
    userlist = getUserList(FromData)

if __name__ == '__main__':
    main()