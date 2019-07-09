
.DEFAULT_GOAL := default

default:
	@ echo "make migration -e NAME=\"migration name\" #  create new migration"
	@ echo "make migrate                            #  migrate DB to last revision"
	@ echo "make downgrade                          #  downgrade db"

migration:
	docker-compose exec velo_core bash -c "alembic -c /etc/velocore/alembic.ini revision --autogenerate -m \"$(NAME)\""

migrate:
	docker-compose exec velo_core bash -c "alembic -c /etc/velocore/alembic.ini upgrade head"

downgrade:
	docker-compose exec velo_core bash -c "alembic -c /etc/velocore/alembic.ini downgrade -1"
