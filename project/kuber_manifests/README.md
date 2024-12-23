## Для локального запуска:
1) minikube start
2) kubectl apply -f ./project/kuber_manifests/db. Ждем пока поднимется
3) kubectl apply -f ./project/kuber_manifests/app
4) В etc/hosts добавить строку 127.0.0.1 app.com
5) minikube tunnel
6) Теперь по адресу app.com доступен сервис

## Доступ к бд
1) mock_db доступна из подов с сервисом по адресу mock-db-service:5432
2) db доступна из подов с сервисом по адресу psql-db-service:5432


## Из корня

docker build -f Dockerfile -t app-container .

docker build -f DockerfileJob -t alembic .