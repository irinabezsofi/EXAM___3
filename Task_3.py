  # Задача 3
#Класс Company:
# 1. Создайте класс Company
# 2.Создайте статическое свойство levels, которое будет содержать (как словарь) все уровни квалификации программиста:
# 1:junior, 2:middle, 3:senior, 4:lead.
# 3.Создайте метод __init__(), внутри которого будут определены два динамических protected свойства:
# 1) _index - передается параметром и
# 2) _levels - принимает из словаря levels значение с ключом _index
# 4.Создайте метод _level_up(), который будет переводить программиста на следующий уровень
# 5. Создайте метод is_lead(), который будет проверять, что программист достиг последней квалификации
# Класс Programmer:
# 1. Создайте класс Programmer
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1) name - передается параметром, является публичным и
# 2) _level – уровень квалификации на основе словаря из Company
# 3. Создайте метод work(), который заставляет программиста работать,
# что позволяет ему становиться более квалифицированным с помощью метода _level_up()
# 4. Создайте статический метод knowledge_base(), который выведет в консоль справку по программированию.

# Тесты:
# 1.Вызовите справку по программированию
# 2.Создайте объекты классов Company, Programmer
# 3.Используя объект класса Programmer, повысьте свой уровень квалификации
# 4.Дойдите до уровня lead


# class Company:
#     levels = {
#               1: "junior",
#               2: "middle",
#               3: "senior",
#               4: "lead"
#               }
#
#     def __init__(self, index):
#         if index > 4:
#             index = 4
#         self._index = index
#         self._levels = self.levels[self._index]
#
#
#     def level_up(self):
#         if self._index != 4:
#             self._index += 1
#             self._levels = self.levels[self._index]
#         print("Уровень повышен до:" , self._levels)
#
#     def is_lead(self):
#         if self._index == 4:
#             print("Програмист достиг высшей квалификации")
#         else:
#             print("Ваш уровень слишком мал!")
#         return self._index == 4
#
# class Programmer(Company):
#
#     def __init__(self, name, uroven):
#         super().__init__(uroven)
#         self.name = name
#
#     def work(self):
#         self.level_up()
#
#
#     @staticmethod
#     def knowledge_base():
#         print(Company.levels)
#
# irina = Programmer("Irina", 1)
# irina.knowledge_base()
# while irina.is_lead() == False:
#     irina.level_up()
# irina.is_lead()
