from HomeWork_27.calculator import Calculator
from HomeWork_27.input import Input
from HomeWork_27.output import Output


def run() -> None:
    key1, key2 = Input.get_numbers()
    if key1 is not None and key2 is not None:
        calculators = Calculator(key1, key2)
        results = {
            "sum": calculators.add(),
            "difference": calculators.subtract(),
            "product": calculators.multiply(),
            "quotient": calculators.divide(),
        }
        Output.display_results(results)
    else:
        print("Ошибка ввода!")


class Main1:
    pass

if __name__ == "__main__":
    app = Main1()
    run()

