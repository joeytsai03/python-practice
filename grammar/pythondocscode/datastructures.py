

def list_method():
    datas_map = map(lambda x : x ** 2 , range(10))
    datas_list = list(datas_map)
    print(datas_list)
    print([x ** 2 for x in range(5)])
    print([(x,y) for x in range(0,3) for y in range(4,7)])
    #########################
    print('#' * 40)
    print([(x,y * 2) for x in range(0,3) for y in range(4,7) if x == 0 or y % x != 0])
    #等价于
    datas_list = []
    for x in range(0,3):
        for y in range(4,7):
            if x == 0 or y % x != 0:
                datas_list.append((x,y * 2))
    print(datas_list)
    #########################
    print('#' * 40)
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    print([[row[i] for row in matrix] for i in range(4)])
    #等价于
    datas = []
    for i in range(4):
        datas_tmp = []
        for row in matrix:
            datas_tmp.append(row[i])
        datas.append(datas_tmp)
    print(datas)

def zip_method():
    data_tuple = ((1,2,3,4),(5,6,7,8))
    print(data_tuple)
    print(list(zip(*data_tuple)))
    print(list(zip(data_tuple)))

def del_method():
    a = [1,2,3,4,5,6]
    del a[0]
    print(a)
    del a[0]
    print(a)
    del a[1:3]
    print(a)

if __name__ == '__main__':
    # list_method()
    # zip_method()
    del_method()
    pass