# Напишите ФУНКЦИИ реализующие проверки:

## **Задание 1: Сложная система скидок**
**Условие:**  
Магазин применяет скидки по сложной системе:
- **10%** если: (VIP-клиент И сумма > 5000) ИЛИ (не VIP И сумма > 10000)
- **15%** если: (возраст < 25 ИЛИ возраст > 60) И сумма > 7000 И НЕ первый заказ
- **20%** если: (VIP И сумма > 10000) И (акция ИЛИ сезон распродаж)

Напишите программу, которая определяет размер скидки.

```python
# Пример данных
vip = True
summa = 12000
age = 30
first_order = False
sale_season = True
promotion = False

# Ваш код здесь
```

---

## **Задание 2: Сложная проверка пароля**
**Условие:**  
Пароль считается надежным, если:
- Длина от 8 до 20 символов И
- Содержит хотя бы одну цифру И одну заглавную букву И
- (Содержит спецсимвол ИЛИ длина ≥ 12) И
- НЕ содержит пробелов И НЕ начинается с цифры

```python
def check_password(password):
    # Ваша реализация
    pass

# Тесты
print(check_password("Pass123!"))     # Должен вернуть True
print(check_password("short"))        # Должен вернуть False
print(check_password("123Password"))  # Должен вернуть False (начинается с цифры)
```

---

## **Задание 3: Система доступа с приоритетами**
**Условие:**  
Определите уровень доступа:
- **Admin**: (сотрудник И админ) ИЛИ (root И НЕ заблокирован)
- **Moderator**: (сотрудник И модератор) ИЛИ (стаж > 2 года И рейтинг > 4.5)
- **User**: НЕ заблокирован И (подтвержден ИЛИ гостевой режим)
- **Blocked**: заблокирован ИЛИ (нарушения > 3 И НЕ premium)

```python
employee = False
admin = False
root = True
blocked = False
experience = 1
rating = 4.8
confirmed = True
guest_mode = False
violations = 2
premium = False

# Определите уровень доступа
```

---

## **Задание 4: Сложное условие для кредита**
**Условие:**  
Кредит одобряется, если:
- (Возраст ≥ 21 И возраст ≤ 65) И
- (Доход ≥ 50000 ИЛИ есть поручитель) И
- (Кредитная история хорошая ИЛИ первоначальный взнос ≥ 30%) И
- НЕ (просрочки в прошлом И сумма кредита > 1000000) И
- (стаж работы ≥ 1 года ИЛИ доход ≥ 100000)

```python
age = 25
income = 45000
has_guarantor = True
credit_history_good = False
down_payment_percent = 35
past_delinquencies = True
loan_amount = 800000
work_experience = 0.5

# Одобрен ли кредит?
```

---

## **Задание 5: Сложная система оценок**
**Условие:**  
Студент получает:
- **A**: (баллы ≥ 90 И посещаемость ≥ 80%) ИЛИ (баллы ≥ 85 И дополнительные задания)
- **B**: (баллы ≥ 75 И НЕ списал) И (посещаемость ≥ 70% ИЛИ уважительная причина)
- **C**: баллы ≥ 60 И НЕ (посещаемость < 50% И нет уважительной причины)
- **F**: в остальных случаях

```python
score = 87
attendance = 85
extra_tasks = True
cheated = False
valid_reason = True

# Какая оценка?
```

---

## **Задание 6: Умный дом - сложная логика**
**Условие:**  
Система умного дома включает кондиционер, если:
- (Температура > 25°C И влажность > 60%) ИЛИ 
- (Температура > 28°C И есть люди дома) ИЛИ
- (Температура > 22°C И влажность > 70% И НЕ открыты окна)

И выключает, если:
- Температура < 20°C ИЛИ 
- (Нет людей дома И температура < 26°C) ИЛИ
- (открыты окна И температура < 24°C)

```python
temperature = 26
humidity = 65
people_home = True
windows_open = False

# Включить или выключить кондиционер?
```

---

## **Задание 7: Сложная проверка email**
**Условие:**  
Email считается валидным, если:
- Содержит ровно один '@' И
- (Длина имени пользователя ≥ 3 И ≤ 15) И
- Доменная часть в списке разрешенных ['gmail.com', 'yandex.ru', 'mail.ru'] И
- НЕ содержит запрещенных символов [' ', ',', ';'] И
- (НЕ начинается с цифры ИЛИ имеет длину ≥ 5)

```python
def validate_email(email):
    allowed_domains = ['gmail.com', 'yandex.ru', 'mail.ru']
    forbidden_chars = [' ', ',', ';']
    
    # Ваша реализация
    pass

# Тесты
print(validate_email("user123@yandex.ru"))  # True
print(validate_email("ab@mail.ru"))         # False (имя слишком короткое)
print(validate_email("123@mail.ru"))        # False (начинается с цифры и короткое)
```

