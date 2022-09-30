#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
__author__ = 'Harry0597'

"""
使用说明
特点：只针对驻波数据处理计算
"""

# 计算线密度
def miu(L, f, F):
    m = (n - 1) ** 2 * ((F) / (4 * (L ** 2) * (f ** 2)))
    return m


# 求均值
def x_ba(data_list):
    leng = len(data_list)
    sum = 0
    for i in data_list:
        sum += i
    return sum / leng


print("默认频率数据为：50、55、60...75 Hz")
print("默认波节数n=3个")
n = 3
F = float(input('请输入弦线所受张力F(单位为N)：'))
data_list = input('请输入弦长数据（单位cm）, 用 逗号 或 空格 分开！\n请输入：')
print('------------------------------------------------------------')
print('除了不确定度，其他度数据请自己四舍五入！')
data_list_ = []
if ',' in data_list:
    data_list = data_list.split(',')
elif '，' in data_list:
    data_list = data_list.split('，')
else:
    data_list = data_list.split(' ')
for i in data_list:
    data_list_.append(float(i))
data_list = [float(i) * 0.01 for i in data_list_]  # cm转为m

num = 1
m_list = []  # 存放ui

for L in data_list:
    # 默认波节数全为3
    f = float(50 + 5*(num-1))
    m = miu(L, f, F)*1000
    m_list.append(float(str(m)))
    print('u{0} = {1}'.format(num, m))
    num += 1
    n = 3

u_ba = x_ba(m_list)  # u的均值
print('u均值 = {0}'.format(u_ba))
# 计算不确定度∆u
u_sum = 0
for i in m_list:
    u_sum += (i - u_ba)**2

N = len(m_list)
u_ = (u_sum / (N * (N - 1))) ** (1 / 2)

### 不确定度表示
ba = u_ba
zong = u_

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
    print('∆u= {0}'.format(tmp_zong))
    print('数据用不确定度表示为: {0} ± {1}'.format(tmp_ba, tmp_zong))
    # 相对不确定度
    E = (float(tmp_zong) / float(u_ba))*100
    print('相对不确定度: E={0}%'.format(E))

print('除了不确定度，其他度数据请自己四舍五入！')
print('------------------------------------------------------------')

