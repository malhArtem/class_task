# ООП в C++: вспоминаем основы

**Цель:** вспомнить, что такое класс, объект, поля и методы.

---

## 📖 Мини-теория (прочитай перед заданиями)

**Класс** — это шаблон (чертёж), по которому создаются объекты.
**Объект** — это конкретная «вещь», сделанная по этому шаблону.

Пример:
- **Класс** `Собака` — описывает, что у любой собаки есть кличка и возраст, и что она умеет лаять.
- **Объект** `Шарик` — конкретная собака с кличкой «Шарик» и возрастом 3.

**Структура класса:**
```cpp
class Dog {
public:              // отсюда всё доступно снаружи
    string name;     // поле (данные)
    int age;         // поле

    void bark() {    // метод (действие)
        cout << name << " говорит: Гав!" << endl;
    }
};
```

**Как пользоваться:**
```cpp
int main() {
    Dog d;              // создали объект
    d.name = "Шарик";   // задали поле
    d.age = 3;
    d.bark();           // вызвали метод
    return 0;
}
```

**Три главных слова:**
| Слово | Что значит |
|-------|-----------|
| `class` | объявить новый тип (шаблон) |
| `public:` | «это можно трогать снаружи» |
| `.` (точка) | доступ к полю или методу объекта |

---

## Часть 1. «Что выведет программа?»

**1.1**
```cpp
class Cat {
public:
    string name;
    void meow() {
        cout << name << " мяукает" << endl;
    }
};

int main() {
    Cat c;
    c.name = "Мурка";
    c.meow();
    return 0;
}
```

**1.2**
```cpp
class Point {
public:
    int x;
    int y;
};

int main() {
    Point p;
    p.x = 3;
    p.y = 4;
    cout << p.x + p.y;
    return 0;
}
```

**1.3**
```cpp
class Counter {
public:
    int value = 0;
    void inc() {
        value++;
    }
};

int main() {
    Counter c;
    c.inc();
    c.inc();
    c.inc();
    cout << c.value;
    return 0;
}
```

---

## Часть 2. «Найди ошибку»

**2.1**
```cpp
class Dog {
    string name;
public:
    void bark() {
        cout << name;
    }
};

int main() {
    Dog d;
    d.name = "Шарик";
    d.bark();
    return 0;
}
```

**2.2**
```cpp
class Cat {
public:
    string name;
    void meow() {
        cout << name;
    }
}

int main() {
    Cat c;
    c.meow();
    return 0;
}
```

**2.3**
```cpp
class Point {
public:
    int x;
    int y;
};

int main() {
    Point p;
    p.x = 3;
    cout << p.x + p.y;
    return 0;
}
```

---

## Часть 3. «Заполни пропуски»

**3.1**
```cpp
___ Book {
___:
    string title;
    int pages;

    void info() {
        cout << title << ", " << pages << " стр." << endl;
    }
};

int main() {
    Book b;
    b.___ = "Война и мир";
    b.pages = 1300;
    b.___();
    return 0;
}
```

**3.2**
```cpp
class Circle {
public:
    double radius;

    double area() {
        return 3.14 * ___ * ___;
    }
};

int main() {
    Circle c;
    c.radius = 5;
    cout << c.___();
    return 0;
}
```

---

## Часть 4. «Напиши класс сам»

**4.1. Класс `Student`**
Поля: `string name`, `int age`.
Метод: `void sayHi()`, который выводит приветствие с именем и возрастом.

В `main()` создай объект, заполни поля и вызови метод.

---

**4.2. Класс `Rectangle`**
Поля: `double width`, `double height`.
Методы:
- `double area()` — площадь.
- `double perimeter()` — периметр.

В `main()` создай прямоугольник, задай стороны и выведи площадь и периметр.

---

**4.3. Класс `Counter`**
Поле: `int value` (начальное значение 0).
Методы:
- `void inc()` — увеличивает на 1.
- `void dec()` — уменьшает на 1.
- `void reset()` — сбрасывает в 0.

В `main()` создай счётчик, вызови несколько методов и покажи результат.

---

**4.4. Класс `BankAccount`**
Поля: `string owner`, `double balance`.
Методы:
- `void deposit(double amount)` — пополнить счёт.
- `void withdraw(double amount)` — снять деньги (если хватает).
- `void show()` — вывести имя владельца и баланс.

