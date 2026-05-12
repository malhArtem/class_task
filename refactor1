## Задание для рефакторинга (начинающие Python)

### Что такое рефакторинг?
Рефакторинг — это улучшение внутренней структуры кода без изменения его внешнего поведения. Цели: сделать код читаемым, модульным, легко поддерживаемым и расширяемым. Для начинающих важно научиться:
- Давать осмысленные имена переменным и функциям.
- Разбивать длинный код на небольшие функции.
- Устранять дублирование.
- Добавлять аннотации типов и документацию.
- Обрабатывать возможные ошибки.


---

## Задание 1 (с решением, пример)

**Исходный «плохой» код**  
Программа запрашивает у пользователя несколько чисел, затем выводит их сумму, среднее арифметическое, максимум и минимум.

```python
# Плохой код
nums = []
while True:
    x = input("Введи число или 'стоп' чтобы закончить: ")
    if x == "стоп":
        break
    nums.append(float(x))

s = 0
for n in nums:
    s = s + n
print("Сумма:", s)

if len(nums) > 0:
    avg = s / len(nums)
else:
    avg = 0
print("Среднее:", avg)

if len(nums) > 0:
    m = nums[0]
    for n in nums:
        if n > m:
            m = n
    print("Максимум:", m)
else:
    print("Нет чисел для максимума")

if len(nums) > 0:
    m = nums[0]
    for n in nums:
        if n < m:
            m = n
    print("Минимум:", m)
else:
    print("Нет чисел для минимума")
```

**Что нужно улучшить**  
- Дублирование проверки `len(nums) > 0` и циклов.  
- Переменные с однобуквенными именами (`s`, `n`, `m`).  
- Отсутствие функций — весь код в глобальной области.  
- Нет обработки ошибок при вводе нечисловых данных.  
- Логика вычислений смешана с вводом/выводом.

**Решение (отрефакторенный код)**  

```python
from typing import List

def get_numbers_from_user() -> List[float]:
    """
    Запрашивает у пользователя числа до тех пор, пока он не введёт 'стоп'.
    Возвращает список вещественных чисел.
    """
    numbers = []
    while True:
        user_input = input("Введите число (или 'стоп' для завершения): ")
        if user_input.lower() == "стоп":
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Ошибка: введите число или слово 'стоп'.")
    return numbers

def calculate_sum(numbers: List[float]) -> float:
    """Возвращает сумму чисел списка."""
    return sum(numbers)

def calculate_average(numbers: List[float]) -> float:
    """Возвращает среднее арифметическое. Для пустого списка возвращает 0.0."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def calculate_maximum(numbers: List[float]) -> float:
    """Возвращает максимальное значение. Для пустого списка возвращает 0.0."""
    if not numbers:
        return 0.0
    return max(numbers)

def calculate_minimum(numbers: List[float]) -> float:
    """Возвращает минимальное значение. Для пустого списка возвращает 0.0."""
    if not numbers:
        return 0.0
    return min(numbers)

def display_results(numbers: List[float]) -> None:
    """Выводит статистику по списку чисел."""
    if not numbers:
        print("Нет введённых чисел.")
        return

    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = calculate_maximum(numbers)
    minimum = calculate_minimum(numbers)

    print(f"Сумма: {total}")
    print(f"Среднее: {average}")
    print(f"Максимум: {maximum}")
    print(f"Минимум: {minimum}")

def main() -> None:
    numbers = get_numbers_from_user()
    display_results(numbers)

if __name__ == "__main__":
    main()
```

**Что изменилось?**  
- Появились функции с понятными названиями и `docstring`.  
- Устранены циклы вручную (использованы встроенные `sum`, `max`, `min`).  
- Добавлена обработка нечислового ввода (`try/except`).  
- Добавлены аннотации типов.  
- Логика разделена на ввод, вычисления и вывод.  
- Пустой список не вызывает ошибок.  

---

## Задание 2 

**Исходный код**  
Программа для управления списком задач (todo list). Позволяет добавлять, удалять, показывать задачи и сохранять их в файл.

```python
# todo_v1.py
import os

tasks = []
f = "tasks.txt"

if os.path.exists(f):
    with open(f, "r") as file:
        for line in file:
            tasks.append(line.strip())

while True:
    print("\n1 - Добавить задачу")
    print("2 - Удалить задачу")
    print("3 - Показать задачи")
    print("4 - Выйти")
    c = input("Выберите действие: ")

    if c == "1":
        t = input("Введите задачу: ")
        tasks.append(t)
        print("Задача добавлена.")
    elif c == "2":
        if len(tasks) == 0:
            print("Нет задач для удаления.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
            try:
                n = int(input("Номер задачи для удаления: "))
                if 1 <= n <= len(tasks):
                    tasks.pop(n-1)
                    print("Удалено.")
                else:
                    print("Неверный номер.")
            except:
                print("Некорректный ввод.")
    elif c == "3":
        if len(tasks) == 0:
            print("Список пуст.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
    elif c == "4":
        with open(f, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print("До свидания!")
        break
    else:
        print("Неизвестная команда.")
```

**Недостатки для рефакторинга**  
- Весь код в одном бесконечном цикле, нет функций.  
- Магические строки ("1", "2", "3", "4").  
- Неинформативные имена переменных (`c`, `t`, `f`, `n`).  
- Дублирование кода для отображения списка задач.  
- Нет обработки ошибок при чтении/записи файла (например, если нет прав).  
- Ввод номера для удаления не защищён от нечислового ввода (используется голый `except`).  
- Логика сохранения в файл вызывается только при выходе — но если программа аварийно завершится, изменения потеряются.  
- Отсутствуют аннотации типов и документация.

**Задание**  
 Проведите рефакторинг этого кода.  

*Результат должен работать точно так же, как исходная программа, но быть чище и надёжнее.*
