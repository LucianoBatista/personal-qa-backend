install:
	@echo "Installing dependencies..."
	pipenv install --dev black isort flake8 pre-commit mkdocs-material mkdocs-mermaid2-plugin fontawesome-markdown
	pipenv install numpy==1.23 pandas==1.5
	pipenv install fastapi==0.95.1 uvicorn==0.21.1 gunicorn==20.1.0 pydantic==1.10.7

install-extra:
	@echo "Installing extra dependencies..."
	@if [ "yes" = "yes" ]; then \
		pipenv install sqlalchemy==2.0.10 alembic==1.10.4 pymysql==1.0.3 mysqlclient==2.1.1 mysql-connector-python==8.0.32; \
	fi
	@if [ "no" = "yes" ]; then \
		pipenv install celery==5.2.7 redis==4.5.4; \
	fi

structurize:
	@echo "Structurizing project..."
	@if [ "yes" = "yes" ]; then \
		mkdir -p project/app/models && \
		mkdir -p project/app/database/repository && \
		touch project/app/database/repository/.gitkeep && \
		touch project/app/database/__init__.py && \
		mv models.py project/app/models/models.py && \
		mv session.py project/app/database/session.py; \
	fi
	@if [ "yes" = "no" ]; then \
		echo "Removing database files..."; \
	fi
	@if [ "no" = "yes" ]; then \
		mkdir -p project/app/celery && \
		mv celery_utils.py project/app/celery/setup.py && \
		mv initial_celery.py project/__init__.py && \
		mv main_celery.py project/main.py &&\
		rm initial.py && \
		rm main.py; \
	fi
	@if [ "no" = "no" ]; then \
		mv initial.py project/__init__.py && \
		mv main.py project/main.py &&\
		rm initial_celery.py && \
		rm main_celery.py && \
		rm celery_utils.py; \
	fi

dockerize:
	@echo "Dockerizing project..."
	@if [ "yes" = "yes" ] && [ "no" = "yes" ]; then \
		mv docker-compose-database-queue.yaml docker-compose.yaml &&\
		rm docker-compose-database.yaml && \
		rm docker-compose-queue.yaml && \
		mv .example-db-queue.env .example.env && \
		rm .example-db.env && \
		rm .example-queue.env && \
		mv entrypoint-db-queue.sh entrypoint.sh && \
		rm entrypoint-db.sh && \
		rm entrypoint-queue.sh; \
	elif [ "yes" = "yes" ] && [ "no" = "no" ]; then \
		mv docker-compose-database.yaml docker-compose.yaml &&\
		rm docker-compose-database-queue.yaml && \
		rm docker-compose-queue.yaml && \
		mv .example-db.env .example.env && \
		rm .example-db-queue.env && \
		rm .example-queue.env && \
		mv entrypoint-db.sh entrypoint.sh && \
		rm entrypoint-queue.sh && \
		rm entrypoint-db-queue.sh; \
	elif [ "yes" = "no" ] && [ "no" = "yes" ]; then \
		mv docker-compose-queue.yaml docker-compose.yaml &&\
		rm docker-compose-database-queue.yaml && \
		rm docker-compose-database.yaml && \
		mv .example-queue.env .example.env && \
		rm .example-db-queue.env && \
		rm .example-db.env && \
		mv entrypoint-queue.sh entrypoint.sh && \
		rm entrypoint-db.sh && \
		rm entrypoint-db-queue.sh; \
	elif [ "yes" = "no" ] && [ "no" = "no" ]; then \
		rm docker-compose-database-queue.yaml && \
		rm docker-compose-database.yaml && \
		rm docker-compose-queue.yaml && \
		rm .example-queue.env && \
		rm .example-db-queue.env && \
		rm .example-db.env && \
		rm entrypoint-queue.sh && \
		rm entrypoint-db.sh && \
		rm entrypoint-db-queue.sh; \
	fi

activation:
	@echo "Activating the environment..."
	pipenv shell

alembicrize:
	@echo "Alembicrizing project..."
	@if [ "yes" = "yes" ]; then \
		pipenv run alembic init project/migrations && \
		mv env.py project/migrations/env.py && \
		mv alembic-local.ini alembic.ini; \
	fi
	@if [ "yes" = "no" ]; then \
		echo "Removing alembic files..." && \
		rm env.py; \
	fi

mkdocs:
	@echo "Creating mkdocs..."
	pipenv run mkdocs new .
	mv mkdocs-local.yml mkdocs.yml
	mv dsa.md docs/dsa.md
	mv api.md docs/api.md

setup: install install-extra structurize dockerize alembicrize mkdocs activation

setup-val: structurize dockerize