"""
[self의 이해]
self는 인스턴스 객체이다.
클래스 안에 있는 self의 주소와 만들어진 인스턴스의 주소는 같다. 즉 self는 인스턴스 그 자체이다.
"""

from re import X


class SelfTest:

    # 클래스 변수
    name = "jaekwan"

    def __init__(self, x):
        self.x = x

    # 클래스 메서드
    @classmethod
    def func1(cls):
        print(f"cls: {cls}")
        print("func1")

    # 인스턴스 메서드
    def func2(self):
        print(f"self : {self}")
        print("class안의 Self 주소 : ", id(self))
        print("func2")


test_obj = SelfTest(17)

test_obj.func2()
print("인스턴스의 주소: ", id(test_obj))
print("--------------------------------")
SelfTest.func1()
print("++++++")

"""
[출력결과]
class안의 Self 주소 :  140603802664000
func2
인스턴스의 주소:  140603802664000
---------------------------------
cls: <class '__main__.SelfTest'>
func1
"""

test_obj.func1()
print(test_obj.name)

"""
[출력결과]
cls: <class '__main__.SelfTest'>
func1
아니 왜? 이게 되지??
 - 파이썬 내부에서 동적으로 해결해 준다. 
 - 인스턴스를 통해서 해당하는 클래스 메서드, 변수를 호출 시킬 수 있으며, 의미론적으로 때로는 이러한 호출이 필요할 수도 있음.
 - 이렇기 때문에 파이썬은 유연하다고 함.
 - java로 객체지향을 class를 배웠는데 먼저 배우길 잘 한거 같음. 파이썬이 얼마나 유연한 언어인지 알게 되었음.
"""
