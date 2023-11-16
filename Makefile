format:
	pre-commit run --all-files

test:
	pytest -vvv --cov=src tests/
