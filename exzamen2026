

Модуль 4. Разработка информационной системы (Учёт заказов клиентов)

### Цель

Разработать приложение для учёта заказов: авторизация, две роли («менеджер» и «кладовщик»), просмотр и изменение заказов.

### 4.1. База данных

#### Создать таблицы:

```sql
-- Пользователи
CREATE TABLE Users (
    UserID INTEGER PRIMARY KEY,
    Login TEXT UNIQUE,
    Password TEXT,
    FullName TEXT,
    Role TEXT CHECK(Role IN ('менеджер','кладовщик')),
    IsActive INTEGER DEFAULT 1
);

-- Заказы
CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    CustomerName TEXT,
    Product TEXT,
    Quantity INTEGER,
    Status TEXT DEFAULT 'новый'  -- новый, в работе, завершён
);
```

#### Тестовые данные:

* Менеджер: login: admin, pass: 123, роль менеджер.
* Кладовщик: login: user, pass: 123, роль кладовщик.
* 3–4 заказа со статусами.

### 4.2. Функционал

#### Общее:

* Форма входа: логин/пароль, проверка, блокировка после 3 неудачных попыток (учётная запись деактивируется).
* При успешном входе открывается таблица заказов.

#### Менеджер:

* Может добавлять новые заказы (все поля).
* Может менять статус заказа (на любой).
* Может удалять заказ.

#### Кладовщик:

* Может посмотреть список заказов.
* Не может добавлять/редактировать/удалять заказы.

Интерфейс:

· После входа – таблица заказов.
· Кнопка выхода.
· Для менеджера – кнопки «Добавить», «Редактировать», «Удалить».
· Для кладовщика – выпадающий список статуса для каждой строки.

4.3. Критерии оценки (макс. 10 баллов)

1. Авторизация с проверкой блокировки – 2 балла.
2. Отображение таблицы заказов – 1 балл.
3. Функционал менеджера (CRUD) – 3 балла.
4. Функционал кладовщика (смена статуса) – 2 балла.
5. Качество кода и работа с БД – 2 балла.

---

Краткий SQL-скрипт для подготовки БД

```sql
-- Создание таблиц
CREATE TABLE Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Login TEXT UNIQUE NOT NULL,
    Password TEXT NOT NULL,
    FullName TEXT,
    Role TEXT NOT NULL CHECK(Role IN ('менеджер','кладовщик')),
    IsActive INTEGER DEFAULT 1
);

CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerName TEXT NOT NULL,
    Product TEXT NOT NULL,
    Quantity INTEGER NOT NULL CHECK(Quantity > 0),
    Status TEXT DEFAULT 'новый' CHECK(Status IN ('новый','в работе','завершён'))
);

-- Тестовые данные
INSERT INTO Users (Login, Password, FullName, Role) VALUES
    ('admin', '123', 'Администратор', 'менеджер'),
    ('user', '123', 'Кладовщик', 'кладовщик');

INSERT INTO Orders (CustomerName, Product, Quantity, Status) VALUES
    ('ООО "Ромашка"', 'Ноутбук', 2, 'новый'),
    ('ИП Петров', 'Принтер', 1, 'в работе'),
    ('ЗАО "Весна"', 'Сканер', 3, 'завершён');
```

Этот вариант легко реализовать за отведённое время и проверить.