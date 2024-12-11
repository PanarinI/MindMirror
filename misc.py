class DivineCode:
    def __init__(self, word):
        self.word = word
        self.creator = "God"
        self.word_is_creator = True

    def create(self):
        if self.word_is_creator:
            print(f"{self.word} spoke, and the universe began.")

# В начале было слово
code = DivineCode("In the beginning was the Word")
code.create()





##############


class Divine:
    def __init__(self, word):
        self.word = word

    def speak(self):
        print(f"In the beginning, {self.word} spoke.")
        return Divine(self.word)  # Слово создает самого себя

# Начало
divine = Divine("God")
running = True  # Флаг выполнения

while running:
    divine = divine.speak()
    user_input = input("Введите 'stop', чтобы завершить: ")
    if user_input.lower() == 'stop':
        running = False

#########
class Divine:
    def __init__(self, message):
        self.message = message

    def speak(self):
        print(self.message)
        user_input = input("Введите 'exit', чтобы остановить: ")
        if user_input.lower() == 'exit':
            return None  # Сигнализируем о выходе из цикла
        return self  # Возвращаем объект для продолжения

divine = Divine("God")
while divine is not None:  # Условие для выхода из бесконечного цикла
    divine = divine.speak()



############
class Divine:
    def __init__(self, word):
        self.word = word

    def speak(self):
        print(f"In the beginning, {self.word} spoke.")
        return Divine(self.word)  # Слово создает самого себя

# Начало
divine = Divine("God")
while True:  # Бесконечное самовоспроизведение
    if input("Введите 'stop', чтобы завершить цикл, или нажмите Enter для продолжения: ").lower() == 'stop':
        print("Цикл завершен.")
        break  # Прерываем цикл
    divine = divine.speak()



###############

import time

class Divine:
    def __init__(self, word):
        self.word = word

    def speak(self):
        print(f"In the beginning, {self.word} spoke.")

divine = Divine("God")

while True:
    divine.speak()  # Вывод текста
    time.sleep(0.5)  # Небольшая задержка для читаемости
    user_input = input("Введите 'stop', чтобы завершить цикл: ")  # Проверка ввода
    if user_input.lower() == 'stop':
        print("Цикл завершен.")
        break


def divine_word(word="God", depth=0, max_depth=3):
    if depth >= max_depth:
        return f"In the beginning was the Word: '{word}', and it continues forever..."

    print(f"In the beginning was the Word: '{word}'")
    return divine_word(word=word, depth=depth + 1, max_depth=max_depth)


# Запуск
print(divine_word())
