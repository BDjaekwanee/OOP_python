# OOP_python
파이썬에서 객체지향 프로그래밍을 어떻게 구현하는지 공부하고 학습해봄. <br/> 
모든 공부 내용은 git log에 남겨서 commit messeage로 저장함.
<img width="753" alt="image" src="https://user-images.githubusercontent.com/95554757/197773580-2e10b04f-2a6e-42d2-bcd6-c31669f24af8.png">

commit 530060fd34cdb94d86e3715ec5db4b0724f6d658 (HEAD -> main, origin/main)
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Tue Oct 25 00:07:21 2022 +0900

    Add : python __slots__ magic mathod

      - 파이썬에서 모든 클래스 네임스페이스는 dic으로 관리됨. 클래스.__dict__ 찍어보면됨.
      - 심지어 클래스 밖에서도 네임스페이스 건드릴 수 있음. (setter로 유효성 검사 안한다면)
      - 근데 유효성 검사 한다는 거 자체도 일단은 접근 한다는건데 그럼 메모리 효율이 떨어지지 않을까?
      - 그래서 dict로 관리하지 않고 slots으로 관리하게 되면 메모리 효율 절약 가능
      - 근데 이렇게 짜는거는 리펙토링 과정에서는 메모리 효율이 필요할때 쓰는 것은 바람직 하지만 굳이?
      - 어쩌면 파이썬을 자바, c처럼 짜려고 하는게 오히려 모순이지 않을까?
      - 파이썬이 파이썬 다운 이유는 너무나도 아름다운(?) 유연성 때문이지 않을까? 생각함.

commit 05ff280c5c1be4227aaf342975b9a1782c1d9fb7
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Mon Oct 24 23:40:45 2022 +0900

    Add : python composition

      - 컴포지션은 상속과 다르게 단순히 사용한다는 개념이다.
      - 자식클래스가 부모클래스의 모든 속성을 물려 받는 것이 아니라, 자식 클래스가 필요한 속성만 부모에서 가져와 사용하는 것
      - 컴포지션은 명시적 선언, 상속은 암시적 선언
:...skipping...
commit 530060fd34cdb94d86e3715ec5db4b0724f6d658 (HEAD -> main, origin/main)
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Tue Oct 25 00:07:21 2022 +0900

    Add : python __slots__ magic mathod

      - 파이썬에서 모든 클래스 네임스페이스는 dic으로 관리됨. 클래스.__dict__ 찍어보면됨.
      - 심지어 클래스 밖에서도 네임스페이스 건드릴 수 있음. (setter로 유효성 검사 안한다면)
      - 근데 유효성 검사 한다는 거 자체도 일단은 접근 한다는건데 그럼 메모리 효율이 떨어지지 않을까?
      - 그래서 dict로 관리하지 않고 slots으로 관리하게 되면 메모리 효율 절약 가능
      - 근데 이렇게 짜는거는 리펙토링 과정에서는 메모리 효율이 필요할때 쓰는 것은 바람직 하지만 굳이?
      - 어쩌면 파이썬을 자바, c처럼 짜려고 하는게 오히려 모순이지 않을까?
      - 파이썬이 파이썬 다운 이유는 너무나도 아름다운(?) 유연성 때문이지 않을까? 생각함.

commit 05ff280c5c1be4227aaf342975b9a1782c1d9fb7
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Mon Oct 24 23:40:45 2022 +0900

    Add : python composition

      - 컴포지션은 상속과 다르게 단순히 사용한다는 개념이다.
      - 자식클래스가 부모클래스의 모든 속성을 물려 받는 것이 아니라, 자식 클래스가 필요한 속성만 부모에서 가져와 사용하는 것
      - 컴포지션은 명시적 선언, 상속은 암시적 선언
      - 오버라이딩을 무작정 하기 전에 컴포지션 고려해 볼 필요 있음.
