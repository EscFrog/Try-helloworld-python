class Car():

    def __init__(self, name):
        self.name = name

    def run(self):
        print("차가 달립니다.")

class Truck(Car):

    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity
    
    def load(self):
        print("{}톤 트럭인 {}에 짐을 실었습니다.".format(self.capacity, self.name))


truck = Truck("포터", 1)
truck.load()



