import requests
import pymysql

def getFromData(pro_id, num):
    FromData = {
        'pro_id':pro_id,
        'type':1,
        'page':1,
        'pageSize':num
    }
    return FromData

def getUserList(id, num):
    # 模拟发POST请求，并获得返回的json数据
    FromData = getFromData(id, num)
    print(FromData)
    r = requests.post('https://wds.modian.com/ajax_backer_list', data = FromData)
    user = r.text
    user = eval(user)   # 返回的数据实际是str类型，要转换为字典类型
    user_list = user['data']
    final_list = []
    for user in user_list:
        item = tuple(user.values())
        final_list.append(item)
    print(final_list)
    print(final_list)
    return final_list

# 存入数据库
def insert_by_many(table):
    conn = pymysql.Connect(host='localhost', user='root', passwd='', db='wds', charset='utf8') # 建立连接
    cur = conn.cursor() # 获取游标
    try:
        sql = "INSERT INTO userlist VALUES('%s', '%s', '%s', '%s', '%s')"
        # 批量插入
        cur.executemany(sql % table)    # table是list里放的tuple
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    print('[insert_by_many executemany] total:', len(table))
    cur.close()
    conn.close()

def main():
    url = 'https://wds.modian.com/ranking_list?pro_id=6195'
    pro_id = 6195
    num = int(input('Enter Numbers: '))
    userlist = getUserList(pro_id, num)
    # insert_by_many(userlist)

if __name__ == "__main__":
    main()