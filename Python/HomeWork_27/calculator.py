class Calculator:

    def __init__(self, key1, key2):
        self.key1 = key1
        self.key2 = key2

    def add(self):
        return self.key1 + self.key2

    def subtract(self):
        return self.key1 - self.key2

    def multiply(self):
        return self.key1 * self.key2

    def divide(self):
        if self.key2 != 0:
            return self.key1 / self.key2
        else:
            return "Ошибка!!! Деление на ноль!!!"

