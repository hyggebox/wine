# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Данные

Данные для сайта оформляются в `.xlsx` файл в таблицу вида:

| Категория   | Название    | Сорт        | Цена        | Картинка    | Акция       |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| Белые вина  | Кокур       | Кокур       | 450         | kokur.png   |                      |
| Напитки     | Чача        |             | 299         | chacha.png  | Выгодное предложение |

Путь к картинкам указан относительно папки `/images/`


## Установка и запуск

- Скачайте код
- Python3 должен быть уже установлен. Используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

- Запустите сайт командой `python` (`python3`, если есть конфликт с Python2):

```
python main.py
```
- По умолчанию данные для сайта подгружаются из файла `wines.xlsx` в корневой папке.
Можно задать другой путь к `.xlsx` файлу с данными. Для этого введите
```
python main.py --data_path <путь_к_файлу>
```

- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).