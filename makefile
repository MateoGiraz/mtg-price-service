postgres:
	docker run --name mtg-prices -p 5432:5432 -e POSTGRES_PASSWORD=secret -d postgres

createdb:
	docker exec -it mtg-prices createdb --username=postgres --owner=postgres prices

dropdb:
	docker exec -it mtg-prices dropdb -U postgres prices

postgres-terminal:
	docker exec -it mtg-prices psql -U postgres prices

.PHONY: postgres createdb dropdb postgres-terminal 