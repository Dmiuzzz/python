class Stationery:
    title = 'Пишушие'
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")

class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашем")

class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")

pen = Pencil()
pen.draw()