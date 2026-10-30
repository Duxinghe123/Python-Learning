# Python 第十课：列表（list） 2.1.3
# 列表使用英文方括号 []，数据之间用英文逗号 , 分隔。
# 例如
cj=[50,60,70,80,90]
print(cj[0]) # 输出列表第一个元素
# Shift + Enter	临时运行选中的几行代码

scores=[85,90,76,88,95]
print(scores[2])
scores[1] = 100 #修改列表中某一位的数据
scores.append(92) #使用.append()可向列表添加新数据
print(scores)

scores = [85, 90, 76, 88, 95]
print(len(scores)) #len() 可以获取列表中元素的数量。

# 计算平均成绩
scores = [85, 90, 76, 88, 95]
total = 0
for score in scores:
    total += score
print("平均成绩为：", total / len(scores))

# 找出最高成绩

scores = [85, 90, 76, 88, 95]  # 创建列表，保存5名学生的成绩
highest = scores[0]  # 将列表中第一个成绩85作为初始最高分
for score in scores:  # 遍历列表，依次取出每一个成绩
    if score > highest:  # 判断当前成绩是否大于已记录的最高分
        highest = score  # 如果更大，就更新最高分
print("最高成绩为：", highest)  # 循环结束后，输出最终最高分

# 列表中的最小值与计数 2.2.1