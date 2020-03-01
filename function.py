# def exam():
#     print('You can pass')
#
#
# print(exam)  It gives Memory Location
# exam()


# def users(name, age, address):
#     return (name, age, address)
#
#
# print(users('Ram', 21, 'Ktm'))

# def users(*name):
#     print(name)
#                         Array arguments
#
# users('Ram', 'Shyam', 'Sita')


# def users(**name):
#     print(name)
#                         Keywords arguments
#
# users(name='Ram',age=21,address='Ktm')


# def take_value():
#     P = int(input('Enter a principle: '))
#     T = int(input('Enter a time: '))
#     R = int(input('Enter a rate: '))
#     return [P, T, R]
#
#
# def calculate_value():
#     SI = take_value()
#     P = SI[0]
#     T = SI[1]
#     R = SI[2]
#     return (P*T*R)/100
#
# def display_value():
#     print(calculate_value())
#
#
# display_value()

# data = lambda x, y: x + y
# print(data(10, 90))

# def users(*name,**data):
#     print(name)
#     print(data['name'])
#
#
# users('ram','sita',name='hari',age=20)


# x = 20
#
#
# def add():
#     global x
#     x += 20
#     print(x)
#
#
# add()

# def users():
#     def name(name):
#         return "Hello Python" + name
#
#     return name
#
#
# data = users()
# print(data("World"))


# def my_repeat(data, time):
#     for i in range(time):
#         print(data)
#
#
# my_repeat('Ram', 20)


# def add_sub(x, y):
#     add = x + y
#     sub = x - y
#     return [add, sub]
#
#
# print(add_sub(50, 20))


# def vote(age):
#     if age >= 18 and age <= 40:
#         print('You can vote')
#     else:
#         print('You cannot vote')
#
#     return age
#
#
# x = int(input('Enter your age: '))
# print(vote(x))

# def users(name, age):
#     print(name)
#     if age >= 0:
#          print(age)
#     else:
#          print('zero')
#
#
#
# users('Ram', -1)

# users = []


# def add_emp(num):
#     x = 1
#     while x <= num:
#         name = input('Enter name: ')
#         users.append(name)
#         x += 1
#
#
# add_emp(2)
# for name in users:
#     print(f'Your name is {name}')


# def users():
#     """This is user function"""
#     return 'Hello Python'
#
#
# # print(users.__doc__)
# print(print.__doc__)
# print(list.__doc__)

# def users():
#     def get_name(name):
#         return name
#
#     return get_name
#
#
# a = users()
# print(a('Ram'))






