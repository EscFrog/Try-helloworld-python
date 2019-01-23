class Human():
    '''인간'''

def create_human(name, weight): # 이 함수는 현재 클래스 밖에 있음.
    person = Human()
    person.name = name
    person.weight = weight
    return person

Human.create = create_human # 클래스 밖에 있는 암수를 클래스에 create란 이름으로 포함시킴
person = Human.create("철수", 60.5)
