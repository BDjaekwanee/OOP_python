"""
namespace : 개체를 구분할 수  있는 범위
__dict__ : 네임스페이스를 확인할 수 있다.
dir() : 네임스페이스의 key 값을 확인할 수 있다.
__doc__ : class의 주석을 확인한다.
__class__ : 어떤 클래스로 만들어진 인스턴스인지를 확인할 수 있다.
"""


class Robot:
    """
    [Robot Class]
    Author : 송재관
    Role : ex) 이거 로봇 만든거임.
    """

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

print(Robot.__dict__)

print(siri.__dict__)  # {'name': 'siri', 'code': 20214213535}
print(jarvis.__dict__)  # {'name': 'jarvis', 'code': 3222321424}

siri.cal_add(
    2, 3
)  # ?? namespace 확인했는데 없었는데 어찌 찾은거지?? : 파이썬 내부적으로 인스터스 네임스페이스에 없다면 class 네임스페이스에서 찾음.

Robot.say_hi()  # TypeError: Robot.say_hi() missing 1 required positional argument: 'self'
Robot.say_hi(siri)

siri.say_hi()

print(dir(siri))

print(dir(Robot))

print(Robot.__doc__)

print(siri.__class__)
