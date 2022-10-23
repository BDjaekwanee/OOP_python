"""
[property]
인스턴스 변수 값을 사용하여 적절한 값으로  보내고 싶을 때 사용함.
인스턴스 변수 값에 대한 유효성 검사 및 수정 가능
"""


class Robot:
    """
    [Robot Class]
    Author : 송재관
    Role : ex) 이거 로봇 만든거임.
    """

    __population = 0

    def __init__(self, name, age, code):
        self.__name = name
        self.__age = age
        self.__code = code
        Robot.__population += 1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise TypeError("invalid range to age")
        self.__age = new_age

    def say_hi(self):
        print(f"Greetings, my masters call me {self.__name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.__population} robots."


droid = Robot("JK", 8, 214351)

droid.age = 77

droid.age = -999  # 유효성 검사 통과 못함.
