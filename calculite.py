import re
'''
Простейшая реализация калькулятора, получаем первое число, получаем действие,
получаем второе число выдаем результат
'''
NUM_RE = r'^\d+[.]?\d*$'
EXP_RE = r'^[+*\/%^]$'
ESC_STR = ['q', 'quit', 'exit']

def get_value(message: str, regex: str) -> str:
    """
    Функция для вычитывания и валидации данных, введенных 
    пользователем
        Arguments:
            message (str) - Приглашение для ввода
            regex (str) - Регулярное выражение для проверки ввода
        Return:
            str - валидные данные от пользователя
    """
    while True:
        data = input(message)
        # Если введена escape-последовательность, то прекращаем работу
        if data.lower() in ESC_STR:
            quit(0)

        if re.findall(regex, data):
            return data
        else:
            print(f"Invalide value {data}")


def calculate(first: float, second: float, expression: str) -> float:
    """
    Функция для совершения математического действия с двумя числами на основе
    переданного выражения.
        Arguments:
            first (float) - Первое число выражения
            second (float) - Второе число выражения
            expression (str) - Выражение
        Return:
            (float) - Результат выражения
    """
    match expression:
        case '+':
            return first + second
        case '*':
            return first * second
        case '/':
            return first / second
        case '%':
            return first % second
        case '^':
            return first ** second
        case _:
            return 0

def run() -> None:
    """
    Основная функция, которая запускает калькулятор
    """
    while True:
        first_num = float(get_value("Input first number:", NUM_RE))
        expression = get_value("Input expression:", EXP_RE)
        second_num = float(get_value("Input second number:", NUM_RE))
        try:
            print(calculate(first_num, second_num, expression))
        except ZeroDivisionError:
            print("Error division by zero")


if __name__ == "__main__":
    run()