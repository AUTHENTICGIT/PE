import urllib.request
from bs4 import BeautifulSoup
import re

# 获得贴吧地址，并返回
def getHomeLink(keyword):
    url = 'http://tieba.baidu.com/f?kw=' + urllib.parse.quote(keyword)
    return url

# 获得所有帖子地址列表，返回所有帖子地址
def getLinkList(keyword):
    inputlink = getHomeLink(keyword)
    response = urllib.request.urlopen(inputlink)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    # 找标题
    homepage_titles = soup.find_all('a', class_ = 'j_th_tit')
    # print(homepage_titles)
    # 取标题中对应地址
    href_list = []
    for href in homepage_titles:
        # print(href)
        item = re.findall(r'/p/\d+', str(href))
        href_list.append(item[0])
    # print(href_list)
    # url = 'http://tieba.baidu.com' + href_list[0]
    title_list = []
    for href in homepage_titles:
        item = re.findall(r'<a.*? title="(.*?)".*?>.*?</a>', str(href))
        title_list.append(item[0])
    return(title_list, href_list)

# 获得每层内容
def getContent(url):
    try:
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        page_content_list = soup.find_all('div', {"class": re.compile("(d_post_content j_d_post_content )|(d_post_content j_d_post_content  clearfix)")})
        print(page_content_list)
        content_list = []
        for item in page_content_list:
            content = item.get_text()[8:-1]
            content_list.append(content)
        print(content_list)
    except UnicodeEncodeError as reason:
        print('遇到非法内容，可能含有未能识别编码！程序结束！')

# 处理页面标签
class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        #strip()将前后多余内容删除
        return x.strip()


def main():
    try:
        keyword = input('->请输入一个正确的贴吧名称：')
        if keyword == '':
            keyword = '塞纳河路边社'
        print('->前往【'+keyword+'吧】。。。。。。')
        title, title_list = getLinkList(keyword)
        for i in range(20):
            name = title[i]
            url = 'http://tieba.baidu.com' + title_list[i]
            print(i+1, name, url)
        # getContent('http://tieba.baidu.com' + title_list[0])
        inp_no = int(input('->请输入要查看帖子的编号：'))
        getContent('http://tieba.baidu.com' + title_list[inp_no-1])
    except KeyboardInterrupt as reason:
        print('程序结束！')


if __name__ == '__main__':
    main()