В `main()` создай счёт, положи 1000, сними 300, покажи баланс.

---

**4.5. Класс `Dog`**
Поля: `string name`, `int age`.
Метод `void birthday()` — увеличивает возраст на 1 и выводит поздравление с новым возрастом.

Создай собаку и «отпразднуй» три дня рождения подряд.

---

## Часть 5. «Собери класс из кусочков»

Строки перепутаны. Расставь в правильном порядке.

```cpp
};
    }
        cout << "Гав!";
    void bark() {
class Dog {
public:
    string name;
```

---

## Часть 6. Работа в парах

Один студент **придумывает класс** (например, `Телефон`, `Книга`, `Кот`, `Игрок`) и описывает:
- какие у него поля,
- какие методы.

Второй — **пишет класс** по этому описанию и создаёт объект.

Потом меняетесь ролями.

---
---

# ООП в C++: задания среднего уровня

**Тема:** классы, конструкторы, инкапсуляция, работа объектов друг с другом.

---

## 📖 Мини-теория

**Инкапсуляция** — поля класса скрыты (`private`), а доступ к ним идёт через методы (`public`). Это защищает данные от случайной порчи.

```cpp
class Wallet {
private:              // ← снаружи не видно
    double balance;
public:               // ← снаружи доступно
    void add(double x) { balance += x; }
    double get() { return balance; }
};
```

**Конструктор** — специальный метод, который вызывается автоматически при создании объекта. Имя совпадает с именем класса, тип возврата не пишется.

```cpp
class Point {
    int x, y;
public:
    Point(int x, int y) {   // конструктор
        this->x = x;        // this-> различает поле и параметр с тем же именем
        this->y = y;
    }
};
```

**Список инициализации** — короткая запись того же самого:
```cpp
Point(int x, int y) : x(x), y(y) {}   // работает так же
```

**Деструктор** — метод, вызываемый при удалении объекта. Пишется с `~`:
```cpp
~Box() { cout << "Объект удалён"; }
```

**Копия объекта:** когда пишешь `Counter b = a;`, создаётся **отдельная копия** — изменения в `b` не влияют на `a`.

**Передача по ссылке `&`** — если метод должен изменить **другой** объект, его принимают по ссылке:
```cpp
void attack(Player &enemy) { enemy.hp -= damage; }
```

**`this`** — указатель на текущий объект. Нужен, когда имя параметра совпадает с именем поля.

---

## Часть 1. «Что выведет программа?»

**1.1**
```cpp
class Counter {
    int value;
public:
    Counter(int start) {
        value = start;
    }
    void inc() { value++; }
    int get() { return value; }
};

int main() {
    Counter a(5);
    Counter b = a;
    b.inc();
    b.inc();
    cout << a.get() << " " << b.get();
    return 0;
}
```

**1.2**
```cpp
class Box {
    int size;
public:
    Box(int s) : size(s) {}
    ~Box() {
        cout << "Удалён " << size << endl;
    }
};

int main() {
    Box a(1);
    {
        Box b(2);
    }
    cout << "Конец" << endl;
    return 0;
}
```

**1.3**
```cpp
class Number {
    int x;
public:
    Number(int x) : x(x) {}
    Number add(Number other) {
        return Number(x + other.x);
    }
    int get() { return x; }
};

int main() {
    Number a(3);
    Number b(4);
    Number c = a.add(b);
    cout << c.get();
    return 0;
}
```

**1.4**
```cpp
class Wallet {
    int money;
public:
    Wallet(int m) : money(m) {}
    void spend(int x) {
        if (x <= money)
            money -= x;
    }
    int get() { return money; }
};

int main() {
    Wallet w(100);
    w.spend(30);
    w.spend(200);
    w.spend(50);
    cout << w.get();
    return 0;
}
```

---

## Часть 2. «Найди ошибку»

**2.1**
```cpp
class Point {
    int x, y;
public:
    Point(int x, int y) {
        x = x;
        y = y;
    }
    void show() {
        cout << x << " " << y;
    }
};

int main() {
    Point p(3, 4);
    p.show();
    return 0;
}
```
*(подсказка: параметры конструктора имеют те же имена, что и поля)*

