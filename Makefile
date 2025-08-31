.PHONY: lint format fmt test all

lint:
	uv run ruff check .

format:
	uv run ruff format .

fmt: format

test:
	uv run pytest

all: lint format test