:...skipping...
commit 530060fd34cdb94d86e3715ec5db4b0724f6d658 (HEAD -> main, origin/main)
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Tue Oct 25 00:07:21 2022 +0900

    Add : python __slots__ magic mathod

      - 파이썬에서 모든 클래스 네임스페이스는 dic으로 관리됨. 클래스.__dict__ 찍어보면됨.
      - 심지어 클래스 밖에서도 네임스페이스 건드릴 수 있음. (setter로 유효성 검사 안한다면)
      - 근데 유효성 검사 한다는 거 자체도 일단은 접근 한다는건데 그럼 메모리 효율이 떨어지지 않을까?
      - 그래서 dict로 관리하지 않고 slots으로 관리하게 되면 메모리 효율 절약 가능
      - 근데 이렇게 짜는거는 리펙토링 과정에서는 메모리 효율이 필요할때 쓰는 것은 바람직 하지만 굳이?
      - 어쩌면 파이썬을 자바, c처럼 짜려고 하는게 오히려 모순이지 않을까?
      - 파이썬이 파이썬 다운 이유는 너무나도 아름다운(?) 유연성 때문이지 않을까? 생각함.

commit 05ff280c5c1be4227aaf342975b9a1782c1d9fb7
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Mon Oct 24 23:40:45 2022 +0900

    Add : python composition

      - 컴포지션은 상속과 다르게 단순히 사용한다는 개념이다.
      - 자식클래스가 부모클래스의 모든 속성을 물려 받는 것이 아니라, 자식 클래스가 필요한 속성만 부모에서 가져와 사용하는 것
      - 컴포지션은 명시적 선언, 상속은 암시적 선언
      - 오버라이딩을 무작정 하기 전에 컴포지션 고려해 볼 필요 있음.

commit 65f62ec948cf0522d3d9d97d26d434e7b1eb439a
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Mon Oct 24 23:25:15 2022 +0900

    Add : python polymorphism

    다형성, 객체를 부품화 하기.

commit 868eb1e185315fbd3716b95cc293201680857672
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Sun Oct 23 16:17:21 2022 +0900

    Add : python encapsulation

    private 접근 제어자를 사용해도 접근이 실제로는 가능했다.
    이를 컨트롤 할 수 있는 것이 @proterty
    @proterty를 활용하여 외부에서 인스턴스 변수를 read 할 수 있고,
    @setter을 활용하여 외부에서 write 할 시 유효성 검사를 통과 해야지만 작성되게 할 수 있음.

commit 113258ffa16f65331931862ec28751e08f1bca42
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Sat Oct 22 16:08:28 2022 +0900

    Add : python private VS public

    파이썬도 typescript, java 처럼 private, public을 사용할 수 있지만 이 기능이 실제로 제한 되는 것이 아니라 제한되는 척(?
)처럼 보이게 만듬.
    실제로 다른사람과 같이 개발하거나 할때 접근제어자 명시를 파이썬 문법으로 해주어 다른 개발자에게 알려 줄 수 있지만, 강
제할 수는 없음.
    자주 사용하는 습관을 들이고, 명시해준 규칙대로 코드를 짜되, 파이썬은 실제로 제어가 되지 않는다는 것을 항상 인지해야 겠
음.

commit 79336dd588c2e9e4c828499c3c820032d5ab754f
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Sat Oct 22 10:59:17 2022 +0900

    Add : python inheritance practice5

    파이썬에서 모든것은 객체이다. -> object 클래스 상속받아서 쓰고 있는 것
      - int, str, boolean 이런 자료구조 타입도 결국 파이썬 클래스이며, object클래스 상속 받음.
      - 클래스.mro()를 확인하면 상속 확인 가능
    상속은 다중상속도 가능하다. -> 다형성
      - 하지만 다중상속은 의미없이 사용해 버린다면 안티 패턴인 경우가 많음.
      - 객체지향 원칙 중 단일책임 원칙(SRP)을 깨서 그런거 아닐까? 생각함.

commit 3ceb2c2dda29e6559768193e38065d216c958c00
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Mon Oct 3 20:50:56 2022 +0900

    Add : python inheritance practice4

    super()은 부모 클래스를 나타낸다.
    어차피 부모에게 다 상속을 받는데 super을 쓸 일이 있을까?
     - ex) __init__ 을 오버로딩 해야된다면? 그런데 부모 클래스의 인스턴스 변수가 너무 많다면?
     - super().__init__ 을 호출하고 그담에 필요한 것만 self.필요한거 = 필요한거 로 정의하면 된다.

commit 914b46ec1f39d0c83ae8a8418e5027e00f86dbbe
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Mon Oct 3 20:18:27 2022 +0900

    Add : python inheritance practice3

    부모에서 물려받은 함수를 같은 이름이지만, 새롭게 재정의 할 수 있음. 이를 오버라이딩이라고 함.