**2.2**
```cpp
class Student {
    string name;
public:
    Student(string n) : name(n) {}
    string getName() { return name; }
};

int main() {
    Student s("Иван");
    cout << s.name;
    return 0;
}
```

**2.3**
```cpp
class Array {
    int data[5];
public:
    void set(int i, int val) {
        data[i] = val;
    }
    int get(int i) {
        return data[i];
    }
};

int main() {
    Array a;
    for (int i = 0; i <= 5; i++)
        a.set(i, i * 2);
    return 0;
}
```
*(подсказка: где границы массива и что делает цикл)*

---

## Часть 3. «Заполни пропуски»

**3.1**
```cpp
class Rectangle {
    double w, h;
public:
    Rectangle(double w, double h) : ___(w), ___(h) {}

    double area() {
        return ___ * ___;
    }

    void scale(double k) {
        w ___ k;
        h *= ___;
    }
};
```

**3.2**
```cpp
class BankAccount {
    string owner;
    double balance;
public:
    BankAccount(string o, double b) : ___(o), ___(b) {}

    void deposit(double x) {
        balance ___ x;
    }

    bool withdraw(double x) {
        if (x ___ balance) {
            balance -= x;
            return ___;
        }
        return false;
    }

    double get() { return ___; }
};
```

---

## Часть 4. «Напиши класс сам»

**4.1. Класс `Fraction` (дробь)**
Приватные поля: `int num` (числитель), `int den` (знаменатель).
Методы:
- конструктор с двумя параметрами;
- `double value()` — возвращает десятичное значение дроби;
- `void show()` — выводит в виде `num/den`.

Проверь в `main()`: создай дроби 3/4 и 7/2, выведи их значения.

---

**4.2. Класс `Vector2D`**
Приватные поля: `double x`, `double y`.
Методы:
- конструктор;
- `double length()` — длина вектора (корень из `x² + y²`, используй `sqrt` из `<cmath>`);
- `Vector2D add(Vector2D other)` — возвращает новый вектор-сумму.

В `main()` сложи два вектора и выведи длину результата.

---

**4.3. Класс `Counter`**
Приватное поле: `int value` (по умолчанию 0).
Методы:
- `inc()`, `dec()`, `reset()`;
- `int get()` — возвращает значение;
- **два конструктора**: без параметров (старт 0) и с параметром (стартовое значение).

В `main()` создай два счётчика — один пустой, другой со стартом 10. Поработай с обоими.

---

**4.4. Класс `Book`**
Приватные поля: `string title`, `int pages`, `int currentPage` (по умолчанию 1).
Методы:
- конструктор с названием и количеством страниц;
- `void read(int n)` — читает `n` страниц вперёд (не выходя за `pages`);
- `void show()` — выводит название и прогресс в процентах.

Проверь: книга на 200 страниц, прочитай 50, покажи прогресс.

---

**4.5. Класс `Player`**
Приватные поля: `string name`, `int hp` (100), `int damage` (10).
Методы:
- конструктор с именем;
- `void attack(Player &enemy)` — наносит урон врагу (принимай **по ссылке**!);
- `bool isAlive()` — жив ли (`hp > 0`);
- `void show()` — выводит имя и текущее здоровье.

В `main()` создай двух игроков и устрой бой в цикле `while`, пока один не умрёт.

---

## Часть 5. «Собери класс из кусочков»

Строки перепутаны. Расставь в правильном порядке.

**5.1**
```cpp
    }
        return 3.14 * r * r;
    double area() {
class Circle {
public:
    Circle(double r) : r(r) {}
};
private:
    double r;
```

**5.2**
```cpp
    }
        balance += x;
    void deposit(double x) {
class Wallet {
public:
private:
    double balance;
    Wallet(double b) : balance(b) {}
};
```

---

## Часть 6. Работа в парах

Один студент **проектирует класс**: придумывает назначение, поля, конструктор и 3–4 метода, описывает их словами.
Второй — **реализует класс** по описанию и пишет тестовый `main()`, где проверяет все методы.

Затем меняются ролями и делают второй класс.

---

## Часть 7. «Придумай сам»

Придумай класс с **приватными полями**, конструктором и **минимум тремя методами**, один из которых возвращает значение (не `void`). Реализуй его и проверь в `main()`.

Примеры тем: `Timer`, `Product`, `Movie`, `Song`, `Task`, `Elevator`.

-
