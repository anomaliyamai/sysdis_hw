## Расчеты и требования

Рассмотрим эндпойнты-ручки.

### 1. Назначить заказ

Ожидается, что на этот эндпойнт будет нагрузка порядка 200 RPS. Происходит запись в БД.

### 2. Получить заказ

Учитывая, что у нас будет 500к исполнителей и то, что каждый исполнитель запрашивает эту ручку каждую минуту до того, как получить заказ, получаем нагрузку в 8,3k RPS. Происходит запись в БД.

### 3. Отменить заказ

Мы ожидаем, что 5% от рейта заказов будет отменяться, значит нагрузка будет порядка 10 RPS. Происходит удаление записей из БД.
