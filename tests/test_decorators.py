from src.decorators import log, printing, timer


@log()
def my_function(x, y):
    """Функция сложения"""
    return x + y


def test_log_console_ok(capsys):
    """Функция тестирует вывод в консоль при правильно заданных параметрах"""
    my_function(1, 4)
    output = capsys.readouterr()
    assert output.out == "my_function ok\n"


def test_log_console_error(capsys):
    """Функция тестирует вывод в консоль при не правильно заданных параметрах"""
    my_function(1, "4")
    output = capsys.readouterr()
    assert output.out == "my_function error: TypeError. Inputs: (1, '4'), {}\n"


@timer
@printing
def test_timer():
    """Функция тестирует декоратор таймера и логирование начала и конца выполнения функции"""
    my_function(1, 4)
    assert timer == timer
