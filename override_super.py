class Animal():
    '''동물'''
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('걷는다')
    
    def eat(self):
        print('먹는다')

    def greet(self):
        print('{}이/가 인사한다'.format(self.name))

class Human(Animal):
    '''인간'''
    def __init__(self, name, hand):
        super().__init__(name)
        self.hand = hand

    def wave(self):
        print('{}을 흔들면서'.format(self.hand))
    
    def greet(self):
        self.wave()
        super().greet()

person = Human("월터", "오른손")
person.greet()
