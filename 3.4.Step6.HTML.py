import requests
import re

# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.


def htmv2():
    ss1 = input()  # Запишем ссылки А и В в переменные
    ss2 = input()
    res1 = requests.get(ss1)  # Делаем запрос по А
    res2 = re.findall(r"htt.+tml", res1.text)  # Создаем список со ссылками С по рег.выражению
    for i in res2:  # Проходим по списку ссылок С
        res3 = requests.get(i)  # делаем запрос по каждой ссылке С
        res4 = re.findall(r"htt.+tml", res3.text)  # Получаем список ссылок B по запросу из С
        if ss2 in res4:  # Если ссылка В входит в список, то выводим Да
            return "Yes"
    return "No"


print(htmv2())


