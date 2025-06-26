import sys, pathlib; sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
import json
from pathlib import Path
import pytest
from tasks.service import TaskService
from tasks.storage.json_storage import JsonStorage, StorageError


def create_service(tmp_path: Path) -> TaskService:
    storage = JsonStorage(tmp_path / 'tasks.json')
    return TaskService(storage)


def read_file(path: Path):
    with open(path) as f:
        return json.load(f)


def test_add_list_find(tmp_path):
    service = create_service(tmp_path)
    task = service.add_task('Test task')
    assert task.id == 1
    assert task.description == 'Test task'
    assert read_file(tmp_path / 'tasks.json') == [{'id': 1, 'description': 'Test task'}]
    assert service.list_tasks() == [task]
    assert service.find_tasks('test') == [task]


def test_remove(tmp_path):
    service = create_service(tmp_path)
    t1 = service.add_task('A')
    t2 = service.add_task('B')
    assert service.remove_task(t1.id) is True
    assert service.list_tasks() == [t2]
    assert read_file(tmp_path / 'tasks.json') == [{'id': 2, 'description': 'B'}]
    assert service.remove_task(999) is False


def test_corrupted_file(tmp_path):
    path = tmp_path / 'tasks.json'
    path.write_text('invalid json')
    storage = JsonStorage(path)
    with pytest.raises(StorageError):
        storage.load_tasks()


def test_permission_error(tmp_path, monkeypatch):
    path = tmp_path / 'tasks.json'
    storage = JsonStorage(path)
    service = TaskService(storage)
    service.add_task('A')

    def raise_error(*a, **k):
        raise OSError('denied')

    monkeypatch.setattr(path.__class__, 'open', lambda self, mode='r', *a, **k: raise_error() if 'w' in mode else open(self, mode, *a, **k))
    with pytest.raises(StorageError):
        storage.save_tasks([])
