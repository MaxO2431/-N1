import random


class Unit:
    def __init__(self, number, commandid):
        self.number = number
        self.commandId = commandid


class Hero(Unit):
    def __init__(self,  number, commandid, name, level=1):  #  добавляем свойства name и level
        Unit.__init__(self, number, commandid)
        self.name = name  # Привязка level
        self.level = level

    def getlevel(self):
        return self.level

    def inclevel(self):
        self.level += 1
        print('Уровень героя', self.name,'увеличен на 1 и равен', self.level)


class Soldier(Unit):
    def gotohero(self, Hero):
        print('Солдат номер', self.number, 'следует за героем', Hero.name, 'с номером', Hero.number)


H1 = Hero(1, 1, 'Red army')  # Создаем героев с номерами 1 и 2
H2 = Hero(2, 2, 'Blue army')
armyH1, armyH2 = [], []  # Списки солдат

for i in range(3, 10):  # Генерация нечетное количество солдат
    n = random.randint(0, 1)
    if n:
        armyH1.append(Soldier(i, 1))
        print('Солдат с номером', i, 'добавлен в армию', H1.name)
    else:
        armyH2.append(Soldier(i, 2))
        print('Солдат с номером', i, 'добавлен в армию', H2.name)

print('Армия героя', H1.name, ':', len(armyH1))
print('Армия героя', H2.name, ':', len(armyH2))

if len(armyH1) > len(armyH2):
    print('В армии', H1.name, 'больше солдат, увеличиваем его уровень')
    H1.inclevel()
else:
    print('В армии', H2.name, 'больше солдат, увеличиваем его уровень')
    H2.inclevel()

armyH1[1].gotohero(H2)