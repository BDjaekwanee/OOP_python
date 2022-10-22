"""
* public vs private
java 나 typescrite 는 protect까지 지원 하는데 파이썬은 public, private를 지원한다.
"""


class Robot:
    """
    [Robot Class]
    Author : 송재관
    Role : ex) 이거 로봇 만든거임.
    """

    population = 0

    def __init__(self, name, age, code):
        self.name = name
        self.__age = age  # private 완벽한 private 아님. 변수명을 바꿔서 없는것 처럼 해버리는 거임.
        self._code = code  # protected [실제로는 구현 안됨. portected 면 외부에서 접근 불가능 해야 하는데 파이썬은 외부에서도 접근가능 죽 압묵적인 명시]
        Robot.population += 1

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."


jk = Robot("jaekwan", 8, 4564654)
