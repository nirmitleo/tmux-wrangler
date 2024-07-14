from scripts.base import _call

files = ["src/", "scripts/", "migrations/"]


def lint() -> None:
    _call("ruff check", files)


def lint_fix() -> None:
    files.append("--fix")
    _call("ruff check", files)


def fix() -> None:
    _call("isort", files)

    _call("ruff format", files)


def type_check() -> None:
    _call("mypy --explicit-package-bases", files)
