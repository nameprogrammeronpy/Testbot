# print("result", max(1,3,-4,5,0), sep='\n', end=' ! ')
# print(round(5/2))
# result
# 5 ! 2
# a = 1.232   #float
# word = "result " #string
# boolean = True #bool
# c = 5 #int
# d = '5' #string
# print(word, c)
# print(c+int(d))
# print(word +str(c+int(d)))
from time import process_time_ns


# k = input("Введите число конечных автоматов ")
# k = int(k)
# while k>0:
#     k=str(k)
#     n = input("Введите число состояний "+k+" автомата ")
#     m = input("Введите число переходов "+k+" автомата ")
#     d = 19*int(m) + (int(n) + 239)*(int(n) + 366) / 2
#     print(d)
#     k = int(k)
#     k=k-1
# word=input("a ")
# print(word*2)
# word= True
# print("are lives matter?",word)
# user_data=int(input("20/2*2: "))
#
# if user_data==5 :
#     print("Your answer is correct")
#
# elif user_data !=5 and user_data > 5:
#     print("Your answer is more than right answer3")
# data = input("Enter a mark : ")
# x="idk"
# a = 5 if data == 'five' else x
# print(a)
# for a in range(2,10,2):
#     print(a)
# count = 0
# word=input()
# for i in word:
#     if(i=="o" or i=="O"):
#         count+=1
# print(count)
# bool= True
# while bool:
#     if input("enter a number : ") == "exit":
#         bool = False
# a=int(input("Enter "))
#
# for a in range(a,a+10):
#     if (a == 8):
#         break
#     if a%2==0:
#         continue
#     print(a)
#     a += 1
# numbers = [5,1,2,3,4,True, 6,7,8] # Список
# numbers[5] = False
# print(numbers[-1])
# numbers.append(True)
# numbers.insert(7,100)
# numbers.extend([1.4,1.5,1.6])
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers.pop(-1) # В скобках можно индекс элемента писать
# print(numbers)
# numbers.remove(2)
# print(numbers)
# # numbers.clear()
# print(numbers.count(5))
# print(len(numbers))
# nums = [9,1,2,3,4,5,6,7,8,]
# for i in nums:
#     i *= 2
#      print(i)

# i=0
# while i<len(nums):
#     print(nums[i])
# #    i+=1
# word='hello world'
# print(word.upper())
# print(word.capitalize()) # Заглавная буква начала строки
# print(word.find('l'))


# word = input("Enter your hobby: ")
# hobby = word.split(',')
# for i in range(len(hobby)):
#     hobby[i] = hobby[i].capitalize()
# remark=' ,'.join(hobby)
# print(remark)

# word = 'Football'
# print(word[1:-1:2])
# #1-начало,2-конец,3 шаг
# a=[9,1,2,3,4]
# print(a[2:])
# print(a[::-1])

# data = 1,2,3,4,5 # Kортеж (tuple)
# data[2]=3 - NOO
# print(data[1:5:2])
# print(data.count(2))
# for i in (data):
#     if(i<5):
#         print(i)
# word ='nope'
# print(tuple(word))


# b = ['kz','cn','uz','kr','sg','in']
# country = {'Asia' : b}  # Словари (dict)
# c=input('Choose a region ')
# if c in country:
#     print(country[c])
# i=int(input('choose a country in this region '))
# print(b[i-1])


# Kazakhstan = dict(language='Kazakh', population=20000000, capital='Astana')
# for key,value in Kazakhstan.items():
#     print(key,' - ',value)
# Kazakhstan.pop('population')
# (Kazakhstan.popitem()
# print(Kazakhstan)
# Kazakhstan['capital']='Nursultan'
# print(Kazakhstan)


# personality = dict(
#     user_1= dict(
#         username="Abzal",
#         password="Abzal2001",
#         age= dict(
#             day=16,
#             month='July',
#             year=2009)),
#     user_2= dict(
#         username="Almaz",
#         password="Almaz1902",
#         age= dict(
#             day=9,
#             month='November',
#             year=1974))
# )
# b=input('Which user do you want? ')
# if b in personality:
#     print(personality[b])

# data=set('hello')
# data = {1,2,3,4,5,2}
# data.add(True)
# data.update(['12',7,])
# data.pop()
# data.clear()
# print(data)

# nums=[1,2,3,4,5,4,3,2,1]
# nums2=set(nums)
# print(nums2)
# nums3=frozenset(nums2)
# nums3.add(2)   #НЕЛЬЗЯ добавлять
# print(nums3)

# def fun_func(word):
#     print('Hello',word)
#
# fun_func('Abzal')
# fun_func('12')

# def main(a,b,c):
#     res=a+b+c
#     return res
# res=main(3,2,1)
# print(res)

