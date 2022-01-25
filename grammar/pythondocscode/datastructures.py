def list_method():
    datas_map = map(lambda x: x ** 2, range(10))
    datas_list = list(datas_map)
    print(datas_list)
    print([x ** 2 for x in range(5)])
    print([(x, y) for x in range(0, 3) for y in range(4, 7)])
    #########################
    print('#' * 40)
    print([(x, y * 2) for x in range(0, 3) for y in range(4, 7) if x == 0 or y % x != 0])
    # 等价于
    datas_list = []
    for x in range(0, 3):
        for y in range(4, 7):
            if x == 0 or y % x != 0:
                datas_list.append((x, y * 2))
    print(datas_list)
    #########################
    print('#' * 40)
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    print([[row[i] for row in matrix] for i in range(4)])
    # 等价于
    datas = []
    for i in range(4):
        datas_tmp = []
        for row in matrix:
            datas_tmp.append(row[i])
        datas.append(datas_tmp)
    print(datas)


def zip_method():
    data_tuple = ((1, 2, 3, 4), (5, 6, 7, 8))
    print(data_tuple)
    print(list(zip(*data_tuple)))
    print(list(zip(data_tuple)))


def del_method():
    a = [1, 2, 3, 4, 5, 6]
    del a[0]
    print(a)
    del a[0]
    print(a)
    del a[1:3]
    print(a)
    del a
    try:
        b = a
    except Exception as ex:
        print('after del use a exception ! ' + str(ex))
    a = []
    print('a = ' + str(a))


def sequences_method():
    seq = (1)
    print('seq = (1) : ' + str(seq))
    seq = (1,)
    print('seq = (1,) : ' + str(seq))
    seq = 1, 2, '3'
    print("seq = 1, 2, '3' : " + str(seq))
    seq = (1, 2, '3')
    print("seq = (1, 2, '3') : " + str(seq))
    seq_tmp1 = (1, 2, 3)
    seq_tmp2 = (4, 5, 6)
    seq = seq_tmp1, seq_tmp2
    print("seq = seq_tmp1 , seq_tmp2 : " + str(seq))
    seq = *seq_tmp1, *seq_tmp2
    print("seq = *seq_tmp1 , *seq_tmp2 : " + str(seq))
    seq = [*seq_tmp1, *seq_tmp2]
    print("seq = [*seq_tmp1, *seq_tmp2] : " + str(seq))

    ######################################
    print('-' * 40)
    tuple = (1, 2, 3)
    data_list = [1, 2, 3]
    try:
        tuple[0] = 0
    except Exception as ex:
        print('tuple[0] = 0 ex : ' + str(ex))
    data_list[0] = 0
    print('tuple = ' + str(tuple))
    print('data_list = ' + str(data_list))
    seq = (1, 2, 3)
    x, y, z = seq
    print(str(x) + ' ' + str(y) + ' ' + str(z) + ' ')


def set_method():
    data_set = set()
    print('set() type is ' + str(type(data_set)))
    data_set = {}
    print('{} type is ' + str(type(data_set)))
    data_set = {'1'}
    print('{1} type is ' + str(type(data_set)))
    data_set = {'key': 'value'}
    print("{'key':'value'} type is " + str(type(data_set)))
    data_set = {('1', '2', '3')}
    print("{('1','2','3')} : " + str(data_set))
    data_set = {*('1', '2', '3')}
    print("{*('1','2','3')} : " + str(data_set))
    data_set = {*('1', '1', '2', '3')}
    print("{*('1','1', '2', '3')} : " + str(data_set))
    data_set = set('abc123')
    print("set('abc123') : " + str(data_set))
    data_set = {x for x in 'abc123a1' if x not in 'a12'}
    print("{x for x in 'abc123a1' if x not in 'a12'} : " + str(data_set))
    data_set1 = {'11', '2', '3', '1', '4'}
    data_set2 = {'5', '7', '3', '11', '4'}
    print("data_set1 - data_set2 : " + str(data_set1 - data_set2))
    print("data_set1 | data_set2 : " + str(data_set1 | data_set2))
    print("data_set1 & data_set2 : " + str(data_set1 & data_set2))
    print("data_set1 ^ data_set2 : " + str(data_set1 ^ data_set2))


def dict_method():
    dict = {}
    print('dict = {}  =>  ', str(dict))
    dict['k1'] = 'v1'
    print("dict['k1'] = 'v1'  =>  " + str(dict))
    del dict['k1']
    print("del dict['k1']  =>  " + str(dict))
    dict['k1'] = 'v1'
    print("dict['k1'] = 'v1'  =>  " + str(dict))
    dict['k3'] = 'v3'
    print("dict['k3'] = 'v3'  =>  " + str(dict))
    dict['k2'] = 'v2'
    print("dict['k2'] = 'v2'  =>  " + str(dict))
    print("sorted(dict)  =>  " + str(sorted(dict)))
    print("dict  =>  " + str(dict))
    print("list(dict)  =>  " + str(list(dict)))
    print("'k1' in dict  =>  " + str('k1' in dict))
    print("'k4' in dict  =>  " + str('k4' in dict))


class User():
    username = ''
    name = ''
    phone = ''

    def __init__(self, username, name, phone):
        self.username = username
        self.name = name
        self.phone = phone


def for_method():
    for i in range(5):
        print(i, end=' ')
    print()
    users = {'user1': User('1', '2', '3'), 'user2': User('4', '5', '6'), 'user2': User('7', '8', '9')}
    for k, v in users.items():
        print(str(k) + ' , user : [ ' + v.username + ' ' + v.name + ' ' + v.phone + ' ]')


def condition_method():
    user1 = User('1', '2', '3')
    user2 = user1
    user3 = User('1', '2', '3')
    print('user1 is user2 : ' + str(user1 is user2))
    print('user1 is user3 : ' + str(user1 is user3))
    print('user2 is user3 : ' + str(user2 is user3))
    a = 1
    b = 2
    c = True
    print('a < b == c : ' + str(a < b == c))
    print('(a < b) == c : ' + str((a < b) == c))
    print('not False is True : ' + str(not False is True))
    print('not False == True : ' + str(not False == True))
    d = not (e := True)
    print('d = not (e := True) => d = ' + str(d) + ' and e = ' + str(e))


def module_name_method():
    print('__name__ : ' + __name__)
    print('list.__name__ : ' + list.__name__)


if __name__ == '__main__':
    # list_method()
    # zip_method()
    # del_method()
    # sequences_method()
    # set_method()
    # dict_method()
    # for_method()
    # condition_method()
    module_name_method()
    pass
