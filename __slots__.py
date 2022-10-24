"""
객체 내에 있는 변수들은 __dict__를 통해서 관리가 된다.
__slots__을 통해 변수를 관리 :
파이썬 인터프리터에게 통보 해당 클래스가 가지는 속성을 제한한다.
"""


class WithoutSlotClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


wos = WithoutSlotClass("jaekwanee", 12)

print(wos.__dict__)

wos.__dict__["hello"] = "world"
wos.code = 777

print(wos.__dict__)


class WithSlotClass:
    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        self.age = age


ws = WithSlotClass("jaekwanee", 15)

# print(ws.__dict__)
print(ws.__slots__)


# ------- 메모리 성능 비교 -------
import timeit


def repeat(obj):
    def inner():
        obj.name = "jaekwanee"
        obj.age = 22
        del obj.name
        del obj.age

    return inner


use_slot_time = timeit.repeat(repeat(ws), number=9999999)
no_slot_time = timeit.repeat(repeat(wos), number=9999999)

print(min(use_slot_time))
print(min(no_slot_time))
