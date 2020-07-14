_before_install:
	pip install --upgrade pip

install:
	make _before_install
	pip install .

install-test:
	make _before_install
	pip install .[test]

migrate:
	python pyuser/db/migrate.py

tests:
	pytest tests.py