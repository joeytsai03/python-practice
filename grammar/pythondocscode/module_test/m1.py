import abc
import asyncio
from functools import wraps
from typing import Optional, Any, List, Dict

from grammar.pythondocscode.module_test.m2 import LogDecorator, RemoteRequest
from grammar.pythondocscode.module_test.m4 import GetTaskListPageWithRelationQueryData


class AAAA(metaclass=abc.ABCMeta):
    def __init__(self):
        self.b = 1
        self.bb = 1
        self.bbb = 1
        self.bbbb = 1
        pass

    @LogDecorator.async_log
    def pt(self):
        print("pt")

    @LogDecorator.async_log
    def ptargs(self, *args, **kwargs):
        print("ptargs")
        return self

    @classmethod
    @RemoteRequest.post(url='1111')
    async def ptstaticargs1(cls, data, y=5, *, params=1, b=6) -> GetTaskListPageWithRelationQueryData:
        ...

    @classmethod
    @LogDecorator.async_log
    # @RemoteRequest.post(url="111111")
    async def ptstaticargs(cls, *args, **kwargs):
        print("ptstaticargs")
        return args


class Pet():
    def __init__(self):
        self.a = 1
        self.pet1 = Pet1('1', '2')


class Pet1():
    l = 111

    def __init__(self, a, b):
        self.a = a
        self.b = b


w = str('2')


# AAAA().pt()
# pet = Pet()
# aaaa = AAAA()
# aaaa.ptargs(Pet(), 1, 2, 3, a=1, b=2, c=3)
# print(dict(Pet()))


#

class StrEnumData(str):
    def __new__(cls, data: Optional[Any], desc: Optional[str]):
        return str.__new__(cls, data)

    def __init__(self, data: Optional[Any], desc: Optional[str]):
        self.data = data
        self.desc = desc


# s = StrEnumData('1', '2')
# print(s)
# print(s.data)
# print(s.desc)

# class Inch(float):
#     "Convert from inch to meter"
#     def __new__(cls, arg=0.0):
#         return float.__new__(cls, arg*0.0254)
#
# print(Inch(12))


async def main():
    await AAAA.ptstaticargs1(data=2)


asyncio.run(main())

