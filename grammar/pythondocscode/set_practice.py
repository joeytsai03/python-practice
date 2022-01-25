def obj_set():
    datas1 = list()
    datas2 = list()
    datas1.append(Data('1', '2'))
    datas1.append(Data('1', '2'))
    datas2.append(Data('1', '2'))
    datas2.append(Data('3', '4'))
    print(datas1)
    print(datas2)
    datas1.remove()
    print(datas2 - datas1)

    # if len(datas3) == 0:
    #     print('datas is None!!')


def list_sub_each_count(minuend: list, subtrahend: list) -> dict:
    data_list = list_sub(minuend, subtrahend)
    return convert_each_count_dict(data_list)


def list_sub(minuend: list, subtrahend: list) -> list:
    result = minuend.copy()
    subtrahend_each_count_dict = convert_each_count_dict(subtrahend)
    for data in minuend:
        if subtrahend_each_count_dict.get(data) is None:
            continue
        subtrahend_each_count_dict[data] = subtrahend_each_count_dict[data] - 1
        result.remove(data)
        if subtrahend_each_count_dict[data] == 0:
            del subtrahend_each_count_dict[data]
    return result


def convert_each_count_dict(data_list: list) -> dict:
    data_count_dict = dict()
    for data in data_list:
        value = data_count_dict.get(data)
        if value is None:
            data_count_dict[data] = 1
        else:
            data_count_dict[data] = value + 1
    return data_count_dict


def list_sub_test():
    data_list1 = [Data(1, 1), Data(2, 2), Data(2, 2), Data(2, 2), Data(3, 3), Data(4, 4)]
    data_list2 = [Data(1, 1), Data(2, 2), Data(2, 2), Data(2, 2), Data(3, 3)]
    each_count_dict = list_sub_each_count(data_list1, data_list2)
    sub_data_list = list_sub(data_list1, data_list2)
    print(each_count_dict)
    print(sub_data_list)


def convert_each_count_dict_test():
    data_list = [Data(1, 1), Data(2, 2), Data(2, 2), Data(2, 2), Data(3, 3)]
    data_dict = convert_each_count_dict(data_list)
    print(data_dict)


def print_list(datas: list):
    for data in datas:
        print(data)
    print('--------------')


class Data:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return self.name + '-' + self.gender

    def __hash__(self):
        return hash(self.name + self.gender)

    def __eq__(self, other):
        return self.name == other.name and self.gender == other.gender


if __name__ == '__main__':
    # obj_set()
    # convert_each_count_dict_test()
    list_sub_test()
