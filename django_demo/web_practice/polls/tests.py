from abc import ABC, ABCMeta
from typing import List


# Create your tests here.
class Tests:
    account_ids: List[int] = [12]
    is_all: bool


# print(Tests.account_ids)


class ABCTest(metaclass=ABCMeta):
    pass


# ABCTest()

if __name__ == '__main__':
    ABCTest()

#
# t = Tests()
# t.account_ids = [1111111111111111111111111111111111111111]
#
#
#
# print(t.account_ids)
