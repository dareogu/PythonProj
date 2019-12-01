'''
有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
'''
a = 1
b = 2
t = 0
s = []
for i in range(1, 21):
    s.append(b / a)
    t = b
    b = a + b
    a = t
print(s, '长度为{0}'.format(len(s)))
print('总和为{0}'.format(sum(s)))
