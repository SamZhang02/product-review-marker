default:
  just --list

install:
  poetry install

run *args:
  poetry run python3 src/{{args}}

main:
  poetry run python3 src/main.py

