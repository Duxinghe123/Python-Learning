print("学习变量以及基础计算")
# name="xinghe"
# money=100
# a=50
# b=30
# monney=money-a-b
# result=money
# print(name+"剩余的钱是：" + str(monney))

# name=input("请输入你的名字：")
# age=input("请输入你的年龄：")
# print("好的"+name+"你今年"+str(age)+"岁了")
# age=int(age)+1
# print("明年你就"+str(age)+"岁了")
# age=int(age)-1
# print(f"去年你是{age}岁")

spmc=input("请输入商品的名称：")
spdj=input("请输入商品的单价：")
gmsl=input("请输入商品的购买数量：")
result=float(spdj)*int(gmsl)
print(f"你购买了{gmsl}个{spmc}")
print(f"总共需支付{result}元")