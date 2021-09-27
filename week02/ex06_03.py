def search(name):
    f = open('student.txt', 'r')
    datalist = f.readlines()

    for data in datalist:
        if name in data:
            a = data.split('|')
            print(f"average{a[4]}, grade{a[5]}")
            f.close()
            return

    print('없음')
    f.close()

search('Sun')
search('Jacob')
search('Yuna')