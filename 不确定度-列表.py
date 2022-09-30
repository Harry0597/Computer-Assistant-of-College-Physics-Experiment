#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
__author__ = 'Harry0597'

"""
使用说明
按照菜单从小到大顺序，依次键入数字使用即可
特点：一次性输入数据列表与∆仪，一次性给出各数据
"""


# 求均值
def x_ba(data_list):
    leng = len(data_list)
    sum = 0
    for i in data_list:
        sum += i
    return sum / leng


mode = 597
data_list = []
ba = 0  # 均值
s = 0  # 标准偏差
A = 0  # A类不确定度
B = 0  # B类不确定度
zong = 0  # 总不确定度
while mode:
    try:
        data_list = input('请输入数据, 用 逗号 或 空格 分开！\n')
        YI = float(input('请输入∆仪：'))
        print('------------------------------------------------------------')
        data_list_ = []
        if ',' in data_list:
            data_list = data_list.split(',')
        elif '，' in data_list:
            data_list = data_list.split('，')
        else:
            data_list = data_list.split(' ')
        for i in data_list:
            data_list_.append(float(i))
        data_list = data_list_

        # 初始化参数
        ba = 0  # 均值
        s = 0  # 标准偏差
        A = 0  # A类不确定度
        B = 0  # B类不确定度
        zong = 0  # 总不确定度
        del data_list_

        if data_list:
            ba = x_ba(data_list)  # 平均值
            print('平均值 为：{0}'.format(ba))

        if ba:
            he = 0
            for i in data_list:
                he += (i - ba) ** 2
            s = (he / (len(data_list) - 1)) ** (1 / 2)
            print('标准偏差S 为：{0}'.format(s))

        if s:
            A = s / (len(data_list) ** (1 / 2))
            print('A类不确定度 为：{0}'.format(A))

        B = YI / (3 ** (1 / 2))
        print('B类不确定度 为：{0}'.format(B))

        if A and B:
            zong = ((A ** 2) + (B ** 2)) ** (1 / 2)
            print('总不确定度 为：{0}'.format(zong))

        if ba and zong:
            ba = str(ba) + '0' * 9  # 补充位数
            ba_ = str(ba)
            zong_ = str(zong)
            ba_index = 0  # 需要舍、入位
            """
            总不确定度处理
            """
            for i in zong_:
                if i != '.':
                    if i != '0':
                        ba_index = zong_.find(i)  # 找到第一位非零数字的位置
                        break
            if int(zong_[ba_index]) >= 4:  # 保留一位
                if len(zong_) == len(zong_[:ba_index + 1]):  # 后面没有数
                    zong = float(zong_[:ba_index] + zong_[ba_index])
                elif int(zong_[ba_index + 1]) > 0:  # 后面有数且后一位数>0，进位
                    zong = float(zong_[:ba_index] + str(int(zong_[ba_index]) + 1))
                else:  # 后面有数后一位数=0，舍
                    zong = float(zong_[:ba_index] + zong_[ba_index])
            else:  # 保留两位
                if len(zong_) == len(zong_[:ba_index + 1]):  # 一位后没有数
                    zong = zong_[:ba_index + 1] + '0'
                elif len(zong_) == len(zong_[:ba_index + 2]):  # 两位后没有数
                    zong = zong_
                elif int(zong_[ba_index + 2]) > 0:  # 两位后有数且后一位数>0，进位
                    if zong_[ba_index + 1] != '9':
                        zong = float(zong_[:ba_index + 1] + str((int(zong_[ba_index + 1]) + 1)))
                    else:
                        zong = str(zong_[:ba_index]) + str(int(zong_[ba_index]) + 1) + '0'
                else:  # 后面有数后一位数=0，舍
                    zong = float(zong_[:ba_index + 1] + zong_[ba_index + 1])
            tmp_zong = str(zong)

            """
            平均数处理
            """
            ba_index += (len(ba.split('.')[0]) - 1)  # 19.xxx 那么ba_index是对<10而言的
            # 四舍
            if int(ba_[ba_index + 1]) <= 4:
                ba = float(ba_[:ba_index + 1])
            # 六入
            elif int(ba_[ba_index + 1]) >= 6:
                ba = float(ba_[:ba_index] + str(int(ba_[ba_index]) + 1))
            # 五凑偶
            elif int(ba_[ba_index + 1]) == 5:
                if len(ba_) > len(ba_[:ba_index + 2]):  # 五后面有数
                    ba = float(ba_[:ba_index] + str(int(ba_[ba_index]) + 1))
                else:
                    if int(ba_[ba_index]) % 2 == 0:  # 偶数舍
                        ba = float(ba_[:ba_index] + str(int(ba_[ba_index])))
                    else:  # 入
                        ba = float(ba_[:ba_index] + str(int(ba_[ba_index]) + 1))
            tmp_ba = str(ba)
            print('数据用不确定度表示为: {0} ± {1}'.format(tmp_ba, tmp_zong))
            print('------------------------------------------------------------')
    except:
        print('\n---------------输入有误，请重新输入！---------------\n')

"""
潜在bug：
九的进位问题
"""
