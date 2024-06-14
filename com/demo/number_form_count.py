# 计算1,2,3,4组成一个三位数，且三位各不相同的个数，并且打印出来

count = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and j != k and i != k:
                count += 1
                print(i, j, k)
print("一共可以组成", count, "个三位数")
