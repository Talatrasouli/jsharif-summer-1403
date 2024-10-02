# def say_hello(name):
#     return f'hello {name}'

# def say_hi(name):
#     return f'hi {name}'


# def greet (greeter_func,name):
#     return greeter_func(name)

# print(greet(say_hello,'Emad'))

# ---------------------------------

# def parent():
#     print('parent')

#     def first_chid():
#         print('first_child')

#     def second_child():
#         print('second_child')

#     second_child()
#     first_chid()

# parent()

# -----------------------------

# def parent(num):
#     def first_child():
#         print('first child')

#     def second_child():
#         print('second child')
    
#     if num==1:
#         return first_child
#     else:
#         return second_child
    
# print(parent(2))

# parent(2)()
# parent(1)()

# ----------------------------

# def my_decorator(func):
#     def wrapper():
#         print('befor calling func')
#         func()
#         print('after calling func')
#     return wrapper
    
# def say_hi():
#     print('hi!')
# def say_hello():
#     print('hello')

# say_hi=my_decorator(say_hi)
# say_hi()

# --------------------------
# def my_decorator(func):
#     def wrapper():
#         print('befor calling func')
#         func()
#         print('after calling func')
#     return wrapper


# @my_decorator    
# def say_hi():
#     print('hi!')
# def say_hello():
#     print('hello')


# say_hi()

# ----------------------------
# def do_twise(func):
#     def wrapper_do_twice(*args,**kwargs):
#         func(*args,**kwargs)
#         func(*args,**kwargs)
#     return wrapper_do_twice

# @do_twise
# def greet(name):
#     print(f'Hello{name}')

# greet('Emad')

# ----------------------------------
# def repeat(num_times):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             for _ in range(num_times):
#                 func(*args,**kwargs)
#         return wrapper
#     return decorator

# @repeat(num_times=4)
# def greet(name):
#     print(f'Hello{name}')

# greet('Emad')

# -------------------

# نون بر می گردونه چون باید در رپر حتما خروجی بگیریم و حتما ریترنش کنیم
# 
# -----------------------------

def do_twise(func):
    def wrapper_do_twice(*args,**kwargs):
        func(*args,**kwargs)
        output=func(*args,**kwargs)
        return output
    return wrapper_do_twice

@do_twise
def greet(name):
    print(f'creating greet function')
    return f'Hi {name}'

output=greet('Emad')
print(output) 

# -----------------------------