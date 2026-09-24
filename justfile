#!/usr/bin/env just --justfile

# Default recipe to display help
default:
    @just --list

# Initialize the project
init:
    direnv allow

# Run tests
test *ARGS:
    poetry run test {{ARGS}}

# Reset the virtual environment
reset:
    rm -Rf .venv

# Install dependencies
deps:
    poetry install

# Run linter
lint:
    poetry run lint

# Build standalone executable
build:
    poetry run pyinstaller --name=tmuxw --onefile src/cli/cli.py

# Install the built executable to system
install:
    sudo cp dist/tmuxw /usr/local/bin

# Run any poetry command
run CMD *ARGS:
    poetry run {{CMD}} {{ARGS}}