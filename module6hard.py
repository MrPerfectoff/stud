class Figure:
    def __init__(self, color=(0, 0, 0), *sides):
        self.__sides = []
        self.__color = list(color)
        self.filled = False
        self.sides_count = 0

        if sides:
            self.set_sides(*sides)
        else:
            raise ValueError("стороны должны быть определены")

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(n, int) and 0 <= n <= 255 for n in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) == 0:
            self.set_sides(1)

    def get_square(self):
        if self.get_sides():
            radius = self.get_sides()[0] / 2
            return 3.14159 * radius ** 2
        return 0


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) == 0:
            self.set_sides(1, 1, 1)

    def get_square(self):
        if len(self.get_sides()) == 3:
            a, b, c = self.get_sides()
            s = (a + b + c) / 2
            return (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return 0


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) == 0:
            self.set_sides(1)

    def set_sides(self, *sides):
        if len(sides) == 1:
            super().set_sides(*(sides[0],) * self.sides_count)
        else:
            print("Укажите только одну сторону для рёбер куба.")

    def get_volume(self):
        if self.get_sides():
            side_length = self.get_sides()[0]
            return side_length ** 3
        return 0


# Примеры использования:
circle1 = Circle((200, 200, 100), 10)  # (цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # Ожидается: [55, 66, 77]
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # Ожидается: [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # Ожидается: 15

# Проверка объёма (куба):
print(cube1.get_volume())  # Ожидается: 216