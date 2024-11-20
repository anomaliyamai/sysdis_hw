## Для локального запуска:
1) minikube start
2) kubectl apply -f ./project/kuber_manifests
3) В etc/hosts добавить строку 127.0.0.1 app.com
4) minikube tunnel
5) Теперь по адресу app.com доступен сервис

## Доступ к бд
1) mock_db доступна из подов с сервисом по адресу mock-db-service:5432
2) db доступна из подов с сервисом по адресу psql-db-service:5432