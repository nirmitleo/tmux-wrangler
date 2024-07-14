
#!/bin/bash

run_init() {
  direnv allow
}

run_test() {
  _with_test_env
  poetry run test "${@}"
}

run_dev.reset() {
  rm -Rf .venv
}

run_deps() {
  poetry install
}

run_lint() {
    poetry run lint
}

fn_exists() { declare -F "$1" >/dev/null; }

run() {
  local cmd=$1
  shift
  local fn="run_$cmd"

  if fn_exists $fn; then
    $fn "${@}"
  else
    poetry run "$cmd" "${@}"
  fi
}

run "${@}"