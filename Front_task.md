
**Задание 1: Персональная Визитка (HTML/CSS)**  
*   **Цель:** Верстка статичной страницы.  
*   **Задача:** Создать HTML-страницу "О себе".  
*   **Требования:**  
    *   Заголовок с именем.  
    *   Фото или аватар.  
    *   Краткий абзац с биографией или интересами.  
    *   Список контактов (email, соцсети - иконки Font Awesome или ссылки).  
    *   Использовать семантические теги (`<header>`, `<section>`, `<footer>`).  
    *   Стилизовать с помощью CSS (шрифты, цвета, отступы, фон).  
    *   Сделать адаптивной (на мобильных - элементы друг под другом).  

**Задание 2: Светофор (HTML/CSS/JS - Базовый DOM)**  
*   **Цель:** Работа с DOM и событиями.  
*   **Задача:** Создать интерактивный светофор.  
*   **Требования:**  
    *   Верстка: 3 круга (красный, желтый, зеленый) вертикально.  
    *   Кнопки: "Старт" (запускает автоматическое переключение: красный -> желтый -> зеленый -> желтый -> красный... с задержками), "Стоп" (останавливает автоматическое переключение).  
    *   При клике на любой цвет - этот цвет включается, остальные выключаются (ручной режим).  
    *   Использовать `setInterval`/`clearInterval` и обработчики событий (`onclick`).  

**Задание 3: Список задач (To-Do List) (HTML/CSS/JS - DOM манипуляции)**  
*   **Цель:** Работа с формами, динамическое изменение DOM.  
*   **Задача:** Создать простой список дел.  
*   **Требования:**  
    *   Поле ввода (`<input type="text">`) и кнопка "Добавить".  
    *   При нажатии "Добавить" или Enter - текст из поля добавляется как новый элемент в список (`<ul>` или `<ol>`).  
    *   Каждый элемент списка имеет:  
        *   Текст задачи.  
        *   Кнопку "Удалить" (убирает элемент из списка).  
        *   Чекбокс. При отметке чекбокса - задача перечеркивается (или меняет фон).  
    *   Пустое поле ввода не должно добавляться.  
    *   Данные сохранять в `localStorage` (чтобы список оставался после перезагрузки страницы - *опционально, для усложнения*).  

**Задание 4: Таймер обратного отсчета (HTML/CSS/JS - Работа со временем)**  
*   **Цель:** Работа с `Date` и `setInterval`.  
*   **Задача:** Создать таймер, отсчитывающий время до указанной даты/времени.  
*   **Требования:**  
    *   Поле ввода для даты/времени (`<input type="datetime-local">`).  
    *   Кнопка "Старт".  
    *   Дисплей, показывающий: Дни, Часы, Минуты, Секунды до выбранной даты.  
    *   При нажатии "Старт" начинается обратный отсчет. Таймер обновляется каждую секунду.  
    *   Когда отсчет достигает 0 - таймер останавливается и выводится сообщение (например, "Время вышло!").  

**Задание 5: Простой слайдер изображений (HTML/CSS/JS - Анимации, DOM)**  
*   **Цель:** Создание интерактивного элемента интерфейса.  
*   **Задача:** Создать слайдер, переключающий изображения.  
*   **Требования:**  
    *   Контейнер для текущего изображения.  
    *   Две кнопки: "Назад" (<) и "Вперед" (>).  
    *   Массив с URL изображений (минимум 3).  
    *   При клике "Вперед" показывается следующее изображение в массиве. После последнего - первое.  
    *   При клике "Назад" - предыдущее изображение. Перед первым - последнее.  
    *   Добавить плавную смену изображений (CSS `transition` на свойство `opacity`).  
    *   Точки (индикаторы) под слайдером, показывающие текущую позицию и позволяющие перейти к конкретному слайду (*опционально, для усложнения*).  

**Задание 6: Валидация формы (HTML/CSS/JS - Обработка форм)**  
*   **Цель:** Валидация пользовательского ввода.  
*   **Задача:** Создать форму регистрации с проверкой данных.  
*   **Требования:**  
    *   Поля: Имя (только буквы), Email (валидный формат), Пароль (минимум 8 символов, буквы и цифры), Подтверждение пароля.  
    *   Кнопка "Зарегистрироваться".  
    *   При вводе в поле (событие `input` или `blur`):  
        *   Рядом с полем появляется текст ошибки (если данные невалидны).  
        *   Поле подсвечивается красной рамкой при ошибке, зеленой - при корректном вводе.  
    *   При нажатии "Зарегистрироваться":  
        *   Проверяются ВСЕ поля.  
        *   Если есть ошибки - показываются все сообщения, отправка отменяется.  
        *   Если все верно - выводится alert "Форма успешно отправлена!" (или имитация отправки).  
    *   Проверка совпадения паролей.  
