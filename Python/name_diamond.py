def name_diamond(name):
    for i in range(len(name)):
        print(name[:i])
    for i in range(len(name)):
        print((' ' * i) + name[i:])

