"""
polymorphism
여러 형태를 가질 수 있도록 한다. 즉 객체를 부품화 할 수 있도록 한다.
같은 형태의 코드가 다른 동작을 하도록 하는 것.
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


class Siri(Robot):
    def say_apple(self):
        print("hello my apple")


class SiriKR(Robot):
    def say_apple(self):
        print("안녕하세요")


class Bixby(Robot):
    def say_samsung(self):
        print("안녕하세요")
