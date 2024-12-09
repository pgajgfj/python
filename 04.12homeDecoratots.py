#1
import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Час виконання: {elapsed_time:.2f} секунд")
        return result
    return wrapper


@timing_decorator
def generate_even_numbers():
    return [num for num in range(100001) if num % 2 == 0]

even_numbers = generate_even_numbers()
print("Парні числа:", even_numbers)

#2
def fix_negative_decorator(func):
    def wrapper(*args, **kwargs):
        fixed_args = tuple(max(1, arg) if isinstance(arg, (int, float)) and arg < 0 else arg for arg in args)
        fixed_kwargs = {key: (max(1, value) if isinstance(value, (int, float)) and value < 0 else value) for key, value in kwargs.items()}
        return func(*fixed_args, **fixed_kwargs)
    return wrapper

@fix_negative_decorator
def example_function(*args, **kwargs):
    print("Аргументи:", args)
    print("Іменовані аргументи:", kwargs)

example_function(10, -3, "red", -1, 200, named_arg=-5, another_arg=0)

