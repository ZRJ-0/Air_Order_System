import random, json, os
from pymysql import *
import hashlib

class Air_Order_System_Mysql:
    def __init__(self):
        self.conn = connect(host='localhost', port=3306, user='root', passwd='root',
                               database='air_system', charset='')
        self.cur = self.conn.cursor()
        self.Chose()

    @staticmethod
    def info():
        print('----------航空订票系统(mysql)----------\n')
        print('------------1: 注册系统------------')
        print('------------2: 登录系统------------')
        print('------------3: 订票系统------------')
        print('------------4: 退票系统------------')
        print('------------5: 查询系统------------')
        print('------------6: 改签系统------------')
        print('------------0: 退出系统------------')

    @staticmethod
    def Basic_data():
        o_num = random.randint(7000, 10000)
        o_pre = random.choice(['SC', 'ZH', 'MF', 'FM', 'MU'])
        order_num = o_pre + str(o_num)
        air_des = ['北京','上海','广州','深圳','杭州']
        airlines = []
        for i in range(5):
            if(i == 4):
                airlines.append(str(i + 1) + '号航班 ' + air_des[i] + ' --> ' + air_des[0])
            else:
                airlines.append(str(i + 1) + '号航班 ' + air_des[i] + ' --> ' + air_des[i + 1])
        air_name = random.choice(["春秋航空","南方航空","中国航空","四川航空"])
        seat_num = str(random.randint(1,20)) + "排" + str(random.randint(1,6))\
                                          + str(random.choice('ABCEEF')) + "号"
        # mon = random.randint(1, 13)
        # if mon in [1,3,5,7,8,10,12]:
        #     day = random.randint(1, 32)
        # elif mon == 2:
        #     day = random.randint(1, 29)
        # else:
        #     day = random.randint(1, 31)
        # time_1 = random.randint(0, 6) * 10
        # time = str(random.randint(0, 23)) + ':' + \
        # str(time_1 if time_1 != 0 else '00')
        # depart_time = '2021-' + str(mon) + '-' + str(day) + ' ' + time
        return order_num, airlines, air_name, seat_num
    def Chose(self):
        try:
            self.info()
            num = int(input('请输入您的选择:'))
            if num == 1:
                self.Register()     # 注册系统
            elif num == 2:
                self.Login()        # 登录系统
            elif num == 3:
                self.Order()        # 订票系统
            elif num == 4:
                self.Refund()       # 退票系统
            elif num == 5:
                self.Search()       # 查询系统
            elif num == 6:
                self.Update()       # 改签系统
            elif num == 0:
                pass
        except Exception as e:
            print(e)
        finally:
            if input('是否返回主界面(y/n)? ') == 'y':
                self.Chose()
            else:
                print('成功退出系统!!!')
                self.conn.close()
                self.cur.close()

    def Search(self):
        print('{:^16}'.format('\n------订单查询系统------'))
        print('请先登录!!!')
        Username = self.Login()
        if Username != ' ':
            se_sql = 'select * from user_data where u_id=%s'
            # self.cur.execute(se_sql)
            # air_name = '春秋航空'
            # self.cur.execute('select * from user_data where air_name = %s', [air_name])
            res_len = self.cur.execute(se_sql, [Username])
            # result = self.cur.fetchone()
            # print(result == None)
            res = list(self.cur.fetchall())
            print('------您共有' + str(res_len) + '条订单信息------\n')
            for i in range(res_len):
                print('第'+ str(i + 1) + '条订单信息:')
                result = res[i]
                format_title = '{:^5}\t{:^12}\t{:^18}\t{:^12}\t{:^8}\t{:^16}'
                format_data = '{:^5}\t{:^14}\t{:^12}\t{:^12}\t{:^8}\t{:^20}'
                print(format_title.format("订单号","ID", "航班", "航班名称", "座位", "起飞时间"))
                print(format_data.format(result[0], result[1], result[2],
                                         result[3], result[4], str(result[5]) + '\n'))
            return True
        else:
            print('查询失败!!!')
            return False
    def DataInput(self):
        num = int(input('请选择你预定的航班号(1 ~ 5): '))
        depart_date = input('请选择订票的日期(例: 2月13日 --> 02-13): ')
        time = []
        for i in range(5):
            t_1 = random.randint(0, 5) * 10
            t_2 = str(random.randint(0, 23)) + ':' + \
                str(t_1 if t_1 != 0 else '00')
            if t_2 not in time:
                time.append(t_2)
            else:
                i -= 1
                continue
        time_list = []
        for i in range(5):
            time_list.append('2021-' + depart_date + ' ' + time[i])
        print('{:^16}'.format('\n------订票时间------\n'))
        i = 1
        for item in time_list:
            print(i, item)
            i += 1
        depart_num = int(input('请选择您的订票时间的序号(1 ~ 5): '))
        depart_time = time_list[depart_num - 1]
        return num, depart_time
    def Order(self):        #订票系统
        Username = self.Login()
        if Username != ' ':
            print('{:^16}'.format('\n------订票系统------\n'))
            order_num, airlines, air_name, seat_num = self.Basic_data()
            for airline in airlines:
                print(airline)
            num, depart_time = self.DataInput()
            in_sql = '''insert into user_data values (%s, %s, %s, %s, %s, %s)'''
            # ('订单2', 'zrj', '5号航班 杭州 --> 北京', '中国航空', '14排3B号', '2021-2-15 11:30')
            result = self.cur.execute(in_sql, [order_num, Username, airlines[num - 1], air_name, seat_num, depart_time])
            if result == 1:
                print('订票成功!!!')
                self.conn.commit()
            else:
                print('订票失败!!!')
        else:
            print('无法插入数据, 请先登录!!!')

    def Update(self):
        print('{:^16}'.format('\n------改签系统------\n'))
        flag = False
        if input('是否查询您的相关信息(y/n): ') == 'y':
            if self.Search() == True:
                up_num = input('请输入您要改签的订单号:')
                se_sql = '''select * from user_data where u_order = %s'''
                up_sql = '''update from user_data where u_order = %s'''
                result = self.cur.execute(se_sql, [up_num])
                if result == 1:
                    flag = True
                    print('信息如下:')
                    print(self.cur.fetchone())
                else:
                    while True:
                        up_num = input('无相关的航班信息, 请输入正确的订单号(退出: 0): ')
                        if self.cur.execute(se_sql, [up_num]) == 1:
                            print('信息如下:')
                            flag = True
                            print(self.cur.fetchone())
                            break
                        elif up_num == '0':
                            break
                        else:
                            continue
                if flag:
                    print('1: 航班', '2: 座位', '3: 起飞时间')
                    up_chose = input('请选择改签的内容: ')
                    if up_chose == '1':
                        _, airlines, _, _ = self.Basic_data()
                        print('航班信息如下:')
                        for airline in airlines:
                            print(airline)
                        num = int(input('请选择你预定的航班号(1 ~ 5): '))
                        up_sql1 = '''update user_data set airline = %s where u_order = %s'''
                        if self.cur.execute(up_sql1, [airlines[num - 1], up_num]) == 1:
                            print('改签成功, 信息如下:')
                            self.cur.execute('select * from user_data where u_order = %s', [up_num])
                            print(self.cur.fetchone())
                            self.conn.commit()
                    elif up_chose == '2':
                        seat_list = []
                        for i in range(5):
                            seat_num = str(random.randint(1,20)) + "排" + str(random.randint(1,6))\
                                              + str(random.choice('ABCEEF')) + "号"
                            seat_list.append(seat_num)
                        print('可供选择的座位如下:')
                        i = 1
                        for item in seat_list:
                            print(i, item)
                            i += 1
                        seat_upnum = int(input('请选择你预定的航班号(1 ~ 5): '))
                        up_sql2 = '''update user_data set u_seat = %s where u_order = %s'''
                        if self.cur.execute(up_sql2, [seat_list[seat_upnum - 1], up_num]) == 1:
                            print('改签成功, 信息如下:')
                            self.cur.execute('select * from user_data where u_order = %s', [up_num])
                            print(self.cur.fetchone())
                            self.conn.commit()
                    elif up_chose == '3':
                        depart_date = input('请选择订票的日期(例: 2月13日 --> 02-13): ')
                        time = []
                        for i in range(5):
                            t_1 = random.randint(0, 5) * 10
                            t_2 = str(random.randint(0, 23)) + ':' + \
                                str(t_1 if t_1 != 0 else '00')
                            if t_2 not in time:
                                time.append(t_2)
                            else:
                                i -= 1
                                continue
                        time_list = []
                        for i in range(5):
                            time_list.append('2021-' + depart_date + ' ' + time[i])
                        print('{:^16}'.format('\n------订票时间------\n'))
                        i = 1
                        for item in time_list:
                            print(i, item)
                            i += 1
                        depart_num = int(input('请选择您的订票时间的序号(1 ~ 5): '))
                        up_sql3 = '''update user_data set depart_time = %s where u_order = %s'''
                        if self.cur.execute(up_sql3, [time_list[depart_num - 1], up_num]) == 1:
                            print('改签成功, 信息如下:')
                            self.cur.execute('select * from user_data where u_order = %s', [up_num])
                            print(self.cur.fetchone())
                            self.conn.commit()
                else:
                    print('没有找到相关的航班信息!!!')
        else:
            print('成功退出改签系统!!!')

    def Refund(self):
        print('{:^16}'.format('\n------退票系统------\n'))
        if input('是否查询您的相关信息(y/n): ') == 'y':
            self.Search()
            del_order = input('请输入您要删除的订单号: ')
            del_sql = '''delete from user_data where u_order = %s'''
            result = self.cur.execute(del_sql, [del_order])
            if result == 1:
                print('退票成功!!!')
                self.conn.commit()
            else:
                while True:
                    del_order = input('退票失败, 请输入正确的订单号(退出: 0): ')
                    if self.cur.execute(del_sql, [del_order]) == 1:
                        print('退票成功!!!')
                        self.conn.commit()
                        break
                    elif del_order == '0':
                        break
                    else:
                        continue

        else:
            print('没有查询信息, 无法进行退票!!!')

    def Register(self):
        print('{:^16}'.format('\n------注册系统------\n'))
        flag = False
        while(True):
            ID = input('请输入您注册的账号(要求6位以内): ')
            if len(ID) > 6:
                print('账号不符合要求,请重新输入')
                continue
            else:
                break
        while(True):
            pwd = input('请输入您的密码(要求6位以内): ')
            if len(pwd) > 6:
                print('密码不符合要求,请重新输入')
                continue
            else:
                break
        hashed_pwd = hashlib.md5(pwd.encode()).hexdigest()
        sel_sql = '''select * from user_info'''
        self.cur.execute(sel_sql)
        result = self.cur.fetchall()
        for item in result:
            if item[0] == ID:
                print('该用户名已存在,请输入新的用户名!!!')
                if input('是否重新注册(y/n): ') == 'y':
                    self.Register()
                else:
                    flag = True
                    break
            else:
                continue
        if not flag:
            reg_sql = '''insert into user_info values (%s, %s)'''
            self.cur.execute(reg_sql, [ID, hashed_pwd])
            self.conn.commit()
            print('注册成功!!!')

    def Login(self):
        print('{:^16}'.format('\n------登录界面------\n'))
        flag = True
        ID = input('请输入您的账号: ')
        pwd = input('请输入您的密码: ')
        pwd = hashlib.md5(pwd.encode()).hexdigest()
        self.cur.execute('select * from user_info where u_id=%s', [ID])
        log_info = self.cur.fetchone()
        hashed_pwd = log_info[1]
        if log_info == None:
            print('没有这个账号, 要想登录, 请先注册!!!')
            if input('是否前往注册(y/n)? ') == 'y':
                self.Register()
            else:
                flag = False
        elif pwd != hashed_pwd:
            while True:
                pwd2 = input('密码输入错误, 请重新输入(退出请输入0): ')
                pwd_confirm = hashlib.md5(pwd2.encode()).hexdigest()
                if pwd_confirm == '0':
                    flag = False
                    break
                elif pwd_confirm == hashed_pwd:
                    print('密码输入正确, 登陆成功!!!')
                    break
                else:
                    continue
        else:
            print('密码输入正确, 登陆成功!!!')
        if flag:
            return ID
        else:
            print('登录失败!!!')
            return ' '


        # with open('userInfo_json.txt', 'r', encoding = 'utf-8') as f:
        #     info = json.load(f)
        # while(True):
        #     if info.get(ID) == pwd:
        #         print('密码输入正确!!!')
        #         username = ID
        #         break
        #     elif info.get(ID) == None:
        #         print('不存在当前账户或者每输入用户名, 您可以先进行注册!!!')
        #         choice = input('注册(r) or 退出(q) or 重新登陆(any enter): ')
        #         if choice == 'r':
        #             self.Register()
        #         elif choice == 'q':
        #             username = ' '
        #             break
        #         else:
        #             self.Login()
        #     else:
        #         print('密码输入错误, 请重新输入:')
        #         pwd = input('请输入您的密码: ')
        #         continue
        # return username


Air_Order_System_Mysql()

# user1 = Air_Order_System()    #检验 __new__ 这个初始化方法
# user2 = Air_Order_System()
# print('对象地址相同' if id(user1) == id(user2) else '对象地址不同')

