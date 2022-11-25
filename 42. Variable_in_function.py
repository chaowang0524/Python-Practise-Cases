num = 2


def test():
    num = 1
    print("test num: %d" % num)
    num += 1


for i in range(3):
    print("num: %d" % num)
    num += 1
    test()
