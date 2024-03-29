.PHONY: install

install:
	@echo "Installing dependencies..."
	poetry install

.PHONY: lint

lint:
	@echo "Running linters..."
	poetry run flake8 brain_games
	poetry run isort --check-only brain_games
	poetry run black --check brain_games

.PHONY: test

test:
	@echo "Running tests..."
	poetry run pytest

.PHONY: build

build:
	@echo "Building the package..."
	poetry build

.PHONY: publish

publish:
	@echo "Executing publish dry run..."
	poetry publish --dry-run

.PHONY: package-install

package-install:
	@echo "Installing the package..."
	python3 -m pip install --user dist/*.whl

.PHONY: build-package

build-package: build publish