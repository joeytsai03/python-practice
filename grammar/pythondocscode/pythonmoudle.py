import sys

import moduledemo
# from  moduledemo import data
def module_name_method():
    print('__name__ : ' + __name__)
    print('list.__name__ : ' + list.__name__)

def print_data():
    print('data = ' + data)

# print('in module')
def print_sys_path():
    print(sys.path)

def try_method():
    try:
        raise Exception('custom ex')
    except Exception as ex:
        print('Exception' + str(ex))
    else:
        print('try_method try ... else ...')

if __name__ == '__main__':
    # module_name_method()
    # print_data()
    # print_sys_path()
    try_method()
    pass
