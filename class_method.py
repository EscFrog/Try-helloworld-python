class Human():
    '''인간'''

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        '''문자열화 메서드. 인스턴스를 문자열로 변환해야 할 때 어떻게 표현할지 결정'''
        return "{}(몸무게 {}kg)".format(self.name, self.weight)

    def eat(self):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다.".format(person.name, person.weight))

    def walk(self):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다.".format(person.name, person.weight))



# 클래스 외부에서 클래스를 호출하는 부분
person = Human("사람", 60.5)
print(person)
print(person.name)
print(person.weight)