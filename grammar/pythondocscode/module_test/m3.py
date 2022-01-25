from enum import Enum


class ValueDescEnumData:

    def __init__(self, data, desc):
        self.data = data
        self.desc = desc


class OrderTaskStatusEnum(Enum):
    normal = ValueDescEnumData("nomal", "正常")
    deleted = ValueDescEnumData("deleted", "删除")
    draft = ValueDescEnumData("draft", "下架")
    notstarted = ValueDescEnumData("notstarted", "用于筛选，未开始")
    underway = ValueDescEnumData("underway", "用于筛选，进行中")
    finished = ValueDescEnumData("finished", "用于筛选，已结束")


# OrderTaskStatusEnum.value = 5
print(OrderTaskStatusEnum.normal)
