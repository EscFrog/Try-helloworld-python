class Human():
    '''인간'''

def create_human(name, weight): # 이 함수는 현재 클래스 밖에 있음.
    person = Human()
    person.name = name
    person.weight = weight
    return person

Human.create = create_human # 클래스 밖에 있는 함수를 클래스에 create란 이름으로 포함시킴
person = Human.create("철수", 60.5)

# 먹는 함수
def eat(person):
    person.weight += 0.1
    print("{}가 먹어서 {}kg이 되었습니다.".format(person.name, person.weight))

# 걷는 함수
def walk(person):
    person.weight -= 0.1
    print("{}가 걸어서 {}kg이 되었습니다.".format(person.name, person.weight))

# human 클래스에 넣기
Human.eat = eat
Human.walk = walk

#실제 사람 (person)에 적용하기
person.walk()
person.eat()
person.walk()
