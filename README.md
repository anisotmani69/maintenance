# Maintenance Task Manager

This project provides a simple CLI tool to manage tasks stored in a JSON file. It demonstrates a refactored architecture with separation of concerns and unit tests.

## Architecture

- **tasks.domain** – pure functions and dataclass representing tasks.
- **tasks.storage** – abstraction of the persistence layer with a JSON implementation.
- **tasks.service** – business logic manipulating tasks through the storage.
- **tasks.cli** – command line interface using `argparse`.

## Usage

```
python -m tasks.cli add "Buy milk"
python -m tasks.cli list
python -m tasks.cli remove 1
python -m tasks.cli find milk
```

Tasks are stored in `tasks.json` in the current directory by default.

## Tests

Run all tests with:

```
pytest
```
