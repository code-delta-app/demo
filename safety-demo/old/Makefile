.PHONY: test lint build clean

PY ?= python3

test:
	$(PY) -m pytest -q tests

lint:
	$(PY) -m pyflakes helpdesk tests || true
	gofmt -l cli

build:
	$(PY) -c "import helpdesk; print('helpdesk', helpdesk.__version__)"
	cd cli && go build ./...

clean:
	find . -name '__pycache__' -type d -prune -exec rm -rf {} +
	find . -name '*.pyc' -delete
	rm -f cli/main cli/cli
