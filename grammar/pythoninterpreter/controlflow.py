from random import random

# 流程控制
def if_method():
    x = int( random.random() * 10)
    print(x)
    if x < 3:
        print('x < 3')
    elif x >= 3 and x < 6:
        print('x >= 3 and x < 6')
    elif x >= 6:
        print('x >= 6')

def for_method():
    words = ['one' , 'two' , 'three']
    for word in words:
        print(word + ' ')
    for i in range(len(words)):
        print(words[i] + ' ')

def for_index_method():
    words = ['one' , 'two' , 'three']
    for i in range(len(words)):
        print(words[i] + ' ')


class User():
    name = ''
    phone = ''
    def __init__(self, name , phone):
        self.name = name
        self.phone = phone

def for_copy_method():
    users = [User(name = '1',phone = '1-1') , User('2','2-2') , User('3','3-3')]
    users_copy = users.copy()
    for user in users:
        print(user.name + ' ' + user.phone)
    print('-------------------------------------')
    for user in users_copy:
        print(user.name + ' ' + user.phone)
    print('-------------------------------------')
    users_copy.clear()
    for user in users:
        print(user.name + ' ' + user.phone)
    print('-------------------------------------')
    for user in users_copy:
        print(user.name + ' ' + user.phone)
    print('-------------------------------------')

def range_method():
    for i in range(2,5):
        print('i  = ' + str(i) + '  ' , end = '')
    print()
    for i in range(5):
        print('i  = ' + str(i) + '  ' , end = '')
    print()
    for i in range(20 , 100 , 10):
        print('i  = ' + str(i) + '  ' , end = '')

def sum_method():
    print(sum(range(4)))

def loop_break_control_method():
    print('------------break-----------------')
    for n in range(2,5):
        for i in range(2,n):
            print('i = ' + str(i), end=' ')
            if n % i == 0:
                break
        else:
            print('[else] n = ' + str(n), end=' ')
        print()
    print('------------continue-----------------')
    for n in range(2,5):
        for i in range(2,n):
            print('i = ' + str(i), end=' ')
            if n % i == 0:
                continue
        else:
            print('[else] n = ' + str(n), end=' ')
        print()

def loop_control_method():
    for i in range(8):
        if i == 3:
            break
        print('i = ' + str(i) , end = ' ')
    print()
    for i in range(8):
        if i == 3:
            continue
        print('i = ' + str(i) , end = ' ')

def pass_method():
    pass

class passclass():
    pass

def loop_pass_method():
    while(False):
        pass

def doc_method():
    """
    Do nothong!
    :return:
    """
    pass

def func_method():
    print('func_method')

def func_object_method():
    func = func_method
    func()

def func_return_method():
    func = func_method
    print('print return None func_method : ', end = '')
    print(func_method())
    print('print return None func : ', end = '')
    print(func())

def print_param_define_method(first , second = '2' , third = '3'):
    print(first , end = ' ')
    print(second , end = ' ')
    print(third , end = ' ')
    print()
    print('-----------------end----------------')

def print_param_method():
    try:
        print_param_define_method()
    except Exception as ex:
        print(ex)
        print('-----------------end----------------')
    print_param_define_method('one')
    print_param_define_method('one','two')
    print_param_define_method('one','two','three')

def print_list_param_define_method(list = []):
    list.append(len(list))
    print(list)

def print_list_param_method():
    print_list_param_define_method();
    print_list_param_define_method();
    print_list_param_define_method();
    print_list_param_define_method();

def tuple_keyword_param(nomalParam , *tupleParam , **dictParam):
    print(nomalParam , end = ' ')
    print(tupleParam , end = ' ')
    print(dictParam , end = ' ')
    print()

def tuple_keyword_param_method():
    number = (2)
    tuple = (2,)
    print(number)
    print(tuple)
    tuple_keyword_param(1)
    tuple_keyword_param(2,'tuple1','tuple2')
    tuple_keyword_param(3, 'tuple1' , key1 = 'value1',key2 = 'value2')
    tuple_keyword_param(3,  key1 = 'value1',key2 = 'value2')

def special_param_method(pos1, pos2,  /, pos_or_kwd, *, kwd1, kwd2, **dict):
    print('pos1 = ' + str(pos1) , end=' ')
    print('pos2 = ' + str(pos2) , end=' ')
    print('pos_or_kwd = ' + str(pos_or_kwd) , end=' ')
    print('kwd1 = ' + str(kwd1) , end=' ')
    print('kwd2 = ' + str(kwd2) , end=' ')
    print('dict = ' + str(dict) , end=' ')
    print('-' * 30)


def special_param_invoke_method():
    try:
        special_param_method()
    except Exception as ex:
        print('special_param_method() ex : ' + str(ex))
        print('-' * 30)
    ########################################################
    try:
        special_param_method( 1 , 2 , 3 )
    except Exception as ex:
        print('special_param_method( 1 , 2 , 3 ) ex : ' + str(ex))
        print('-' * 30)
    ########################################################
    special_param_method(1,2,3,kwd1=4,kwd2=5)
    ########################################################
    special_param_method(1,2,pos_or_kwd=3,kwd1=4,kwd2=5)
    ########################################################
    try:
        special_param_method(1, pos2 = 2, pos_or_kwd=3, kwd1=4, kwd2=5)
    except Exception as ex:
        print('special_param_method(1, pos2 = 2, pos_or_kwd=3, kwd1=4, kwd2=5) ex : ' + str(ex))
        print('-' * 30)


if __name__ == '__main__':
    # if_method()
    # for_method()
    # for_copy_method()
    # range_method()
    # sum_method()
    # loop_control_method()
    # loop_break_control_method()
    # func_object_method()
    # func_return_method()
    # print_param_method()
    # print_list_param_method()
    # tuple_keyword_param_method()
    special_param_invoke_method()
