#Задание 1

class Kassa:
    def __init__(self):
        self.balance = 0

    def top_up(self, amount):
        self.balance += amount

    def count_1000(self):
        return self.balance // 1000

    def take_away(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостаточно денег в кассе")

kassa = Kassa()

kassa.top_up(1000000)

print(kassa.count_1000())

kassa.take_away(50000)

print(kassa.balance)

# #Задание 2

# class Turtle:
#     def __init__(self, x=0, y=0, s=1):
#         self._pos = [x, y]
#         self.s = s

#     def get_position(self):
#         return tuple(self._pos)

#     def go_up(self):
#         self._pos[1] += self.s

#     def go_down(self):
#         self._pos[1] -= self.s

#     def go_left(self):
#         self._pos[0] -= self.s

#     def go_right(self):
#         self._pos[0] += self.s

#     def evolve(self):
#         self.s += 1

#     def degrade(self):
#         if self.s <= 1:
#             print("Невозможно уменьшить s")
#         else:
#             self.s -= 1

#     def count_moves(self, x2, y2):
#         x1, y1 = self._pos
#         delta_x = abs(x2 - x1)
#         delta_y = abs(y2 - y1)
#         moves = (delta_x + delta_y) // self.s
#         return moves

# cherepashka = Turtle()

# cherepashka.go_up()
# cherepashka.go_right()
# cherepashka.evolve()
# print(cherepashka.get_position(), cherepashka.s)

# cherepashka.degrade()
# print(cherepashka.s)

# cherepashka.count_moves(9, 7)
# print(cherepashka.count_moves(9, 7))