#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
__author__ = 'Harry0597'

"""
使用说明
按照菜单从小到大顺序，依次键入数字使用即可
特点：没有数据列表，输入数据均值与总不确定度，输出不确定度表示
"""

ba = float(input('请输入数据的平均值：'))
zong = float(input('请输入它的总不确定度：'))
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