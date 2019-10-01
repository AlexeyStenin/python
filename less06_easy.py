# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
# Задача - 2 Посмотрите на задачу-1 подумайте как выделить общие признаки классов в родительский и остальные просто
# наследовать от него.

# Task1
# Parents Object (#Task2)


class Car:
    def __init__(self, name, velocity, color):
        self.velocity = velocity
        self.color = color
        self.name = name
        self.is_police = False
        self.go()

    def go(self):
        print('Car {} start movement!'.format(self.name))

    def stop(self):
        print('Car {} stopped!'.format(self.name))

    def turn(self, direction):
        print('Car {} to turn {}!'.format(self.name, direction))

    def speed(self):
        print('Car {} speed up on!'.format(self.name))


class TownCar(Car):
    def __init__(self, color):
        self.velocity = 60
        self.color = color
        self.name = 'Tesla'
        super().__init__(self.name, self.velocity, self.color)


class SportCar(Car):
    def __init__(self, color):
        self.velocity = 200
        self.color = color
        self.name = 'Lambo'
        super().__init__(self.name, self.velocity, self.color)


class WorkCar(Car):
    def __init__(self, color):
        self.velocity = 30
        self.color = color
        self.name = 'Bobcat'
        super().__init__(self.name, self.velocity, self.color)


class PoliceCar(Car):
    def __init__(self, color):
        self.velocity = 150
        self.color = color
        self.name = 'Ford'
        super().__init__(self.name, self.velocity, self.color)
        self.is_police = True


print('inheritance: ')

town_car = TownCar('White')
sport_car = SportCar('OrangeRed')
work_car = WorkCar('Yellow')
police_car = PoliceCar('Black')

print('--------------------------------------------------')
print('CarClass|', 'CarColor|', 'CarVelocity|', 'is_Police?')
print('--------------------------------------------------')
print(town_car.name, town_car.color, town_car.velocity, town_car.is_police)
print(sport_car.name, sport_car.color, sport_car.velocity, sport_car.is_police)
print(work_car.name, work_car.color, work_car.velocity, work_car.is_police)
print(police_car.name, police_car.color, police_car.velocity, police_car.is_police)

town_car.go()
town_car.speed()
town_car.turn('to the left')
town_car.stop()
