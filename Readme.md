### Тестовое задание Python ###

Выполняет следующие функции:

1. Получает данные с документа при помощи Google API, сделанного в Google Sheets.
2. Данные добавляются в БД, в том же виде, что и в файле –источнике, с добавлением колонки «стоимость в руб.»
   -  СУБД на основе PostgreSQL.
   -  Данные для перевода $ в рубли получены по курсу ЦБ РФ.
3. Учтено, что строки в Google Sheets таблицу могут удаляться, добавляться и изменяться.

   


## Настройка Google Cloud

1. На веб-сайте необходимо зарегистрировать свой проект:
https://console.cloud.google.com/apis/dashboard?project=smart-period-359108 
2. Библиотека – Создать проект
Поиск в библиотеке API:
- Google Drive – Включить
- Создать учётные данные
- Какой API вы используете – Google Drive API
- Откуда вы будете вызывать API – Веб-Сервер
- К каким данным вы будете обращаться – Данные приложения
- Используете этот API для App Engine или Compute Engine – Нет
- Выбрать тип учётных данных
- Роль – Проект – Редактор
- Тип ключа – JSON
- Продолжить (загрузка ключа в формате JSON)
- Открыть полученный файл JSON
- Скопировать значение поля "client_email"
- В своем гугл диске для файла:
https://docs.google.com/spreadsheets/d/1f-qZEX1k_3nj5cahOzntYAnvO4ignbyesVO7yuBdv_g/edit#gid=0
Ввести скопированное значение и предоставить доступ на редактирование
3. Закаченный JSON файл переименовать в credrntials.json и добавить в проект


Дополнительная информация по настройке:
- [Работаем с API Google Drive с помощью Python](http://datalytics.ru/all/rabotaem-s-api-google-drive-s-pomoschyu-python/)
- [Начинаем работу с Google Sheets на Python](https://itnan.ru/post.php?c=1&p=483302)

## Создании миграции
- python manage.py makemigrations
- python manage.py migrate


