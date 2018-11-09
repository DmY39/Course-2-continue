with open("dataset_24465_4.txt") as f, open("itog.txt", "w") as w:
    x = f.read().splitlines()
    for line in x[::-1]:
        print(line)