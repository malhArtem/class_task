## Задание 1: Система геометрических фигур

**Цель:** Создать иерархию геометрических фигур с вычислением площади и периметра.

**Требования:**
- Абстрактный класс `Shape` с методами `area()` и `perimeter()`
- Классы `Circle`, `Rectangle`, `Triangle` наследуются от `Shape`
- Инкапсуляция атрибутов фигур
- Магические методы: `__str__`, `__eq__`

**Атрибуты классов:**
- `Shape`: `_color`
- `Circle`: `_radius`
- `Rectangle`: `_width`, `_height`
- `Triangle`: `_side_a`, `_side_b`, `_side_c`

**Пример использования:**
```python
circle = Circle("красный", 5.0)
rectangle = Rectangle("синий", 4.0, 6.0)

print(circle)  # Круг: радиус=5.0, цвет=красный
print(f"Площадь: {circle.area():.2f}")  # 78.54
print(f"Периметр: {circle.perimeter():.2f}")  # 31.42
```

---

## Задание 2: Система сотрудников компании

**Цель:** Создать систему учета сотрудников с различными типами работников.

**Требования:**
- Абстрактный класс `Employee` с методом `calculate_salary()`
- Классы `FullTimeEmployee`, `PartTimeEmployee`, `Manager`
- Инкапсуляция данных о зарплате
- Магические методы: `__str__`, `__add__` для бонусов

**Атрибуты классов:**
- `Employee`: `_name`, `_employee_id`, `_salary`
- `FullTimeEmployee`: `_position`, `_vacation_days`
- `PartTimeEmployee`: `_hours_per_week`, `_hourly_rate`
- `Manager`: `_department`, `_bonus`

**Пример использования:**
```python
manager = Manager("Иван Иванов", "M001", 80000, "IT", 10000)
part_time = PartTimeEmployee("Петр Петров", "P001", 20, 500)

print(manager)  # Менеджер: Иван Иванов, отдел: IT
print(f"Зарплата: {manager.calculate_salary()}")  # 90000
print(f"Зарплата с доп. бонусом: {manager + 5000}")  # 95000
```

---

## Задание 3: Библиотечная система

**Цель:** Создать систему учета библиотечных материалов.

**Требования:**
- Абстрактный класс `LibraryItem` с методами `check_out()`, `check_in()`
- Классы `Book`, `Magazine`, `AudioBook`
- Инкапсуляция статуса выдачи
- Магические методы: `__str__`, `__len__`

**Атрибуты классов:**
- `LibraryItem`: `_title`, `_item_id`, `_is_checked_out`
- `Book`: `_author`, `_pages`, `_isbn`
- `Magazine`: `_issue_number`, `_publication_date`
- `AudioBook`: `_narrator`, `_duration_minutes`

**Пример использования:**
```python
book = Book("Преступление и наказание", "B001", "Достоевский", 671, "123-456")
magazine = Magazine("Наука и жизнь", "M001", 42, "2024-01")

print(book)  # Книга: Преступление и наказание, автор: Достоевский
print(f"Количество страниц: {len(book)}")  # 671
book.check_out()
print(f"Статус: {book._is_checked_out}")  # True
```

---

## Задание 4: Транспортные средства

**Цель:** Создать иерархию транспортных средств с различными характеристиками.

**Требования:**
- Абстрактный класс `Vehicle` с методами `start_engine()`, `stop_engine()`
- Классы `Car`, `Motorcycle`, `Truck`
- Инкапсуляция данных о двигателе
- Магические методы: `__str__`, `__eq__`

**Атрибуты классов:**
- `Vehicle`: `_brand`, `_model`, `_year`, `_speed`
- `Car`: `_fuel_type`, `_doors`, `_is_engine_on`
- `Motorcycle`: `_engine_cc`, `_has_passenger_seat`
- `Truck`: `_cargo_capacity`, `_axles`

**Пример использования:**
```python
car1 = Car("Toyota", "Camry", 2022, "бензин", 4)
car2 = Car("Toyota", "Camry", 2023, "бензин", 4)

print(car1)  # Автомобиль: Toyota Camry 2022
car1.start_engine()  # Двигатель запущен
print(car1 == car2)  # False (разные года)
```

---

## Задание 5: Банковские счета

**Цель:** Создать систему банковских счетов с различными типами.

**Требования:**
- Абстрактный класс `BankAccount` с методами `deposit()`, `withdraw()`
- Классы `SavingsAccount`, `CheckingAccount`, `CreditAccount`
- Инкапсуляция баланса
- Магические методы: `__str__`, `__add__`

**Атрибуты классов:**
- `BankAccount`: `_account_number`, `_account_holder`, `_balance`
- `SavingsAccount`: `_interest_rate`, `_min_balance`
- `CheckingAccount`: `_overdraft_limit`, `_transaction_fee`
- `CreditAccount`: `_credit_limit`, `_interest_rate`

**Пример использования:**
```python
savings = SavingsAccount("ACC001", "Иван Иванов", 10000, 0.05, 1000)
savings.deposit(5000)
print(savings)  # Сберегательный счет: ACC001, баланс: 15000
print(f"Проценты: {savings.calculate_interest()}")  # 750.0
```

