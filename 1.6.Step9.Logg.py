# Расширение функциональности класса Loggable

import time


# Выводит в лог сообщение и добавляет к нему текущее время
class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, obj):
        list.append(self, obj)  # Добавляет в словарь объект, используя родительский метод
        self.log(obj) # применяет log из метода Loggabke

# проверка:
a = LoggableList()
a.append(10)
a.append('b')
print(a)