## Для локального запуска:
1) minikube start
2) docker build -f Dockerfile -t app-container .
3) docker build -f DockerfileJob -t alembic .
4) docker build -f DockerfileJobMigrations -t migrations .

5) kubectl apply -f ./project/kuber_manifests/db. Ждем пока поднимется
6) kubectl apply -f ./project/kuber_manifests/app
7) В etc/hosts добавить строку <minikube ip> app.local
8) Теперь по адресу app.local доступен сервис

## Доступ к бд
1) mock_db доступна из подов с сервисом по адресу mock-db-service:5432
2) db доступна из подов с сервисом по адресу psql-db-service:5432

