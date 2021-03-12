class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_police
    def go(self):
        print("Машина поехала")
    def stop(self):
        print("Машина остановилась")
    def turn(self):
        w = input("Для поворота нажмите '1' - направо, другую клавишу - налево ")
        if w == "1":
            print("Машина повернула направо")
        else: print("Машина повернула налево")
    def show_speed(self):
        print(f"Текущая скорость - {self.speed}км/ч")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышении скорости")
        else:
            print(f"Текущая скорость - {self.speed}км/ч")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышении скорости")
        else:
            print(f"Текущая скорость - {self.speed}км/ч")

class PoliceCar(Car):
    pass


my_car = WorkCar(60, "red", "zhuk", False)
# my_car.go()
# my_car.turn()
my_car.show_speed()
