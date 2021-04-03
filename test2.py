# 开发者: 朱仁俊
# 开发时间: 2021/3/23  22:48
import FileManager


def login():
    # 1.输入账号和密码
    user_name = input('请输入账号:')
    password = input('请输入密码:')

    # ====================csv文件=====================
    # # 2.获取之前注册过的账号信息
    # all_user = FileManager.read_csv_file('files/userInfo.csv')
    #
    # # 3.判断登录账号是否已经注册
    # for item in all_user:
    #     # 如果已经注册过
    #     if item['账号'] == user_name:
    #         # 判断密码是否正确
    #         if item['密码'] == password:
    #             print('登录成功!')
    #             # 登录成功后要完成的功能接口....
    #         else:
    #             print('登录失败!密码错误！')
    #         break
    # else:
    #     print(f'登录失败！{user_name}没有注册!')

    #  ====================json文件=====================
    all_user = FileManager.read_json_file('files/userInfo.json')
    pw = all_user.get(user_name, '没有注册!')
    if pw == '没有注册!':
        print(f'登录失败!{user_name}没有注册')
    elif pw != password:
        print('登录失败!密码错误')
    else:
        print('登录成功！')


def register():
    """注册"""
    # 1.输入用户名和密码
    user_name = input('请输入用户名:')
    pass_word = input('请输入密码:')
    # 2.判断当前用户名是否已经注册
    # ================csv文件=================
    # # 1）获取已经注册过的所有的账号信息
    # # [{'账号': 'aaa', '密码': '123456'}, {'账号': 'bbb', '密码': '123456'}]
    # all_user = FileManager.read_csv_file('files/userInfo.csv')
    # # 2）判断当前账号是否已经注册过
    # for item in all_user:
    #     if item['账号'] == user_name:
    #         print(f'注册失败! {user_name}已经注册过!')
    #         break
    # else:
    #     print('注册成功!')
    #     FileManager.write_row_csv_file('files/userInfo.csv', [user_name, pass_word])
    #     # FileManager.write_row_csv_file('files/userInfo.csv', {'账号': user_name, '密码': pass_word})

    # ========================json文件===========================
    # 1）获取已经注册过的所有的账号信息
    all_user = FileManager.read_json_file('files/userInfo.json')
    # 2）判断当前账号是否已经注册过
    if user_name in all_user:
        print(f'注册失败！{user_name}已经注册过!')
    else:
        all_user[user_name] = pass_word
        FileManager.write_json_file('files/userInfo.json', all_user)
        print('注册成功！')


def main():
    main_page = FileManager.read_text_file('files/mainPage.txt')
    while True:
        # 1.展示登录页面
        print(main_page)
        # 2.给出选择
        value = input('请选择(1-3):')
        # 3.根据不同的选中完成不同的功能
        if value == '1':
            # print('登录')
            login()
        elif value == '2':
            # print('注册')
            register()
        elif value == '3':
            exit()
        else:
            print('输入有误!')


if __name__ == '__main__':
    main()
