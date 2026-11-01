# 列表切片（Slicing） 2.3.1
scores = [85, 90, 76, 88, 95]  # 创建成绩列表
print(scores[1:4])  # 获取索引1到索引3的元素
# 切片最重要的规则：包含起始索引，不包含结束索引。
numbers = [10, 20, 30, 40, 50]  # 创建数字列表
print(numbers[1:4])  # 获取索引1、2、3的元素 指定开始和结束

numbers = [10, 20, 30, 40, 50]  # 创建数字列表
print(numbers[:3])  # 从开头获取前3个元素

numbers = [10, 20, 30, 40, 50]  # 创建数字列表
print(numbers[2:])  # 从索引2获取到列表末尾

numbers = [10, 20, 30, 40, 50]  # 创建数字列表
print(numbers[-1])  # 获取最后一个元素
print(numbers[-3:])  # 获取最后3个元素

numbers = [10, 20, 30, 40, 50, 60, 70, 80]  # 创建包含8个整数的列表
print(numbers[:3])  # 获取前3个元素
print(numbers[-3:])  # 获取最后3个元素
print(numbers[2:5]) # 获取索引2到索引4的元素
print(numbers[-1])
# 因为在 Python 中，[] 里面有没有冒号 :，决定了你是获取一个元素，还是获取一段元素。

