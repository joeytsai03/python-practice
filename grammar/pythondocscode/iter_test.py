class iter_d:
    def __init__(self):
        self.a = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a != 10:
            self.a += 1
            return self.a
        else:
            raise StopIteration


if __name__ == '__main__':
    # a = (1, 2)
    # b = (4, 5, (6, 10))
    # c = (7, 8, 9)
    # d = []
    # d.append(a)
    # d.append(b)
    # d.append(c)
    # e = []
    # e.extend(a)
    # e.extend(b)
    # e.extend(c)
    # print(d)
    # print(e)
    # sum()
    # datas = iter_d()
    # result = [data for data in iter(datas)]
    # print(result)
    # ds = {1: 2, 3: 4, 5: 6}
    # for d in ds.keys():
    #     print(d)
    # k_arr = ds.keys()
    # n = iter(k_arr)
    # print(next(n))
    # print(n.__next__())
    # print("1".title())
    a = '0' and int('0') or 3
    print(a)
    b = None and int('a') or 6
