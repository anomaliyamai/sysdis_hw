# ДЗ по Дизайну систем

[ADR](/ADR.md)

### Входные параметры

X = 200, 
Y = 500k, 
Z = 50кб, 
W = 5%, 

Архивация 5 лет

### Расчет нагрузки

200рпс * 3600(в час) * 24(в сутки) * 365(в год) * 5(лет) * 50(кб) ~ 1500ТБ данных должно храниться в бд

### Схема системы

[puml схема](/docs/system_scheme.puml)

### Сущности в БД

[puml схема](/docs/erd.puml)

### Scalability

Систему можно масштабировать путем увеличения количества подов, на которых поднимается приложение, чтобы принимать больше rps. С бд так не получится, потому что все запросы в нашей реализации пишущие и должны уходить в мастер.

### Reliability

В нашем варианте нужно было реализовать динамические конфиги. Они были реализованы, как кронтаска в коде сервиса. Помимо этого у нас есть и статические параметры конфигурации, передаваемые из configMap k8s (host и port, по которому доступно приложение)


## Расчеты и требования

Рассмотрим эндпойнты-ручки.

### 1. Назначить заказ

Ручка принимает в себя ID исполнителя и ID заказа. Работать она должна следующим образом:

1. Принимаем идентификаторы и по ним собираем информацию о назначенном заказе, тем самым обогащаем данные и высчитываем стоимость.
2. Записываем и сохраняем всю информацию персистентно о заказе в базу данных.
3. Возвращаем статус.

Ожидается, что на этот эндпойнт будет нагрузка порядка 200 RPS.

### 2. Получить заказ

Ручка принимает в себя ID исполнителя. Работать она должна следующим образом:

1. Достаем первый из заказов назначенных на исполнителя в соответствующей ручке из базы данных.
2. Проставляем статус в базу данных что заказ взят и отмечаем время взятия заказа.
3. Возвращаем информацию о взятом заказе.

Учитывая, что у нас будет 500к исполнителей и то, что каждый исполнитель запрашивает эту ручку каждую минуту до того, как получить заказ, получаем нагрузку в 8,3k RPS.

### 3. Отменить заказ

Ручка принимает ID заказа, который хотим отменить. Так будет работать:

1. Проверяем можно ли отменить заказ (нельзя отменить уже полученный заказ исполнителем, нельзя отменить заказ назначенный уже 10 минут назад), если все хорошо, то удаляем заказ из базы данных.
2. Возвращаем статус операции.

Мы ожидаем, что 5% от рейта заказов будет отменяться, значит нагрузка будет порядка 10 RPS.
