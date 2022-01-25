"""-"""
import inspect
import json
import logging
import time
from functools import wraps
from typing import List

from pydantic import BaseModel


class DefaultJSONEncoder(json.JSONEncoder):
    """-"""

    def default(self, o):
        """-"""
        if isinstance(o, object):
            return o.__dict__


class LogDecorator(object):
    """-"""

    @classmethod
    def log_info(cls, func, result, *args, **kwargs):
        """-"""
        try:
            func_args = None
            if len(args) != 0 and len(kwargs) != 0:
                func_args = [*args, *[{key: value} for key, value in kwargs.items()]]
            elif len(args) != 0:
                func_args = args
            elif len(kwargs) != 0:
                func_args = [{key: value} for key, value in kwargs.items()]
            print(
                f"func: {func} , args: {json.dumps(func_args, cls=DefaultJSONEncoder)} , "
                f"result: {json.dumps(result, cls=DefaultJSONEncoder)}")
        except Exception as log_ex:
            print(
                f"[ERROR]wk_order_task.decorator.log_decorator.LogDecorator.log_info exception : {log_ex}")

    @classmethod
    def log_exception(cls, func, ex, *args, **kwargs):
        """-"""
        try:
            print(
                f"func: {func} , args: "
                f"{json.dumps([*args, *[{key: value} for key, value in kwargs.items()]], cls=DefaultJSONEncoder)} , "
                f"exception: {ex}")
        except Exception as log_ex:
            print(
                f"[ERROR]wk_order_task.decorator.log_decorator.LogDecorator.log_exception exception : {log_ex}")

    @classmethod
    def async_log(cls, func):
        """-"""

        @wraps(func)
        async def after(first, *args, **kwargs):
            """-"""
            try:
                start_time = time.time()
                result = await func(first, *args, **kwargs)
                end_time = time.time()
                cls.log_info(func, result, *args, **kwargs)
            except Exception as ex:
                cls.log_exception(func, ex, *args, **kwargs)
                raise ex
            return result

        return after


class BBBB:
    async def ptst(cls, *args, **kwargs):
        print("ptst")
        return "ptst"


class RemoteRequest:
    client = BBBB()

    @classmethod
    def post(cls, *, url):
        def method(func):
            @wraps(func)
            async def invoke(first, *, data, **kwargs):
                func_default_params = cls.__get_func_default_params(func)
                return_type = cls.__get_func_return_type(func)
                func_default_params.update(kwargs)
                func_default_params['data'] = data
                await func(first, **func_default_params)
                result = await cls.client.ptst()
                if return_type is not None:
                    print(return_type)
                return result

            return invoke

        return method

    @classmethod
    def __get_func_default_params(cls, func):
        signature = inspect.signature(func)
        default_params = {
            k: v.default
            for k, v in signature.parameters.items()
            if v.default is not inspect.Parameter.empty
        }
        return default_params

    @classmethod
    def __get_func_return_type(cls, func):
        signature = inspect.signature(func)
        return_type = signature.return_annotation
        if return_type is inspect.Parameter.empty:
            return None
        elif not issubclass(return_type, BaseModel):
            logging.exception(f'return_type {type(return_type)} is not valid')
        return return_type
