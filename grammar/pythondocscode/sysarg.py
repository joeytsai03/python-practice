import sys


# 2.1.1. 传入参数
# 解释器读取命令行参数，把脚本名与其他参数转化为字符串列表存到 sys 模块的 argv 变量里。执行 import sys，可以导入这个模块，并访问该列表。该列表最少有一个元素；未给定输入参数时，sys.argv[0] 是空字符串。给定脚本名是 '-' （标准输入）时，sys.argv[0] 是 '-'。使用 -c command 时，sys.argv[0] 是 '-c'。如果使用选项 -m module，sys.argv[0] 就是包含目录的模块全名。解释器不处理 -c command 或 -m module 之后的选项，而是直接留在 sys.argv 中由命令或模块来处理。
def print_argv():
    print(sys.argv)


def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print('a = ' + str(a))
        a, b = b, a + b


def fibonacci_main():
    fibonacci(5)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='迁移脚本参数解析')
    # parser.add_argument('--account-ids', dest='account_ids', nargs='+', type=int,
    #                     help='讲师id列表')
    # parser.add_argument('--all', dest='is_all', action='store_true',
    #                     help='全网更新')
    # parser.add_argument('--not-all', dest='is_all', action='store_false',
    #                     help='非全网更新')
    # args = parser.parse_args()
    # print(args.account_ids)
    # print(args.is_all)
    # print_argv()
    # fibonacci_main()
    func = fibonacci_main
    datas = []
    print(type(func))
    print(type(datas))
