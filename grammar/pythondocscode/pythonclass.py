scope_param = 0


def scope_inner_method():
    scope_param = 1

    def scope_inner_nonlocal_method():
        nonlocal scope_param
        scope_param = 2

        def scope_inner_inner_nonlocal_method():
            nonlocal scope_param
            scope_param = 3

        scope_inner_inner_nonlocal_method()
        print('scope_inner_inner_nonlocal_method : ' + str(scope_param))

    def scope_inner_gobal_method():
        global scope_param
        scope_param = 4

    scope_inner_nonlocal_method()
    print('scope_inner_nonlocal_method : ' + str(scope_param))
    scope_inner_gobal_method()
    print('scope_inner_gobal_method : ' + str(scope_param))


def scope_gobal_method():
    global scope_param
    scope_param = 5


def scope_method():
    scope_inner_method()
    print('scope_inner_method : ' + str(scope_param))
    scope_gobal_method()
    print('scope_gobal_method : ' + str(scope_param))


class MyClass():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def func(self):
        print('self.x : ' + str(self.x) + ' self.y : ' + str(self.y))
        print('func(self)')


def invoke_my_class():
    my_class = MyClass('1', '2')
    print('MyClass(1,2) => x : ' + my_class.x + ' y : ' + my_class.y)


def invoke_my_class_func():
    func_tmp = MyClass.func
    func_tmp(MyClass(1, 2))
    my_class = MyClass(3, 4)
    my_class.func()
    MyClass.func(my_class)
    print(my_class.__class__)


def reload_method():
    print('reload_method')


def reload_method(i):
    print('reload_method , i = ' + str(i))


if __name__ == '__main__':
    # scope_method()
    # invoke_my_class()
    # invoke_my_class_func()
    # reload_method()
    # reload_method(1)
    pass
