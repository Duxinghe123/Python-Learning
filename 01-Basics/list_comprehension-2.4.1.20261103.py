# Python 2.4.1：列表推导式入门
numbers = [1, 2, 3, 4, 5]  # 创建原始数字列表
squares = []  # 创建空列表，保存平方结果
for number in numbers:  # 遍历原始列表
    squares.append(number ** 2)  # 计算平方并添加到新列表
print(squares)  # 输出平方列表

numbers = [1, 2, 3, 4, 5]  # 创建原始数字列表
squares = [number ** 2 for number in numbers]  # 遍历列表并计算每个数字的平方
print(squares)  # 输出平方列表

# numbers = [2, 4, 6, 8, 10]  # 创建原始数字列表
# results = [number ** 2 for number in numbers]  # 遍历列表并计算每个数字的平方
# 错误示范 **是平方 *才是乘

numbers = [2, 4, 6, 8, 10]  # 创建原始数字列表
result = [number * 2 for number in numbers]  # 遍历列表，让每个数字乘以2
print(result)  # 输出新列表

numbers = [1, 2, 3, 4, 5, 6]  # 创建数字列表
result = []  # 创建空列表保存结果
for number in numbers:  # 遍历列表中的每个数字
    if number % 2 == 0:  # 判断数字是否为偶数
        result.append(number)  # 满足条件就添加到新列表
print(result)  # 输出所有偶数

#加入if
numbers = [1, 2, 3, 4, 5, 6]  # 创建数字列表
result = [number for number in numbers if number % 2 == 0]  # 筛选所有偶数
print(result)  # 输出筛选后的列表

# 2.4.1 练习二：筛选及格成绩
scores = [85, 42, 96, 58, 73, 60, 39]  # 创建学生成绩列表
jige=[cj for cj in scores if cj >=60]
print(jige)

#加注释
scores = [85, 42, 96, 58, 73, 60, 39]  # 创建学生成绩列表
jige = [cj for cj in scores if cj >= 60]  # 筛选大于或等于60分的成绩
print(jige)  # 输出所有及格成绩

# cj	将符合条件的成绩加入新列表
# for cj in scores	遍历原始成绩列表
# if cj >= 60	只保留大于或等于 60 分的成绩
# jige =	把筛选结果保存到变量 jige

# 同时筛选和计算
numbers = [1, 2, 3, 4, 5, 6]  # 创建数字列表
result = [number * 2 for number in numbers if number % 2 == 0]  # 筛选偶数并将其乘以2
print(result)  # 输出计算后的列表
# 2.4.1 练习三：筛选并计算成绩
# 请使用一条列表推导式：
# 1. 只保留大于或等于 60 分的成绩。
# 2. 将符合条件的每个成绩加 5 分。
# 3. 把结果保存到 result 并输出。
scores = [50, 65, 80, 45, 90]  # 创建成绩列表
jige=[cj+5 for cj in scores if cj >= 60]
print(jige)  # 输出加分后的及格成绩