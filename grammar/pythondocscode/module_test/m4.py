import datetime
import json
from typing import List, Optional

from pydantic import BaseModel

a = []
a.extend([1, 2, 3, 4, [6]])
print(a)


class DMLParamList(List):
    def check_and_append(self, flag, data):
        if flag:
            self.append(data)
        return flag


class DtoJSONEncoder(json.JSONEncoder):
    """-"""

    def default(self, o):
        """-"""
        if isinstance(o, datetime.datetime):
            return o.timestamp()
        elif isinstance(o, object):
            return o.__dict__
        else:
            return json.JSONEncoder.default(self, o)


# s = None
# ls = [2]
# l = DMLParamList()
# l.check_and_append(len(ls) == 2, 's')
# print(l)


class GetTaskListPageWithRelationQueryData(BaseModel):
    order_task_id: Optional[int] = None
    order_task_publisher_id: Optional[int] = None
    order_task_title: Optional[List] = None
    order_task_scene: Optional[str] = None
    order_task_top: Optional[int] = None
    order_task_state: Optional[str] = None
    order_task_apply_limit: Optional[int] = None
    order_task_approved_limit: Optional[int] = None
    order_task_begin_time: Optional[float] = None
    order_task_end_time: Optional[float] = None
    order_task_create_time: Optional[float] = None
    order_task_update_time: Optional[float] = None
    order_task_json_extend: Optional[dict] = None
    order_task_reward_reward_type: Optional[str] = None
    order_task_reward_reward_unit: Optional[str] = None
    order_task_reward_reward_paid: Optional[int] = None
    order_task_reward_work_num: Optional[int] = None
    order_task_reward_reward_min: Optional[int] = None
    order_task_reward_reward_max: Optional[int] = None
    order_task_reward_deposit: Optional[int] = None
    order_task_reward_reward_json: Optional[dict] = None
    order_task_reward_state: Optional[str] = None
    order_task_reward_json_extend: Optional[dict] = None


# aaa_dict = {'order_task_id': 1, 'order_task_title': '12', 'order_task_begin_time': 11111111111,
#             'order_task_reward_reward_json': {'a': 'b', 'c': {'d': 'f'}, 'g': ['d', 'f']}}
# aaa_json = json.dumps(aaa_dict,cls=DtoJSONEncoder)
# aaa = json.loads(aaa_json)
# a = GetTaskListPageWithRelationQueryData(**aaa)
# print(a.order_task_id)