commit 3b3fc86470543e02147cff6b417e640bf91f67c8
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Sat Oct 1 10:33:12 2022 +0900

    Add : python inheritance practice2

    class에서 상속을 통해 상속받은 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.

commit 3dc8237a362b83ba46de6ab7ce1ad02224a240b0
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Tue Sep 27 17:37:20 2022 +0900

    Add : python inheritance practice

     - 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속됨.
     - 파이썬에서 상속은 이런식으로 사용함
        class부모(자식):
            pass

commit 408dcf4e33004f8bc2ef4b1028792aab86951c06
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Tue Sep 27 17:26:46 2022 +0900

    Add : python magic_method practice

    - 파이썬에서 기본으로 제공되는 magic_method를 오버라이딩 해보면서 어떠한 기능을 제공하는지 확인해봄.
    - 파이썬에서는 함수 또한 객체임. 호출(call)이 되는 이유는 callable 하기 때문. __call__을 오버라이딩 해보면 확인 가능.

commit fce295360838652dd59ce51f5f30c0417fae371b
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Tue Sep 27 14:40:44 2022 +0900

    Add : self & cls 이해

    self 자체는 인스턴스 그 자체임. 한마디로 self가 인스턴스 객체 하나라고 생각하면 되겠음.
    new 연산자가 없으니까 파라미터에 self 인스턴스 객체 그 자체를 넣어버리는거고 거기서 생성하는거임.
    이전에는 강의를 듣거나 설명을 들어도 이해가 되지 않았었는데, 어느정도 보이기 시작하는 시기가 있는거 같다.

commit 42363082851c9b436d39000ab39c04273e0be89c
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Tue Sep 27 12:52:42 2022 +0900

    Add : staticmethod 이해하기

    현재 class와, instance 의 self도 사용하지 않는 함수라면 staticmethod 사용

    Java 에서는 static 메서드를 class 메서드와 동일시 여겼지만, 파이썬은 아님.

commit 48a2bd2f08544a2ea564a34e96316a4cfaa17adf
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Mon Sep 26 23:11:24 2022 +0900

    Add : 파이썬 namespace의 이해

    파이썬은 메모리 효율을 위해서 instance method를 class name space에 만듬.

    그렇다고 class 에서 instance method 만들었다고 해서  Robot.sayhi(siri) 이런식으로 쓰면 안됨.

    siri.sayhi() 이게 정석임.

    파이썬 내부적으로 인스터스 네임스페이스에 없다면 class 네임스페이스에서 찾음.

    즉 파이썬은 네임스페이스 사용을 유연하게 지원하는 것을 알 수 있음.

    Python class를 심도있게 배워보니  사용자가 사용하기 쉽게 java 보다 뒤에서 처리하는 것이 훨씬 많다는 것을 알게 되었음.
    하지만 이렇게 처리해 주는 만큼 제대로 알지 못하거나, 원리를 이해하지 못한다면 객체지향적인 코드를 짜지 못하게 될 것이
라고 생각함.

commit e2d8aca1732f4da3beac2d821e92076de5aad975
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Sat Sep 17 11:05:47 2022 +0900

    Add : class 추상화 구현 샘플 코드

    추상화를 사용하는 샘플 코드를 구현해봄. 파이썬에서는 클래스 함수를 구현하기 위해 @classmethod 를 사용해야 된다는 것을
알게됨.

commit 136bd01656a5e03b028831a95d76b0d24b62d509
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Sat Sep 17 11:03:37 2022 +0900

    Add : 파이썬 class 구현 샘플 코드

    java 에서 강조하면서 배웠던 oop 개념이 파이썬에서는 어떻게 적용되는지 공부해보고자 샘플 코드를 작성함.
    문법은 다르지만, 생성자, 클래스변수, 인스턴스 변수등 하나의 맥락은 통일되어서 객체지향을 구현하고 있음.

commit dd441cbd022bc476b89e3a81cc65c4f30d038b86
Author: BDjaekwanee <jaekwanee@gmail.com>
Date:   Sat Sep 17 11:01:59 2022 +0900

    Add : 파이썬 데코레이터 기본 이해 샘플 코드

    데코레이터가 어떻게 작동되는지 풀어서 쓰기 위해 간단하게 샘플코드로 구현해봄.
