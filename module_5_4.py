class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        house_name = super(House, cls).__new__(cls)
        cls.houses_history.append(args[0])
        return house_name

    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.floors:
            print('Такого этажа не существует')
        else:
            for floor in range (1, new_floor + 1):
                print(floor)
    def __len__(self):
        return self.floors
    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.floors}'
    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        return False
    def __lt__(self, other):
        return self.floors < other.floors
    def __le__(self, other):
        return self.floors <= other.floors
    def __gt__(self, other):
        return self.floors > other.floors
    def __ge__(self, other):
        return self.floors >= other.floors
    def __ne__(self, other):
        return self.floors != other.floors
    def __add__(self, value):
        if isinstance(value, int):
            self.floors += value
        return self
    def __radd__(self, other):
        return self.__add__(False)
    def __iadd__(self, other):
        return self.__add__(False)
    def __del__(self):
        print(f'{self.name} сненсен, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)


del h2
del h3

print(House.houses_history)