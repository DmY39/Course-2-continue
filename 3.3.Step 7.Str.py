# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

# import sys
# import re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if len(re.findall(r"cat", line)) > 1:
#         print(line)


# Выведите строки, содержащие "cat" в качестве слова.
# import sys
# import re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r"\bcat\b", line):
#         print(line)
#

# Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
# import sys
# import re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r"z.{3}z", line):
#         print(line)

# Выведите строки, содержащие обратный слеш "\﻿".
# import sys
# import re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r"\\", line):
#         print(line)


# Выведите строки, содержащие слово, состоящее из двух одинаковых частей
#  (тандемный повтор).
# import sys
# import re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r"\b(\w+)\1\b", line):
#         print(line)

# В каждой строке замените все вхождения подстроки "human"
#  на подстроку "computer"﻿ и выведите полученные строки.
# import sys
# import re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub(r"human", "computer", line))

# В каждой строке замените первое вхождение слова,
# состоящего только из латинских букв "a" (регистр не важен), на слово "argh".
# import sys
# import re
#
# for line in sys.stdin:
#     line = line.strip()
#     print(re.sub(r"\ba+\b", "argh", line, count=1, flags=re.IGNORECASE))

# В каждой строке поменяйте местами две первых буквы в каждом слове,
# состоящем хотя бы из двух букв.
# import sys
# import re
#
# for line in sys.stdin:
#     line = line.strip()
#     # match = re.findall(r"\b(\w)(\w)", line)
#     # print(match)
#     # print(re.findall(r"\b(\w)(\w)", line))
#     print(re.sub(r"\b(\w)(\w)", r"\2\1", line))

# В каждой строке замените все вхождения нескольких
#  одинаковых букв на одну букву.

import sys
import re

for line in sys.stdin:
    line = line.strip()
    # match = re.findall(r"\b(\w)(\w)", line)
    # print(match)
    print(re.findall(r"(\w)\1+", line))
    print(re.sub(r"(\w)\1+", r"\1", line))

