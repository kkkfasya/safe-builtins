.PHONY: lint format fmt test

lint:
	uv run ruff check .

format:
	uv run ruff format .

fmt: format

test:
	uv run pytest

