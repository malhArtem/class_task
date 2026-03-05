

## Задание 1. Класс «Счёт в банке»
**Тема:** инкапсуляция, конструкторы, методы доступа.  
*(Без изменений — указателей здесь не было.)*

**Условие:**  
Создайте класс `BankAccount`, который представляет банковский счёт. Класс должен содержать:
- Приватные поля: номер счёта (строка), имя владельца (строка), баланс (вещественное число).
- Публичные методы:
  - Конструктор для инициализации всех полей.
  - Методы доступа (геттеры) для всех полей.
  - Метод `deposit(double amount)` для пополнения счёта.
  - Метод `withdraw(double amount)` для снятия денег (с проверкой).
  - Метод `display()` для вывода информации о счёте.

**Пример решения аналогичной задачи (класс «Книга»):**
```cpp
#include <iostream>
#include <string>

class Book {
private:
    std::string title;
    std::string author;
    int pages;
public:
    Book(const std::string& t, const std::string& a, int p) 
        : title(t), author(a), pages(p) {}

    std::string getTitle() const { return title; }
    std::string getAuthor() const { return author; }
    int getPages() const { return pages; }

    void setPages(int p) {
        if (p > 0) pages = p;
        else std::cout << "Ошибка: количество страниц должно быть положительным.\n";
    }

    void display() const {
        std::cout << "Книга: " << title << ", автор: " << author 
                  << ", страниц: " << pages << std::endl;
    }
};

int main() {
    Book book("Война и мир", "Лев Толстой", 1300);
    book.display();
    book.setPages(1225);
    std::cout << "Новое количество страниц: " << book.getPages() << std::endl;
    return 0;
}
```

---

## Задание 2. Наследование: «Транспортные средства»
**Тема:** базовый класс, производные классы, переопределение методов.  
*(Убраны виртуальные функции и указатели — объекты создаются на стеке, методы вызываются напрямую.)*

**Условие:**  
Создайте базовый класс `Vehicle` (транспортное средство) с полями: `speed` (скорость), `capacity` (вместимость). Определите метод `move()`, который выводит "Транспортное средство движется".  
Создайте два производных класса:  
- `Car` (легковой автомобиль) – добавляет поле `fuelType` (тип топлива). Переопределите метод `move()` для вывода "Автомобиль едет по дороге".  
- `Bicycle` (велосипед) – добавляет поле `hasBasket` (наличие корзины). Переопределите метод `move()` для вывода "Велосипед крутит педали".  

В главной функции создайте объекты каждого типа и вызовите их методы `move()`.

**Пример решения аналогичной задачи (классы «Животные» без виртуальных функций и указателей):**
```cpp
#include <iostream>
#include <string>

class Animal {
protected:
    std::string name;
    int age;
public:
    Animal(const std::string& n, int a) : name(n), age(a) {}
    void speak() const {
        std::cout << "Животное издаёт звук" << std::endl;
    }
};

class Dog : public Animal {
private:
    std::string breed;
public:
    Dog(const std::string& n, int a, const std::string& b) 
        : Animal(n, a), breed(b) {}
    void speak() const {
        std::cout << "Собака " << name << " лает: Гав-гав!" << std::endl;
    }
};

class Cat : public Animal {
private:
    bool isIndoor;
public:
    Cat(const std::string& n, int a, bool indoor) 
        : Animal(n, a), isIndoor(indoor) {}
    void speak() const {
        std::cout << "Кошка " << name << " мяукает: Мяу-мяу!" << std::endl;
    }
};

int main() {
    Dog dog("Бобик", 3, "Такса");
    Cat cat("Мурка", 2, true);
    dog.speak();   // вызов метода Dog
    cat.speak();   // вызов метода Cat
    return 0;
}
```

---

## Задание 3. Полиморфизм: «Геометрические фигуры» (упрощённый вариант без указателей)
**Тема:** абстрактный класс, чисто виртуальные функции, полиморфизм через ссылки.

**Условие:**  
Создайте абстрактный класс `Shape` (фигура) с чисто виртуальными методами `area()` и `perimeter()`.  
Реализуйте два класса-наследника:  
- `Rectangle` (прямоугольник) с полями `width` и `height`.  
- `Circle` (круг) с полем `radius`.  

В главной функции создайте объекты `Rectangle` и `Circle`. Затем напишите функцию `printInfo(const Shape& s)`, которая принимает фигуру по ссылке и выводит её площадь и периметр. Продемонстрируйте работу, передавая в эту функцию оба объекта.

