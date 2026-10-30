#学习变量以及基础计算
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