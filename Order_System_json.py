import random, json, os, collections

class Air_Order_System:
    #记录第一个被创建对象的引用
    instance = None                     #  单例设计模式
    def __new__(cls, *args, **kwargs):  #  确保接下来创建的对象都共有一个内存，因为new是初始化、分配空间的
        #1. 判断类属性是否为空对象             这里只在创建第一个对象时为其分配空间，其余的对象都使用相同的内存地址
        if cls.instance is None:
            #2. 调用父类方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        #3. 返回类属性保存的对象引用，之后创建的对象都只执行这一步，只使用一个内存空间
        return cls.instance
    def __init__(self):
        self.info()
        self.main()
    @staticmethod
    def info():
        print('-------------欢迎来到航空订票系统----------------')
        print('-------------请选择您想办理的业务----------------')
        print('-----------------0：退出系统-------------------')
        print('-----------------1：订票-------------------')
        print('-----------------2：退票-------------------')
        print('-----------------3：订单查询系统-------------------')
        print('-----------------4：注册-------------------')
        print('-----------------5：登录-------------------')
    def chose(self, num):
        # switcher = {1:Order(),2:Refund(),3:Search()}
        # switcher.get(num,'ERROR!!!')
        if num == 1:
            self.Order()
        elif num == 2:
            self.Refund()
        elif num == 3:
            self.Search()
        elif num == 4:
            self.Register()
        elif num == 5:
            self.Login()

    def Order(self):
        Username = self.Login()
        if Username != ' ':
            print('{:^16}'.format('\n------订票系统------\n'))
            air_des = ['北京','上海','广州','深圳','杭州']
            airlines = []
            for i in range(5):
                if(i == 4):
                    airlines.append(str(i + 1) + '号航班 ' + air_des[i] + ' --> ' + air_des[0])
                    print(airlines[i])
                else:
                    airlines.append(str(i + 1) + '号航班 ' + air_des[i] + ' --> ' + air_des[i + 1])
                    print(airlines[i])
            while(True):
                flag = True
                air_num = int(input('请输入您想选择的航班号(1 ~ 5), 退出输入0: '))
                if (air_num >= 1 and air_num <= 5):
                    print('您选择的航班为：' +  airlines[air_num - 1])
                    if(input('是否定此航班的票(y/n)? ') == 'y'):
                        if not os.path.exists('userData_json.txt'):
                            with open('userData_json.txt', 'a') as f:
                                f.write('{}')
                        with open('userData_json.txt', 'r', encoding = 'utf-8') as f:
                            item = json.load(f)
                        i = 1
                        if item:
                            for i in range(1,11):
                                if '订单' + str(i) in item.keys():
                                    i += 1
                                    continue
                                else:
                                    break
                        for key in item.keys():
                            if str(air_num) in item[key]['航班'] and Username == item[key]['ID']:
                                print('您已预此次航班, 无法继续订票!!!')
                                flag = False
                                break
                        if flag:
                            minute = random.randint(0, 5)        #[0, 5]
                            item['订单' + str(i)] = {"ID": Username, "航班": airlines[air_num - 1],
                                    "航班名称": random.choice(["春秋航空","南方航空","中国航空","四川航空"]),
                                    "座位": str(random.randint(1,20)) + "排" + str(random.randint(1,6))\
                                          + str(random.choice('ABCEEF')) + "号",
                                    "起飞时间": str(random.randint(0,23)) + ":" + str(minute * 10 if minute != 0 else "00")
                                    }
                            #对其进行排序后 是保存在列表当中的  需要转化为字典
                            item_sort = dict(sorted(item.items()))
                            with open('userData_json.txt', 'w', encoding = 'utf-8') as f:
                                f.write(json.dumps(item_sort) + '\n')
                            print('订票成功!!!')
                            #定义标题显示格式
                            format_title = '{:^5}\t{:^15}\t{:^12}\t{:^8}\t{:^8}'
                            format_data = '{:^6}\t{:^12}\t{:^12}\t{:^8}\t{:^10}'
                            if(input('是否查看当前的订票信息(y/n)? ') == 'y'):
                                print(format_title.format("ID", "航班", "航班名称", "座位", "起飞时间"))
                                print(format_data.format(item['订单' + str(i)].get("ID"),
                                         item['订单' + str(i)].get("航班"),
                                         item['订单' + str(i)].get("航班名称"),
                                         item['订单' + str(i)].get("座位"),
                                         item['订单' + str(i)].get("起飞时间")))
                            else:
                                break
                        else:
                            print('订票失败!!!')
                            if(input('是否重新定票(y/n)? ') == 'y'):
                                continue
                            else:
                                break
                    else:
                        print('请输出正确的航班号(1 ~ 5)')
                elif air_num == 0:
                    print('成功退出订票系统!!!')
                    break
        else:
            print('请先登录或注册新的账号!!!')
    def Refund(self):
        print('{:^16}'.format('\n------退票系统------\n'))
        if(input('是否查询订单信息(y/n)? ') == 'y'):
            username, num = self.Search()
            while(True):
                if num == 0:
                    if input('前往订票系统订票(any enter) or 退出退票系统(q): ') == 'q':
                        break
                    else:
                        self.Order()
                        if input('是否退出退票系统(y/n)? ') == 'y':
                            break
                        print('\n------退票中------\n')
                flag = False
                air_num = int(input('请输入您想要退订的航班号(1 ~ 5): '))
                if air_num < 1 or air_num > 5:
                    print('不存在 ' + str(air_num) + '号 航班,请输入正确的航班号!!!')
                    continue
                with open('userData_json.txt', 'r', encoding = 'utf-8') as f_u:
                    userInfo = json.load(f_u)
                if input('是否退订 ' + str(air_num) + '号 航班(y/n)? ') == 'y':
                    key = list(userInfo.keys())
                    for i in range(1, len(key) + 1):
                        if str(air_num) in userInfo[key[i - 1]]['航班'] and username == userInfo[key[i - 1]]['ID']:
                            del userInfo[key[i - 1]]
                            flag = True
                            break
                        else:
                            continue
                    if flag:
                        print('退票成功!!!')
                        with open('userData_json.txt', 'w', encoding = 'utf-8') as f:
                            json.dump(userInfo, f)
                        if input('是否继续退订其他航班的票(y/n)? ') == 'y':
                            continue
                        else:
                            break
                    else:
                        print('您未定 ' + str(air_num) + '号 航班的票,无法进行退票!!!')
                else:
                    if input('是否继续退订其他航班的票(y/n)? ') == 'y':
                        continue
                    else:
                        break
        print('您已退出退票系统!!!')
    def Search(self):
        print('{:^16}'.format('\n------订单查询系统------'))
        Username = self.Login()
        with open('userData_json.txt', 'r', encoding = 'utf-8') as f:
            info = json.load(f)
        num = 0
        key = list(info.keys())
        for i in range(1, len(key) + 1):
            if info[key[i - 1]]['ID'] == Username:
                num += 1
                format_title = '{:^5}\t{:^15}\t{:^12}\t{:^8}\t{:^8}'
                format_data = '{:^6}\t{:^12}\t{:^12}\t{:^8}\t{:^11}'
                print('用户 '+ Username + ' 第 ' + str(num) + ' 条订单信息如下:')
                print(format_title.format("ID", "航班", "航班名称", "座位", "起飞时间"))
                print(format_data.format(info[key[i - 1]]['ID'],
                                         info[key[i - 1]]["航班"],
                                         info[key[i - 1]]["航班名称"],
                                         info[key[i - 1]]["座位"],
                                         info[key[i - 1]]["起飞时间"]) + '\n')
            elif i == len(key):
                print('您还未订票, 找不到您的订单信息!!!')
                return '', 0
            else:
                continue
        return Username, num
    def Register(self):
        while(True):
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
            self.FirstRegister()
            with open('userInfo_json.txt', 'r') as f:
                info = json.load(f)   #读取文件中的内容 将其转化为对应数据类型
            for item in info.keys():
                if ID == item:
                    print('已存在用户名, 请重新输入!!!')
                    flag = True
                    break
            if flag:
                continue
            info[ID] = pwd
            with open('userInfo_json.txt','w',encoding = 'utf-8') as f:
                f.write(json.dumps(info) + '\n')
                print('注册成功!!!')
                break
    def FirstRegister(self):
        if not os.path.exists('userInfo_json.txt'):
            with open('userInfo_json.txt', 'a') as f:   #需要是a追加模式才能对不存在文件进行创建
                f.write("{}")
                print('新的用户表创建成功!!!')
    def Login(self):
        print('{:^16}'.format('\n------登录界面------\n'))
        ID = input('请输入您的账号: ')
        pwd = input('请输入您的密码: ')
        with open('userInfo_json.txt', 'r', encoding = 'utf-8') as f:
            info = json.load(f)
        while(True):
            if info.get(ID) == pwd:
                print('密码输入正确!!!')
                username = ID
                break
            elif info.get(ID) == None:
                print('不存在当前账户或者每输入用户名, 您可以先进行注册!!!')
                choice = input('注册(r) or 退出(q) or 重新登陆(any enter): ')
                if choice == 'r':
                    self.Register()
                elif choice == 'q':
                    username = ' '
                    break
                else:
                    self.Login()
            else:
                print('密码输入错误, 请重新输入:')
                pwd = input('请输入您的密码: ')
                continue
        return username
    def main(self):
        while(True):
            num = int(input('请选择业务: '))
            if num == 0:
                print('成功退出系统!!!')
                break
            self.chose(num)

Air_Order_System()
# user1 = Air_Order_System()    #检验 __new__ 这个初始化方法
# user2 = Air_Order_System()
# print('对象地址相同' if id(user1) == id(user2) else '对象地址不同')
