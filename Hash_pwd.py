# 开发者: 朱仁俊
# 开发时间: 2021/3/31  14:41
import hashlib
import hmac
import random

db = []
class Hash_pwd:
    def __init__(self):
        self.chose()

    def chose(self):
        num = input('请选择哈希加密的方式: ')
        if num == '1':
            self.Hash_md5()
        elif num == '2':
            self.Hash_addsalt()
        elif num == '3':
            self.Hash_HMAC()
            if input('是否进行解密(y/n): ') == 'y':
                self.Check_HMAC(db)

    def Hash_md5(self):             #md5算法
        pwd = input('请输入想要加密的密码: ')
        hash_pwd = hashlib.md5(pwd.encode()).hexdigest()
        print(hash_pwd)

    def Hash_addsalt(self):         # 加盐算法
        pwd = input('请输入想要加密的密码: ')
        salt = ''.join(random.sample('0123456789', 4))
        hash_pwd = hashlib.sha256(f'{salt}{pwd}'.encode()).hexdigest()
        print(f'{salt}:{hash_pwd}')
        # print('{0}:{1}'.format(salt, hash_pwd))   #上下两种方式等价

    def Check_addsalt(self):
        pass
    def Hash_HMAC(self):            # 消息认证码算法
        pwd = input('请输入想要加密的密码: ')
        salt = ''.join(random.sample('0123456789', 4))
        hash_pwd = hmac.new(bytes(salt.encode()), msg=pwd.encode(),
                            digestmod='sha256').hexdigest()
        db.append({'password': hash_pwd, 'salt': salt})

    def Check_HMAC(self, db):
        pwd = input('请输入想要解密的密码: ')
        cor_pwd = db[0]['password']
        salt = db[0]['salt']
        hash_pwd = hmac.new(bytes(salt.encode()), msg=pwd.encode(),
                            digestmod='sha256').hexdigest()
        if cor_pwd == hash_pwd:
            print('解密成功!!!')
        else:
            print('解密失败!!!')

Hash_pwd()
print(db)
