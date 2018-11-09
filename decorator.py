def f1():
    print('function 1')

def f2():
    print('function 2')

def decorator(func):
    def wrapeer():
        print('before')
        func()
        print('after')
    return wrapeer

new_1 = decorator(f1)
new_2 = decorator(f2)

new_1()
new_2()