# def summa(a,b,c):
#     return a+b+c
# May=summa('You are ','good person,',' Arthur Morgan')
# print(May)
# print(summa('You are ','good person,',' Arthur Morgan'))

# nums=(input('Enter a numbers : '))
# nums=nums.split(',')
# min=nums[0]
# for i in nums:
#     if i<min:
#         min=i
#
# print(min)

# def minimal(list):
#     min=list[0]
#     for i in list:
#         if i<min:
#             min=i
#     return min
# lis=input("enter numbers : ")
# lis=lis.split(',')
# min1=minimal(lis)
# lis2=input("enter numbers : ")
# lis2=lis2.split(',')
# min2=minimal(lis2)
# if min1<min2:
#     print(min1)
# else:
#     print(min2)

# func = lambda x,y:x+y
# print(func(1,2))


# data = input("Enter : ")
# file = open('data/text.txt', 'w')   #Переписывание
# file.write('Hello \n')
# file.write(data)
#
# file.close()
#
# file=open('data/text.txt', 'a')   #Добавление
# file.write('Hello \n')
# file.write('Hello \n')
# file.close()
#
# file=open('data/text.txt', 'r')  #Чтение
# # print(file.read(5))
# for line in file:
#     print(line,end='')
# file.close

# a = 0
# while a==0:
#     try:
#         x = int(input("Enter a number "))
#         print(x)
#         a+=1
#     except ValueError:
#         print("Invalid input")


# try:
#     x = int(input("Enter a number "))
# except ValueError:
#     print("Invalid input")
#
# else:
#     print('your number is ',x)    #Если условие(try) сработает
# finally:
#     print('the program is done')   #В конце в любом случае

# try:
#     file=open('data/text2.txt', 'r')   #Не существующий файл
#     file.read()
# except FileNotFoundError:
#     print("File not found")
# finally:
#     file.close()

# try:
#     with open('data/text2.txt', 'r', encoding='utf-8') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('File not found')

# import time
# print(12)
# time.sleep(3)
# print(34)

# import datetime as dt
# print(dt.datetime.now().year)   #время

# import sys,os,platform  #sys-система, os,platform- операционная система(ОС)
# # print(sys.path)
# # print(os.name)
# print(platform.system())

# from math import sqrt as s,ceil
# print(ceil(s(81)))

# name=input("Enter your name: ")
# def urname():
#     print("Hello " + name)
# urname()

# import mymodul as m
# print(m.urname())
#
# from mymodul import slozhenie as plus
# print(plus(3,-3,0))
# import cowsay
# cowsay.trex('I love ')

# class cat:
#     name = None
#     age = None
#     ishappy = None
#     colour = None
#     def __init__(self, name, age = None, ishappy = 'Unknown', colour = None):
#         self.set_data(name, age, ishappy, colour)
#         self.get_data()
#
#     def set_data(self, name, age, ishappy, colour  ):
#         self.name = name
#         self.age = age
#         self.ishappy = ishappy
#         self.colour = colour
#     def get_data(self):
#         print(self.name, self.age, self.ishappy, self.colour)
# cat1= cat()
# cat1.name= 'Барсик'
# cat1.age = 3
# cat1.ishappy = True
# cat1.colour = 'Оранжевый'
#
# cat2 = cat()
# cat2.name= 'Сергей'
# cat2.age = 8
# cat2.ishappy = False
# cat2.colour = 'Серый'
# print(cat1.name, cat1.age, cat1.ishappy, cat1.colour)
# print(cat2.name, cat2.age, cat2.ishappy, cat2.colour)

# cat3= cat()
# cat3.set_data('Рекс',2, True, 'Черный')  #Сокращенно,легче
# cat3.get_data()

# cat1=cat('Rex',9,'','Black')
# cat2=cat('Bars',2,True, 'Orange')

# class building:
#     year = None
#     city = None
#     def __init__(self,year,city):
#         self.year=year
#         self.city=city
#     def get_info(self):
#         print("Year :",self.year,", City :",self.city)
# class School(building):
#     capacity = None
# class House(building):
#     Floor = None
#     def __init__(self,year,city,Floor):
#         super(House,self).__init__(year,city)
#         self.Floor=Floor
#     def get_info(self):
#         super(House,self).get_info()
#         print("Floor:",self.Floor)
# class Store(building):
#     M2= None
#
# house = House(2011,'Almaty',9)
# house.get_info()
# school = School(2018,'Almaty')
# school.get_info()
# store=Store(2022,'Almaty')

# import webbrowser
# def validator(func):
#     def wrapper(url):
#         if "."in url:
#             func(url)
#         else:
#             print("Wrong URL")
#     return wrapper
# @validator
#
# def open_url(url):
#     webbrowser.open(url)
# open_url("https://wwwyoutubecom/watch?v=e3PqdUb7fLA&t=630s")