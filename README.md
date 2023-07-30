# yealink_reboot
Python скрипт для перезапуска IP-телефонов Yealink.
### Подготовка
Для того, чтобы управлять телефоном с помощью HTTP запросов, нужно выполнить на нём следующие действия:
1. Через Web-интерфейс задать адрес хоста, с которого будет запускаться скрипт: в `Features > Remote Control > Action URI Allow IP List` ввести IP-адрес;
2. Создать и загрузить в телефон файл `config.cfg`, со следующими строками:

#!version:1.0.0.1

action_url.show_msgbox = 0

### Использование
1. Открыть скрипт в редакторе и внести в словарь `phones` IP-адреса, логины и пароли аппаратов;
2. Настроить планировщик на запуск скрипта по расписанию.
### P.S.:
После этапа "Подготовка" можно вручную делать скриншоты c дисплея аппарата, задав в браузере URL:

`http://user:password@a.b.c.d/screencapture/download`

...перезапуск:

`http://user:password@a.b.c.d/servlet?key=Reboot`

...или даже звонить с него через Web-интерфейс в `Directory > Phone Call Info > Call Panel`.

Больше команд по ссылке https://habr.com/ru/companies/ipmatika/articles/716476/
