# 列表排序与反转 2.2.3
scores = [85, 60, 95, 72, 88]
scores.sort() #sort()：从小到大排序
# （）里填入reverse=True 从大到小排序
print(scores)

numbers = [30, 10, 50, 20, 40]
numbers.reverse() #反转列表顺序
print(numbers)

scores = [78, 95, 62, 88, 71]
scores.sort()
print(scores)
scores.sort(reverse=True)
print(scores)
scores.reverse()
print(scores)

# sorted() 与 sort() 的区别 2.2.4
# sort() 会直接修改原来的列表。
# sorted()：排序，但不改变原列表
# 常用写法	scores.sort()	sorted(scores)
scores = [78, 95, 62, 88, 71]
ascending=sorted(scores)
descending=sorted(scores,reverse=True)
# 三种输出方式的区别
# 逗号分隔	print("成绩：", scores)
print("原始成绩为：",scores)
print("升序成绩为：",ascending)
print("降序成绩为：",descending)
# str() 转换	print("成绩：" + str(scores))
print("原始成绩为：" + str(scores))
print("升序成绩为：" + str(ascending))
print("降序成绩为：" + str(descending))
# f-string	print(f"成绩：{scores}")
print(f"原始成绩为:{scores}")
print(f"升序成绩为:{ascending}")
print(f"降序成绩为:{descending}")