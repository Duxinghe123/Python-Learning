# Python 第十二课：列表的插入与删除 2.2.2
# insert()：在指定位置插入
# 比如说
sz=[1,2,3,4,5] # 从左到右的索引依次是0 1 2 3 4
sz.insert(2, 10)  # 在索引为2的位置插入10
# remove()：根据值删除元素
# 比如说
sz.remove(3)  # 删除值为3的元素
# pop()：根据索引删除元素
# 比如说
sz.pop(1)  # 删除索引为1的元素

# append(x)	在末尾添加 x
# insert(i, x)	在索引 i 处插入 x
# remove(x)	删除第一个值为 x 的元素
# pop(i)	删除并返回索引 i 处的元素

shopping = ["苹果", "香蕉", "牛奶", "面包"]
shopping.append("鸡蛋")
shopping.insert(1,"橙子")
shopping.remove("牛奶")
shopping.pop() # 里面不填任何东西 是删除最后一个数据
print(shopping)