d = {}
n = int(input())
for i in range(n):
    a = list(input().split())
    if len(a) == 1:
        d[a[0]] = []
    else:
        d[a[0]] = a[2:]
        for i in a[2:]:  # Для создания в словаре ключей, которые не были добавлены
            if i not in d:
                d[i] = []

# print(d)


def ex(errors):
    
    return

q = int(input())
errors = [input() for i in range(q)]
# print(errors)
for i in errors:
    ex(i)

# for i in range(q):
#     error = input().split()
#     print(predok, class2)
#     print(ex(error))
