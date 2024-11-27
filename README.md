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
