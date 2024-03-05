.PHONY: install

install:
	@echo "Installing dependencies..."
	poetry install

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