---

## Задание 6: Система учета животных

**Цель:** Создать иерархию животных с различными поведениями.

**Требования:**
- Абстрактный класс `Animal` с методами `make_sound()`, `move()`
- Классы `Mammal`, `Bird`, `Reptile`
- Инкапсуляция состояния здоровья
- Магические методы: `__str__`, `__eq__`

**Атрибуты классов:**
- `Animal`: `_name`, `_species`, `_age`, `_is_hungry`
- `Mammal`: `_fur_color`, `_is_pregnant`
- `Bird`: `_wingspan`, `_can_fly`
- `Reptile`: `_scale_type`, `_is_venomous`

**Пример использования:**
```python
lion = Mammal("Симба", "Лев", 5, "золотистый", False)
eagle = Bird("Орлик", "Орел", 3, 2.0, True)

print(lion)  # Млекопитающее: Симба (Лев), 5 лет
lion.make_sound()  # Рррр!
print(lion == eagle)  # False
```

---

## Задание 7: Электронные устройства

**Цель:** Создать иерархию электронных устройств.

**Требования:**
- Абстрактный класс `ElectronicDevice` с методами `turn_on()`, `turn_off()`
- Классы `Smartphone`, `Laptop`, `Tablet`
- Инкапсуляция данных о батарее
- Магические методы: `__str__`, `__repr__`

**Атрибуты классов:**
- `ElectronicDevice`: `_brand`, `_model`, `_battery_level`
- `Smartphone`: `_screen_size`, `_storage_gb`
- `Laptop`: `_ram_gb`, `_processor`
- `Tablet`: `_has_cellular`, `_stylus_support`

**Пример использования:**
```python
phone = Smartphone("Apple", "iPhone 15", 85, 6.1, 128)
laptop = Laptop("Dell", "XPS 13", 90, 16, "Intel i7")

print(phone)  # Смартфон: Apple iPhone 15
print(repr(laptop))  # Laptop('Dell', 'XPS 13', 90, 16, 'Intel i7')
phone.turn_on()  # Смартфон включен
```

---

## Задание 8: Система заказов

**Цель:** Создать систему управления заказами в интернет-магазине.

**Требования:**
- Абстрактный класс `Order` с методами `calculate_total()`, `get_status()`
- Классы `ProductOrder`, `ServiceOrder`, `SubscriptionOrder`
- Инкапсуляция данных о клиенте
- Магические методы: `__str__`, `__add__`

**Атрибуты классов:**
- `Order`: `_order_id`, `_customer_name`, `_total_amount`
- `ProductOrder`: `_product_name`, `_quantity`, `_weight_kg`
- `ServiceOrder`: `_service_type`, `_duration_hours`
- `SubscriptionOrder`: `_subscription_type`, `_months`

**Пример использования:**
```python
product_order = ProductOrder("ORD001", "Иван", "Ноутбук", 1, 2.5)
service_order = ServiceOrder("ORD002", "Петр", "Ремонт", 2)

print(product_order)  # Заказ товара: ORD001, Ноутбук x1
print(f"Итог: {product_order.calculate_total()}")  # 50000
```

---

## Задание 9: Образовательная система

**Цель:** Создать систему учета студентов и преподавателей.

**Требования:**
- Абстрактный класс `Person` с методами `get_info()`, `get_contacts()`
- Классы `Student`, `Teacher`, `Course`
- Инкапсуляция академических данных
- Магические методы: `__str__`, `__contains__`

**Атрибуты классов:**
- `Person`: `_first_name`, `_last_name`, `_email`
- `Student`: `_student_id`, `_gpa`, `_courses`
- `Teacher`: `_employee_id`, `_department`, `_subjects`
- `Course`: `_course_code`, `_course_name`, `_credits`

**Пример использования:**
```python
student = Student("Иван", "Петров", "ivan@mail.ru", "S001", 4.5, ["Математика"])
teacher = Teacher("Петр", "Сидоров", "petr@mail.ru", "T001", "Информатика")

print(student)  # Студент: Иван Петров, GPA: 4.5
print("Математика" in student)  # True
```

---

## Задание 10: Игровые персонажи

**Цель:** Создать систему игровых персонажей с различными классами.

**Требования:**
- Абстрактный класс `GameCharacter` с методами `attack()`, `defend()`
- Классы `Warrior`, `Mage`, `Archer`
- Инкапсуляция характеристик
- Магические методы: `__str__`, `__add__`

**Атрибуты классов:**
- `GameCharacter`: `_name`, `_level`, `_health`
- `Warrior`: `_strength`, `_armor`
- `Mage`: `_mana`, `_spell_power`
- `Archer`: `_agility`, `_range`

**Пример использования:**
```python
warrior = Warrior("Боромир", 10, 100, 15, 20)
mage = Mage("Гэндальф", 15, 80, 100, 25)

print(warrior)  # Воин: Боромир, уровень: 10, здоровье: 100
warrior.attack()  # Атака мечом!
print(warrior + mage)  # Объединенная сила: 215
```

Каждое задание должно быть реализовано с соблюдением всех принципов ООП: наследование, инкапсуляция, полиморфизм и использование абстрактных классов.
