"""
추상화 : abstraction
불필요한 정보는 숨기고 중요한(필요한) 정보만을 표현함으로서
공통의 속성 값이나 행위(methods)를 하나로 묶어 이름을 붙이는 것이다.
"""


class Robot:
    # 클래스 변수
    population = 0

    # 클래스 함수
    @classmethod
    def how_many(cls):
        print(f"We have {cls.population} robots.")

    # 생성자 함수 : 인스턴스 생성될때 초기화 함수(new랑 같은거 같음 java)
    def __init__(self, name, code):
        self.name = name  # 인스턴스 변수
        self.code = code  # 인스턴스 변수
        Robot.population += 1

    # 인스턴스 메서드
    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}")

    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b

    def die(self):
        print("파괴되었습니다.")


print(Robot.population)

siri = Robot("siri", 20214213535)
jarvis = Robot("jarvis", 3222321424)
bixby = Robot("bixby", 12324421412)

print(Robot.population)

Robot.how_many()
