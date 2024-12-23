#### Dockerfile для БД

```shell
docker run --name mock_db -p 5433:5432 -v ./resources/volumes/local/pgdata:/var/lib/postgresql/data -e POSTGRES_USER=pguser -e POSTGRES_PASSWORD=pgpass -e POSTGRES_DB=mock_db -d postgres:16
```

#### Для alembic
```shell
export POSTGRES_CONNECTION_STRING="postgresql://pguser:pgpass@localhost:5433/mock_db"
```
