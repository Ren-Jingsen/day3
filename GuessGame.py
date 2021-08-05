# 1.实现步骤
import random

num = random.randint(0, 1000)
count = 0
money = 10000
b = 500
start = 1
while start <= 3:
    print('第', start, '次登录')
    name = input("请输入用户名:")
    pwd = input("请输入密码:")
    if name == 'admin' and pwd == '123456':
        print('登录成功')
        print("您的初始金币为1000")
        break
    else:
        print('登录失败')
    start = start + 1
while start == 4:
    name = input("请输入用户名:")
    pwd = input("请输入密码:")
    print('账户已锁定')
    break
while money>=500:

    count = count + 1
    chose = input("请输入您要想的数字：")
    chose = int(chose)
    if chose > num:
        money = money - b
        print("大了，你现在还剩",money,"元")
        if money<500:
            print("金币数量不足，游戏结束")
            break
    elif chose < num:
        money = money - b
        print("小了,你现在还剩", money, "元")
        if money <500:
            print("金币数量不足，游戏结束")
            break
    else:
        print("恭喜，你猜中了，数字为", num, ",您本次输入了", count, "次!恭喜你猜对了，奖励你1000金币，现在还剩",money, "元")
        money = money + 10000
        n=input("请问你是否继续(y/n)")
        if n=="y ":
            continue
        elif n=="n":
            break  # 跳出循环
        else:
            print("输入错误，结束游戏")
            break





