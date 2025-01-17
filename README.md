# My Favorite Films — Blog
Интерактивный блог.

Создан в рамках дипломной работы по теме: «Анализ и сравнение написания web-приложений с использованием разных фреймворков».

## Цель проекта
Разработать простое веб-приложение с использованием Django для сравнения с подобной разработкой на Flask и FastAPI.

## Обзор проекта
Веб-приложение на базе фреймворка Django, которое позволит:
* админстраторам вносить записи в базу данных;
* пользователям просматривать каталог полностью или фильтруя по категориям.

## Структура проекта
Проект включает в себя следующие ключевые компоненты:

### Домашняя страница
Здесь отображается список всех категорий, имеющихся в базе данных. Каждый пункт — это ссылка на страницу каталога фильмов с динамическим URL для фильтрации.
Также есть меню со ссылками на домашнюю страницу и полный каталог.

<img src="https://github.com/nsazhi/My-Favorite-Films-Blog/blob/master/screenshorts/main_page.jpg">

Рис. 1. Домашняя страница

### Страница каталога
Здесь отображаются карточки фильмов с информацией. В зависимости от параметров запроса, отображается весь каталог фильмов или с фильтрацией по категориям, а также меняется заголовок страницы.
Также на странице есть кнопка выбора фильтра со ссылками, содержащими параметры.

<img src="https://github.com/nsazhi/My-Favorite-Films-Blog/blob/master/screenshorts/catalog.jpg">

Рис. 2. Страница полного каталога

<img src="https://github.com/nsazhi/My-Favorite-Films-Blog/blob/master/screenshorts/catalog2.jpg">

Рис. 3. Страница каталога с фильтром по категории при переходе с домашней страницы.

