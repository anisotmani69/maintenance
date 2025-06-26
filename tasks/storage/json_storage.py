import json
from pathlib import Path
from typing import List
from .storage import TaskStorage, StorageError
from ..domain import Task


class JsonStorage(TaskStorage):
    def __init__(self, path: Path):
        self.path = Path(path)

    def load_tasks(self) -> List[Task]:
        try:
            with self.path.open('r') as f:
                data = json.load(f)
                return [Task(**item) for item in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as exc:
            raise StorageError('Corrupted storage file') from exc

    def save_tasks(self, tasks: List[Task]) -> None:
        try:
            with self.path.open('w') as f:
                json.dump([task.__dict__ for task in tasks], f)
        except OSError as exc:
            raise StorageError('Cannot write storage file') from exc
