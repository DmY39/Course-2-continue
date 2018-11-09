import os
import os
s = set()
a = []
for current_dir, dirs, files in os.walk("main"):
    for file in files:
        if file.endswith(".py"):
            print(current_dir)
            break
            # s.add(current_dir)
# for x in s:
#     a.append(x)
# a.sort()
# itog = "\n".join(a)
# with open("tests.txt", "w") as w:
#     w.write(itog)


