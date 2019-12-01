#!/usr/local/bin/python3.8
'''
Created on 2018年5月13日
输入1到99999之间的数字，转换为大写中文
@: Dareo_Gu
'''
dict_num = {"0", u"零", "1", u"壹", "2", u"贰", "3", u"叁", "4", u"肆", "5", u"伍", "6", u"陆", "7", u"柒", "8", u"捌", "9",
            u"玖"}
dict_unit = {"0", "", "1", u"拾", "2", u"佰", "3", u"仟", "4", u"万"}

flag = True
while flag:
    fs = []  # 空列表
    uppercase = ''  # 空字符串
    # 如果输入的是中文，则首先解码成utf-8，再编码成gbk，确保中文输出的正常
    # num=raw_input("请输入1-99999之间的数字，若输入q则退出程序：".decode('utf-8').encode('gbk'))
    num = input("请输入1-99999之间的数字，若输入q则退出程序：")
    if num == 'q' or num == 'Q':
        print('程序结束！')
        flag = False
    elif int(num) < 1 or int(num) > 99999:
        # print "错误！请重新输入！\n".decode('utf-8').encode('gbk')
        print("错误！请重新输入！\n")
        continue
    else:
        listnum = list(num)  # 将用户输入的字符串转换成列表
        lennum = len(listnum) - 1  # 如果是5位数，实际索引是从0到4的
        for item in listnum:
            fs.append(dict_num[item])
            fs.append(dict_unit[lennum])
            lennum -= 1  # 每次递减一位，就能从实现从万到仟的转换
        uppercase = ''.join(fs)  # 列表向字符串的转换
    # print daxie.encode('gbk')
    print(uppercase.encode('gbk'))
    print('\n')
