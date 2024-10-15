import threading
import time

# Функция для вычисления квадратов чисел
def calculate_square(number):
    print(f"Calculating square of {number}")
    time.sleep(1)  # Имитация задержки в вычислениях
    square = number * number
    print(f"The square of {number} is {square}")

# Функция для создания и запуска потоков
def create_threads(numbers):
    threads = []
    for number in numbers:
        thread = threading.Thread(target=calculate_square, args=(number,))
        threads.append(thread)
        thread.start()  # Запускаем поток

    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()

# Главная часть программы
numbers_to_calculate = [1, 2, 3, 4, 5]  # Числа для вычисления квадратов
create_threads(numbers_to_calculate)