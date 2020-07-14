install:
	pip install --upgrade pip
	pip install -r requirements.txt

migrate:
	python pyuser/db/migrate.py

tests:
	pytest tests.py