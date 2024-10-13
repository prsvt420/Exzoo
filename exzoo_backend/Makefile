run:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py makemigrations && poetry run python manage.py migrate
dumpdata:
	poetry run python -Xutf8 manage.py dumpdata --indent=2 products.Tag -o fixtures/tag.json
	poetry run python -Xutf8 manage.py dumpdata --indent=2 products.Category -o fixtures/category.json
	poetry run python -Xutf8 manage.py dumpdata --indent=2 products.Product -o fixtures/product.json
	poetry run python -Xutf8 manage.py dumpdata --indent=2 -o fixtures/db.json
loaddata:
	poetry run python -Xutf8 manage.py loaddata fixtures/db.json