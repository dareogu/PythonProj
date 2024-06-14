flag = True
while flag:
    num = input("请输入一个偶数：")
    if int(num) % 2 == 1:
        print("你输入的" + num + "是奇数，不是偶数，请重新输入")
    else:
        print("你输入的" + num + "是偶数")
        flag = False
