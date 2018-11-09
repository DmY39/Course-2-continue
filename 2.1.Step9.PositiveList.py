class NonPositiveError(Exception):  # наследуем исключение от Exeption
    pass


class PositiveList(list):
    def append(self, x):
        ''' Добавляет только положительные числа'''
        if x > 0:
            return list.append(self, x)
        else:
            raise NonPositiveError  # бросаем исключение

# a = PositiveList()
# a.append(5)
# a.append(-1)
# print(a)