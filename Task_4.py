  # Задача 4
# Создать класс на тему животных.
# Используйте статические и динамические переменные, дочерний (1 или более)
# классов на конкретное животное. Публичные  и приватные методы. Полиморфизм (одинаковые названия методов info
# в обоих классах, которые выводят информацию о животных, либо о конкретном животном данного класса).
# Создайте обьекты каждого класса и обратьитесь к каждому методу. Напищите один staticmethod, один classmethod
# и к которым также обратитесь.

#class Animals:
#     animals = "Hello!!!"
#     herb = "травоядные животные"
#     pred = "хищные животные"
#
#     def __int__(self, predator):
#         self.predator = predator
#         self.predators = self.pred
#         self.herbivores = self.herb
#
#     def prov(self):
#         if self.predators == self.predator:
#             print("Животное опасное. Не подходите!")
#         elif self.herbivores != self.predator:
#             print("Животное не опасно!")
#
#
#     def eat(self, feed, meat):
#         self._feed = feed
#         self._meat = meat
#         if self._meat == self.pred:
#             print("Животное хищник")
#         elif self._feed == self.herb:
#             print("Животное травоядное")
#
#     @staticmethod
#     def zoo():
#         print("Животные вам рады!")
#
#     @classmethod
#     def zoo_animals(cls):
#         print("В зоопарке есть хищные и травоядные животные")
#
#
# class Tiger(Animals):
#     def __int__(self,tip):
#          super().__int__(tip)
#
#
#     def info(self):
#          print("Данный класс животных - тигры")
#
# ani = Animals("Тигр")
# ani.zoo()
# ani.prov()
# ani.zoo_animals()
#
# tig = Tiger("Ваня")
# tig.info()