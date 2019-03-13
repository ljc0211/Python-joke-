import tkinter

# 2018/3/5
# array = ["gkd", "ahhhhh!", "www"]
#
# print(array)
#
# array.append("wocao")
# array.append("wocao")
# array.append("wocao")
#
# array.remove("wocao")
#
# array.extend(["产业", "孙利龙","利龙大神真TM太帅了啊"])
#
# def print_each(the_list):
#     for each_item in the_list:
#         if(isinstance(each_item, list)):
#             print_each(each_item)
#         else:
#             print(each_item)
#
# print_each(array)

# 2018/3/6
# array = ["中国", "美国", 1999, 2001, ["code", "complier"]]
#
# print(array)
#
# rows = 3
# cols = 3
# matrix = [[0 for col in range(cols)] for row in range(rows)]
# for i in range(rows):
#     for j in range(cols):
#         matrix[i][j] = i * 3 + j
#         print(matrix[i][j], end = ",")
#     print('\n')
#
#
#     print(x*x for x in range(1,11))
#

# # 元组操作
# tup1 = (12, 34, 66)
# tup2 = (78, 90)
#
# tup3 = tup1 + tup2
#
# print(tup3)
#
# tup2 = (90, 78)
# print(tup2)

#2019.3.11
# class Person:#定义类的方法
#     num = 0
#
#     def SayHello(self):
#         print("Hello")
#     def __init__(self, num, weight):
#         self.num = num;
#         self.__weight = weight;#私有，只能被自身成员函数调用。（前面加了双下划线）
#     def __del__(self):
#         print("Person has not been exist!")
#     def Get__Weight(self):
#         return self.__weight
#
# p1 = Person(0, 0)#定义类的实例。
#
# p1.SayHello()#调用成员函数的方法
#
# print("p1是Person类吗？")
# print(isinstance(p1, Person))
# print("p1是str字符串吗？")
# print(isinstance(p1, str))
#
# p1.__init__(2, 3)
#
# print("p1.num的值是:")
# print(p1.num)
# print("p1.__weight的值是:")
# #print(p1.__weight)不能从外部调用私有变量，报错。
# # p1.Get__Weight()
# print(p1.Get__Weight())
#
# class Student(Person):#Student类继承Person类的写法
#     score = 0
#
# s1 = Student(4, 6)
# print("学生身高和体重：")
# print(s1.num)
# print(s1.Get__Weight())
#
# print("学生得分：")
# s1.score = 80
#
# print(s1.score)
#
# del p1#注意这里p1析构函数的用法。
#

# 2019.3.13
win = tkinter.Tk()
win.title('My first GUI Program')
win.mainloop()#进入消息循环，即显示窗口.