import random

def info():
    print('-------------欢迎来到航空订票系统----------------')
    print('-------------请选择您想办理的业务----------------')
    print('-----------------0：退出系统-------------------')
    print('-----------------1：订票-------------------')
    print('-----------------2：退票-------------------')
    print('-----------------3：订单查询系统-------------------')
    print('-----------------4：注册-------------------')
    print('-----------------5：登录-------------------')
def chose(num):
    # switcher = {1:Order(),2:Refund(),3:Search()}
    # switcher.get(num,'ERROR!!!')
    if num == 1:
        Order()
    elif num == 2:
        Refund()
    elif num == 3:
        Search()
    elif num == 4:
        Register()
    elif num == 5:
        Login()
def Order():
    Username = Login()
    if Username != ' ':
        print('欢迎来到订票系统！！！')
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
            air_num = int(input('请输入您想选择的航班号(1 ~ 5), 退出输入0:'))
            if (air_num >= 1 and air_num <= 5):
                print('您选择的航班为：' +  airlines[air_num - 1])
                if(input('是否定此航班的票(y/n)?') == 'y'):
                    print('订票成功!!!')
                    # user_order = Username + '的订单信息:\n'
                    # user_order_data = airlines[air_num - 1] + str(random.choice(['春秋航空','南方航空','中国航空','四川航空'])) + '\t'\
                    #              + str(random.randint(1,20)) + '排' + str(random.randint(1,6))\
                    #              + str(random.choice('ABCEEF')) + '号'
                    minute = random.randint(0,5)
                    item = {'ID': Username, '航班': airlines[air_num - 1],
                            '航班名称': random.choice(['春秋航空','南方航空','中国航空','四川航空']),
                            '座位': str(random.randint(1,20)) + '排' + str(random.randint(1,6))\
                                  + str(random.choice('ABCEEF')) + '号',
                            '起飞时间': str(random.randint(0,23)) + ':' + str(minute * 10 if minute != 0 else '00')
                            }
                    with open('userData.txt', 'a+', encoding = 'utf-8') as f:
                        f.write(str(item) + '\n')
                    #定义标题显示格式
                    format_title = '{:^5}\t{:^15}\t{:^12}\t{:^8}\t{:^8}'
                    format_data = '{:^6}\t{:^12}\t{:^12}\t{:^8}\t{:^10}'
                    if(input('是否查看当前的订票信息(y/n)?') == 'y'):
                        print(format_title.format('ID','航班','航班名称','座位','起飞时间'))
                        print(format_data.format(item.get('ID'),
                                 item.get('航班'),
                                 item.get('航班名称'),
                                 item.get('座位'),
                                 item.get('起飞时间')))
                    else:
                        break
                else:
                    print('订票失败!!!')
                    if(input('是否重新定票(y/n)?') == 'y'):
                        continue
                    else:
                        break
            elif air_num == 0:
                print('成功退出订票系统!!!')
                break
            else:
                print('请输出正确的航班号(1 ~ 5)')
    else:
        print('请先登录或注册新的账号!!!')
def Refund():
        print('欢迎来到退票系统！！！')
        if(input('是否查询订单信息(y/n)?') == 'y'):
            Search()
            while(True):
                air_num = int(input('请输入您想要退订的航班号(1 ~ 5):'))
                if air_num < 1 or air_num > 5:
                    print('不存在 ' + str(air_num) + '号 航班,请输入正确的航班号!!!')
                    continue
                with open('userData.txt', 'r', encoding = 'utf-8') as f_u:
                    userInfo = f_u.read()
                    update = userInfo.split('\n')
                    line_data = []
                    if len(update) - 1 == 0:
                        print('您未订票，无法进行退票')
                        break
                    flag = True
                    for i in range(len(update) - 1):
                        update_1 = eval(update[i])
                        # match_content = str(air_num) + '号航班'
                        # text = update_1['航班']
                        # pattern = re.findall(r'\d?', text)
                        # if pattern[i] == air_num:
                        #     update[i] = f_u.writelines("")
                        if str(air_num) not in update_1['航班']:
                            line_data.append(update_1)
                        else:
                            flag = False
                            continue
                    if flag:
                        print('您未定 ' + str(air_num) + '号 航班的票,无法进行退票!!!')
                        if(input('是否继续退订其他航班的票(y/n)') == 'y'):
                            continue
                        else:
                            break
                    f = open('userData.txt', 'w', encoding = 'utf-8')
                    for data in line_data:
                        f.writelines(str(data) + '\n')
                    f.close()
                    # line_data = (update_1 if str(air_num) not in update_1['航班'] else '')
                    print('成功退订 ' + str(air_num) + '号 航班!!!')
                    if(input('是否继续退票(y/n)?') == 'y'):
                        continue
                    else:
                        break
        print('您已退出退票系统!!!')
def Search():
    print('欢迎来到订单查询系统！！！')
    Username = Login()
    with open('userData.txt', 'r', encoding = 'utf-8') as f:
        info = f.read()
        info_search = info.split('\n')
        for i in range(len(info_search) - 1):
            search = eval(info_search[i])
            if search['ID'] == Username:
                format_title = '{:^5}\t{:^15}\t{:^12}\t{:^8}\t{:^8}'
                format_data = '{:^6}\t{:^12}\t{:^12}\t{:^8}\t{:^11}'
                print('用户 '+ Username + ' 第 ' + str(i + 1) + ' 条订单信息如下:')
                print(format_title.format('ID','航班','航班名称','座位','起飞时间'))
                print(format_data.format(search.get('ID'),
                                 search.get('航班'),
                                 search.get('航班名称'),
                                 search.get('座位'),
                                 search.get('起飞时间')))
def Register():
    print('欢迎来到注册本航空订票系统！！！')
    user_info = []
    while(True):
        ID = input('请输入您注册的账号(要求6位以内):')
        if len(ID) > 6:
            print('账号不符合要求,请重新输入')
            continue
        else:
            break
    while(True):
        pwd = input('请输入您的密码(要求6位以内):')
        if len(pwd) > 6:
            print('密码不符合要求,请重新输入')
            continue
        else:
            break
    info = {'ID': ID,'pwd': pwd}
    user_info.append(info)
    # if (not os.path.exists('userInfo.txt')):
    #     os.mknod('userInfo.txt')
    with open('userInfo.txt','a+',encoding = 'utf-8') as f:
        f.write(str(user_info[0]) + '\n')
        print('注册成功!!!')
def Login():
    print('{:^16}'.format('------登录界面------'))
    ID = input('请输入您的账号:')
    pwd = input('请输入您的密码:')
    with open('userInfo.txt', 'r', encoding = 'utf-8') as f:
        info = f.read()
        info_check = info.split('\n')
        for i in range(len(info_check) - 1):
            check = eval(info_check[i])
            if check['ID'] == ID:
                while(True):
                    if check['pwd'] == pwd:
                        print('密码输入正确!!!')
                        username = ID
                        break
                    else:
                        print('密码错误,请重新输入!!!')
                        pwd = input('请重新输入您的密码(退出密码验证请输入q):')
                        if pwd == 'q':
                            username = ' '
                            break
                break
            else:
                if i == len(info_check) - 2:
                    print('未注册当前账号!!!')
                    if(input('是否前往注册(y/n)?') == 'y'):
                        Register()
                    else:
                        username = ' '
                        break
                else:
                    continue
    return username
def main():
    info()
    while(True):
        num = int(input('请选择业务:'))
        if num == 0:
            print('成功退出系统!!!')
            break
        chose(num)

main()
