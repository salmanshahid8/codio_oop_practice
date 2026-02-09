sync:
	uv sync

format:
	uvx ruff format . --no-cache --respect-gitignore --config pyproject.toml
# --quiet for not detail or --verbose for detail

lint:
	uvx ruff check . --fix --no-cache --respect-gitignore --config pyproject.toml --exit-zero

type_check:
	uvx ty check --exit-zero

security_check:
	uvx bandit -r src/ --configfile pyproject.toml --exit-zero

build:
	uv build --clear --upgrade --quiet

clean:
	uvx ruff clean && uv clean

# test:
# 	python -m pytest -vv test_hello.py
	
all: sync format lint type_check security_check clean