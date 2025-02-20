class Shape:
    def area(self):
        pass


# 接口
# TODO abc抽象类
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


shapes = [Circle(5), Square(10)]
for shape in shapes:
    print(shape.area())
