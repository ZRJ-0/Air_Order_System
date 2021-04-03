# 开发者: 朱仁俊
# 开发时间: 2021/3/18  18:22

import os,random,json

# lines = ([i for i in open('test.txt', 'r') if 'pig' not in i ])
# f = open('test_new.txt', 'w', encoding="utf-8")
# f.writelines(lines)
# f.close()
# print(lines)
# minute = random.randint(0,5)
# i = minute * 10 if minute != 0 else '00'
# print(i)

# os.mkdir('../numpy&pandas')

# test = '''{"ID": "jxw", "航班": "1号航班 北京 --> 上海", "航班名称": "春秋航空", "座位": "7排2E号", "起飞时间": "17:50"}'''
# print(json.loads(test))
#
# with open('userData.txt', 'r', encoding = 'utf-8') as f:
#     for item in f.readlines():
#         print(item.replace('\n',''))

# file = open("userInfo_json.txt", 'r', encoding='utf-8')
# papers = []
# for line in file.readlines():
#     dic = json.loads(line)
#     papers.append(dic)
#     print(dic)
#
#
# print(len(papers))
# f = open("userInfo_json.txt","r",encoding="utf-8")
#
# data = json.load(f)         #这种方法只适用于只有一条数据，多条数据报错
# print(data)

# with open('test.txt', 'r', encoding = 'UTF-8') as f:
#     data = json.loads(f.read())
#     print(data)
#     # print(f.read())

# def load_json(path):
#     import json
#     lines = []     #  第一步：定义一个列表， 打开文件
#     with open(path) as f:
#         for row in f.readlines(): # 第二步：读取文件内容
#             if row.strip().startswith("//"):   # 第三步：对每一行进行过滤
#                 continue
#             lines.append(row)                   # 第四步：将过滤后的行添加到列表中.
#     return json.loads("\n".join(lines))       #将列表中的每个字符串用某一个符号拼接为一整个字符串，用json.loads()函数加载，这样就大功告成啦！！
#
# print(load_json('test.txt'))
# with open('userInfo_json.txt', 'r') as f:
#     data = json.load(f)
# print(data.get('aaa'))

# if not os.path.exists('userData_json.txt'):
#     with open('userData_json.txt', 'a') as f:
#         f.write('{}')
# with open('userData_json.txt', 'r', encoding = 'utf-8') as f:
#     item = json.load(f)

# i = 1
    # if key == None:
    #     break
    # elif item['订单' + str(i)] == key:
    #     i += 1
    #     continue
    # else:
    #     break

# print(list(item.keys()))
#   排序字典
# next = sorted(item.items())
# print(dict(next))

# print(item)
# air_des = ['北京','上海','广州','深圳','杭州']
# airlines = []
# for i in range(5):
#     if(i == 4):
#         airlines.append(str(i + 1) + '号航班 ' + air_des[i] + ' --> ' + air_des[0])
#     else:
#         airlines.append(str(i + 1) + '号航班 ' + air_des[i] + ' --> ' + air_des[i + 1])
# # for airline in airlines:
# #     print(airline)
# print(airlines[1])

# order_num = random.randint(7000, 10000)
# order_pre = random.choice(['SC', 'ZH', 'MF', 'FM', 'MU'])
# print(order_pre + str(order_num))
# from pymysql import *
# conn = connect(host='localhost', port=3306, user='root', passwd='root',
#                                database='air_system', charset='')
# cur = conn.cursor()
# del_order = input('请输入您要删除的订单号: ')
# del_sql = '''delete from user_data where u_order = %s'''
# result = cur.execute(del_sql, [del_order])
# # result = cur.fetchone()
# print(result)
# import hashlib
#
# pwd = '123'
# # hashed_pwd = hashlib.md5(pwd.encode()).hexdigest()
# # print(hashed_pwd)
# print(hashlib.sha1(pwd.encode()).hexdigest())
# salt = ''.join(random.sample('0123456789', 4))
# print(type(salt))

num = int(input('请输入您的选择: '))
try:
    if num == 1:
        print('1')
    elif num == 2:
        print('2')
    elif num == 3:
        print('3')
    elif num == 4:
        print('4')
    elif num == 5:
        print('5')
    elif num == 6:
        print('6')
    elif num == 0:
        print('0')
except Exception as e:
    print(e)
