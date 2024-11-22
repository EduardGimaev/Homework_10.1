from functools import wraps
from typing import Callable, Any, Optional
from time import time


# def log(filename="mylog.txt") -> Callable:
def log(filename: Optional[str] = None) -> Callable:
    """Декоратор логирования начала и конца выполнения функции, а также ее результата или возникновения ошибки"""

    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as error:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {error.__class__.__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {error.__class__.__name__}. Inputs: {args}, {kwargs}")

        return wrapper

    return decorator


def printing(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func} started")
        result = func(*args, **kwargs)
        print(f"Function {func} finished")

        return result

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        time_1 = time()
        result = func(*args, **kwargs)
        time_2 = time()
        print(f"Time from work: {time_2 - time_1}")

        return result

    return wrapper