**Пример решения аналогичной задачи (классы «Работники и зарплата» без указателей):**
```cpp
#include <iostream>

class Employee {
public:
    virtual double calculateSalary() const = 0;
    virtual ~Employee() {}
};

class HourlyEmployee : public Employee {
private:
    double hourlyRate;
    int hoursWorked;
public:
    HourlyEmployee(double rate, int hours) : hourlyRate(rate), hoursWorked(hours) {}
    double calculateSalary() const override {
        return hourlyRate * hoursWorked;
    }
};

class SalariedEmployee : public Employee {
private:
    double annualSalary;
public:
    SalariedEmployee(double salary) : annualSalary(salary) {}
    double calculateSalary() const override {
        return annualSalary / 12;
    }
};

void printSalary(const Employee& e) {
    std::cout << "Зарплата: " << e.calculateSalary() << std::endl;
}

int main() {
    HourlyEmployee hourly(20.0, 160);
    SalariedEmployee salaried(60000.0);
    printSalary(hourly);
    printSalary(salaried);
    return 0;
}
```

---

## Задание 4. Композиция: «Университет и студенты»
**Тема:** отношение между классами, хранение объектов по значению.

**Условие:**  
Создайте класс `Student` с полями: имя, номер студенческого билета.  
Создайте класс `Course` (курс), который содержит название курса и список студентов (вектор объектов `Student`).  
В классе `Course` реализуйте методы:
- `addStudent(const Student& s)` – добавить студента на курс (копия добавляется в вектор).
- `removeStudent(int studentId)` – удалить студента по номеру билета.
- `display()` – вывести всех студентов курса.

В главной функции создайте несколько студентов, добавьте их на курс и продемонстрируйте работу методов.

**Пример решения аналогичной задачи (классы «Автобус и пассажиры» без указателей):**
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

class Passenger {
private:
    std::string name;
    int ticketNumber;
public:
    Passenger(const std::string& n, int ticket) : name(n), ticketNumber(ticket) {}
    std::string getName() const { return name; }
    int getTicketNumber() const { return ticketNumber; }
};

class Bus {
private:
    std::string routeNumber;
    std::vector<Passenger> passengers; // композиция: пассажиры хранятся внутри
public:
    Bus(const std::string& route) : routeNumber(route) {}

    void addPassenger(const Passenger& p) {
        passengers.push_back(p);
    }

    void removePassenger(int ticketNumber) {
        auto it = std::remove_if(passengers.begin(), passengers.end(),
            [ticketNumber](const Passenger& p) { return p.getTicketNumber() == ticketNumber; });
        if (it != passengers.end()) {
            passengers.erase(it, passengers.end());
            std::cout << "Пассажир с билетом " << ticketNumber << " удалён.\n";
        } else {
            std::cout << "Пассажир не найден.\n";
        }
    }

    void display() const {
        std::cout << "Автобус маршрута " << routeNumber << ", пассажиры:\n";
        for (const auto& p : passengers) {
            std::cout << " - " << p.getName() << " (билет " << p.getTicketNumber() << ")\n";
        }
    }
};

int main() {
    Passenger p1("Иван", 101);
    Passenger p2("Мария", 102);
    Bus bus("15А");
    bus.addPassenger(p1);
    bus.addPassenger(p2);
    bus.display();
    bus.removePassenger(101);
    bus.display();
    return 0;
}
```

---

## Задание 5. Перегрузка операторов: «Вектор на плоскости»
**Тема:** перегрузка операторов, дружественные функции.  
*(Без изменений — указателей здесь не было.)*

**Условие:**  
Создайте класс `Vector2D` для представления вектора на плоскости с координатами `x` и `y`.  
Перегрузите следующие операторы:
- `+` (сложение двух векторов)
- `-` (вычитание)
- `*` (умножение на скаляр – как левое, так и правое)
- `==` (сравнение на равенство)
- `<<` (вывод в поток)

Продемонстрируйте работу всех операторов в главной функции.

**Пример решения аналогичной задачи (класс «Дробь» без указателей):**
```cpp
#include <iostream>

class Fraction {
private:
    int numerator;
    int denominator;
public:
    Fraction(int num = 0, int denom = 1) : numerator(num), denominator(denom) {
        if (denominator == 0) denominator = 1;
    }

    Fraction operator+(const Fraction& other) const {
        return Fraction(numerator * other.denominator + other.numerator * denominator,
                        denominator * other.denominator);
    }

    Fraction operator*(const Fraction& other) const {
        return Fraction(numerator * other.numerator, denominator * other.denominator);
    }

    bool operator==(const Fraction& other) const {
        return (numerator * other.denominator == other.numerator * denominator);
    }

    friend std::ostream& operator<<(std::ostream& os, const Fraction& f) {
        os << f.numerator << "/" << f.denominator;
        return os;
    }
};

int main() {
    Fraction f1(1, 2), f2(3, 4);
    Fraction sum = f1 + f2;
    Fraction product = f1 * f2;
    std::cout << f1 << " + " << f2 << " = " << sum << std::endl;
    std::cout << f1 << " * " << f2 << " = " << product << std::endl;
    std::cout << (f1 == f2 ? "равны" : "не равны") << std::endl;
    return 0;
}
```

---
