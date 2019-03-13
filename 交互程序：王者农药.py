"""
王者农药 beta-0.1
Tang
201807026
Tangjun

print('欢迎来到王者农药，请先完成注册吧！')
print('请输入您的用户名：')
logName = input()
print('请输入您的密码：')
password = input()
print("您的用户名是",logName)
print("您的密码是",password)
print('请给您的角色起个名字:')
userName = input()
print("请给",userName,"定个角色类型吧：")
userFlag = input()
print("您好",logName,"，您的",userFlag,userName,"诞生了！！！")

"""

"""
王者农药 beta-0.1
Tang
20180801
Tangjun
"""
print("欢迎来到王者农药，请先完成注册吧！")
logName = input('请输入您的用户名：')
if not logName :
    logName = 'Tang'
password = input('请输入您的密码：')
if not password :
    password = '123456'
print("您的用户名是",logName)
print("您的密码是******")
userName = input('请给您的英雄起个名字:')
if not userName :
    userName = '玩家一'
print("请给",userName,"定个角色类型吧：")
userFlag = input()
if not userFlag :
    userFlag = '法师'
print("您好",logName,"，您的英雄",userName,userFlag,"诞生了！！！")

userHp = 100
userInfo = [userName,userHp]
print('你的英雄的名字是：',userInfo[0])

# else 
#    print('你的英雄的名字是：',userInfo[0])
print('你的英雄的hp是：',userInfo[1])
