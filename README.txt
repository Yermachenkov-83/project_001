PROJECT_001: (time purse)
superuser: admin/admin


app_01:




йойо:
работа приложухи:
1 шаг - регистрация/авторизация. (в идеале - вход,если не авторизирован, если регистрация была- прямой ереход. куки...
на сколько реально такое сделать нам на данный момент?) или ограничимся вкладкой регистрации, для проработки этого момента?
2 переход в рабочее пространство с выбором :
а. добавить активность : предлогает  выбрать ил добавить активность + ввести время в минутах(потраченое)
б. посмотреть суммарное время по категории (и интервал: всего/месяц/неделя) + список поэлементно ниже(за указанный срок)
3. возможность удалить активность + все с ней связанные записи каскадом
(файл визуала приложил)

реализация:
думаю это ограничивается одной папочкой апки.
по вьюхам - 3 страницы: основная/добавить, основная/весь списик и вывод по позиции.
по моделям: позиции (основные забиваем с админки, остальные добавляеются через кнопку) + время...
при выводе - суммируем по позиции и выдаем в минутах и в часах.
есть вариант делать 2 апки одинаковые параллельно ,чтобы ничего не пропустить,и друг друга проверять, сравнивая особенности кода.
и потом каждый свое зальет в сеть и ссылку на СВ приложит. это как варик, можно и одно пилить.


29.01:
созданы модели + миграция + в админку модели записал
зайди в админку, проверь,подгрузились ли мои данные из БД вместе с ней. (пароль и логин вверху этого файла)
запушил картинки временные, вместо лого финальных, которых поканет.
не понял,почему ругается, если создаешь активити нэйм без картинки. вроде БЛАНЕ=тру...
+ обновил рекваймент (пиллов добавил, при миграции)

30.01:
проверка работы бранчей
