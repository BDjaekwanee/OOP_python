"""
[클래스 상속]

1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.
2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.
3. 메서드 오버라이딩
4. Super( )
5. Python의 모든 클래스는 object 클래스를 상속한다. : 모든 것은 객체이다.
6, mro( ) : 상속 관계를 보여준다.
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

    @staticmethod
    def this_is_root_class():
        print("yes!!")

    def __str__(self):
        # 기존 python magic-method overriding
        return f"{self.name} robot!!"

    def __call__(self):
        # 함수가 아닌 객체를 callable 하게 overriding
        print("call")
        return f"{self.name} call!!"


class Siri(Robot):
    def call_me(self):
        print("네?")

    def call_mul(self, a, b):
        return a * b

    @classmethod
    def hello_apple(cls):
        print(f"{cls}")


siri = Siri("iphone14", 1213541)

siri.call_me()

print(siri.call_mul(7, 8))

Siri.hello_apple() #<class '__main__.Siri'>