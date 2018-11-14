# количество вхождений строки t в строку s.
s, t = (input() for i in range(2))
n = 0
for i in range(len(s)):
    if s[i:].startswith(t):
        n += 1
print(n)

# Пример:
# s = "abababa"
# t = "aba"
#
# Вхождения строки t в строку s:
# 3