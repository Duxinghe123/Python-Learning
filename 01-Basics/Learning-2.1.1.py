# Learning Python 2.1.1
# 学习变量以及基础计算
# name="xinghe"
# money=100
# a=50
# b=30
# monney=money-a-b
# result=money
# print(name+"剩余的钱是：" + str(monney))
# 变量 和 print输出

# name=input("请输入你的名字：")
# age=input("请输入你的年龄：")
# print("好的"+name+"你今年"+str(age)+"岁了")
# age=int(age)+1
# print("明年你就"+str(age)+"岁了")
# age=int(age)-1
# print(f"去年你是{age}岁") # f为格式化输出 加f的话后续不用str 但要加{}括起来
# input请在键盘输入字符串 str转换为字符串 int转换为整数 

# spmc=input("请输入商品的名称：")
# spdj=input("请输入商品的单价：")
# gmsl=input("请输入商品的购买数量：")
# result=float(spdj)*int(gmsl)
# print(f"你购买了{gmsl}个{spmc}")
# print(f"总共需支付{result}元")

# 条件判断
# if：如果条件成立，就执行对应代码。
# else：否则，执行另一段代码。
# :：表示下面开始一个代码块
# 缩进：告诉 Python 哪些代码属于这个判断
#elif 的意思是：如果前面的条件不成立，再判断这个条件
# 常见比较运算符
# 运算符	含义	示例
# >	大于	a > 10
# <	小于	a < 10
# >=	大于等于	a >= 10
# <=	小于等于	a <= 10
# ==	等于	a == 10
# !=	不等于	a != 10
# cj=input("请输入考试成绩：") #自己写的
# if int(cj)>=90:
#      print("优秀")
# elif int(cj)>=80:
#      print("良好")
# elif int(cj)>=60:
#         print("及格")
# else:
#         print("不及格")

# cj = int(input("请输入考试成绩：")) #另一种写法-chatgpt优化

# if cj >= 90:
#     print("优秀")
# elif cj >= 80:
#     print("良好")
# elif cj >= 60:
#     print("及格")
# else:
#     print("不及格")

# Python 第四课：逻辑运算符 and、or、not
# and并且 or或者 not取反
# and	并且	所有条件都为 True
# or	或者	至少一个条件为 True
# not	取反	反转 True 和 False
# type 输出这个是什么数据类型
# str 转换为字符串
# age=input("请输入你的年龄：")
# age=int(age)
# cj=input("请输入你的成绩：")
# cj=int(cj)
# if age>=18 and cj>=60:
#     print("审核通过")
# else:
#     print("审核不通过")\

# age = int(input("输入你的年龄："))
# yqh = (input("是否有邀请函 请输入yes或者no："))
# if age>=18 or yqh=="yes": # ==的意思是比较 =是赋值
#     print("允许参加")
# else: # 一定要注意加上 ：
#     print("不允许参加")

# Python 第六课：while 循环
# i=1
# while i<=10:
#     print(str(i))
#     i=i+1 #另一种写法：i += 1
# i=1
# total=0
# while i<=100:
#     total=total+i
#     i=i+1
# print(total)
# 认识 for 循环
# range() 函数可以生成一个整数序列
total=0
for i in range(2,101,2):
    total=i+total
print(total)