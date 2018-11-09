def mod_checker(x, mod = 0):
    ''' Генерирует лямбда функции от аргумента у, которая возвращает
    True, если остаток от деления у на х равен mod, а иначе False '''
    return lambda y: y % x == mod

# пример
mod_3 = mod_checker(3)

print(mod_3(3)) # True
print(mod_3(4)) # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True