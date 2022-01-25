import contextlib
from datetime import datetime
from typing import Optional

from pydantic.main import BaseModel


@contextlib.contextmanager
def f():
    try:
        yield
    finally:
        print("222222")


def k():
    with f():
        print(33333333)
        raise Exception('444444444')


class A(BaseModel):
    t: Optional[datetime] = None


a = A(t=datetime.now())
a = '{"t":1643005367.277232}'
a = A.parse_raw(a)
print(a.json())
