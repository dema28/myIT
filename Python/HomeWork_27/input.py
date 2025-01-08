class Input:
    @staticmethod
    def get_numbers():
        try:
            key1 = float(input("Введите первое число: "))
            key2 = float(input("Введите второе число: "))
            return key1, key2
        except ValueError:
            print("Необходимо ввести число.")
            return None, None