---

## **Задание 8: Сложное условие для страховки**
**Условие:**  
Страховой полис выдается, если:
- (Возраст ≥ 18 И возраст ≤ 70) И
- (Стаж вождения ≥ 2 года ИЛИ возраст ≥ 25) И
- НЕ (серьезные нарушения И возраст < 30) И
- (Город не в списке高风险 ИЛИ стаж ≥ 5 лет) И
- (Кредитная история хорошая ИЛИ первоначальный взнос ≥ 50%)

```python
age = 22
driving_experience = 1
serious_violations = True
high_risk_city = False
credit_history_good = False
down_payment = 40

# Выдается ли страховка?
```

---

## **Задание 9: Сложная система аутентификации**
**Условие:**  
Доступ разрешен, если:
- (Правильный пароль И двухфакторная аутентификация) ИЛИ
- (Биометрическая аутентификация И устройство доверенное) ИЛИ
- (Временный код И IP в белом списке И НЕ подозрительная активность) И
- НЕ (аккаунт заблокирован ИЛИ превышены попытки входа)

```python
correct_password = True
two_factor = False
biometric = True
trusted_device = True
temp_code = False
white_list_ip = True
suspicious_activity = False
account_blocked = False
login_attempts_exceeded = False

# Разрешен ли доступ?
```

---

## **Задание 10: Сложная логика игры**
**Условие:**  
Игрок получает бонус, если:
- (Уровень ≥ 10 И выполнено ≥ 5 квестов) ИЛИ
- (Премиум-аккаунт И играл сегодня) ИЛИ
- (Друг в сети И совместные достижения) И
- НЕ (использовал читы ИЛИ баны в истории) И
- (время игры ≥ 10 часов ИЛИ уровень ≥ 20)

```python
level = 15
quests_completed = 4
premium_account = True
played_today = True
friend_online = False
joint_achievements = False
used_cheats = False
ban_history = False
play_time_hours = 8

# Получает ли бонус?
```




---
---


Мы создадим простую игру, где игрок управляет символом '@' на поле размером 20x10.
Цель игры — собирать монеты (обозначенные как '$'), которые появляются в случайных местах.
Игрок может двигаться вверх, вниз, влево и вправо. Каждую собранную монету счетчик увеличивается.
Также на поле будут препятствия (обозначенные как '#'), при столкновении с которыми игра заканчивается.



* Инициализация игры: задаем размеры поля, начальное положение игрока, счет, размещаем монеты и препятствия.

* Функция отрисовки поля: очищаем консоль и рисуем текущее состояние.

* Обработка ввода: с помощью keyboard проверяем нажатые клавиши и перемещаем игрока.

* Проверка столкновений: с монетами (увеличиваем счет и создаем новую монету) и с препятствиями (завершаем игру).
```
import random
import time
import os
import keyboard

pos_player = {'x':0, 'y':0}
score = 0


def draw_area(area):
    os.system('cls')
    for row in area:
        print(''.join(row))
    print(pos_player)
    print(f"score:{score}")

def gen_area(height, width):
    area = []
    for i in range(height):
        if i == 0 or i == height - 1:
            area.append(list("#"*width))
        else:
            area.append(list("#" + " "*(width-2) + "#"))
    draw_area(area)
    for i, row in enumerate(area):
        for j, element in enumerate(row):
            if element == ' ':
                if random.randint(1, 100) < 5:
                    area[i][j] = "$"
                elif random.randint(1, 100) < 10:
                    area[i][j] = "#"

            draw_area(area)
            time.sleep(0.01)
    return area

def add_player(area):
    for i, row in enumerate(area):
        for j, element in enumerate(row):
            if element == ' ':
                area[i][j] = "@"
                pos_player['x'] = i
                pos_player['y'] = j
                return area

def move_player(area, dx, dy):
    global score
    new_x = pos_player['x'] + dx
    new_y = pos_player['y'] + dy
    if area[new_y][new_x] == '#':
        return
    if area[new_y][new_x] == '$':
        score += 1

    area[pos_player['y']][pos_player['x']] = ' '
    area[new_y][new_x] = '@'
    pos_player['x'] = new_x
    pos_player['y'] = new_y

    draw_area(area)
    time.sleep(0.2)

def main():
    area = gen_area(10, 20)
    area = add_player(area)
    while True:
        if keyboard.is_pressed('w'): move_player(area, dx=0, dy=-1)
        elif keyboard.is_pressed('s'): move_player(area, dx=0, dy=1)
        elif keyboard.is_pressed('a'): move_player(area, dx=-1, dy=0)
        elif keyboard.is_pressed('d'): move_player(area, dx=1, dy=0)


main()

```

