from typing import List
from .domain import Task, add_task as add_task_func, remove_task as remove_task_func, find_tasks as find_tasks_func
from .storage.storage import TaskStorage


class TaskService:
    """Business logic for task management using provided storage."""

    def __init__(self, storage: TaskStorage):
        self._storage = storage
        self._tasks: List[Task] = storage.load_tasks()

    def _save(self):
        self._storage.save_tasks(self._tasks)

    def add_task(self, description: str) -> Task:
        self._tasks = add_task_func(self._tasks, description)
        self._save()
        return self._tasks[-1]

    def remove_task(self, task_id: int) -> bool:
        new_tasks = remove_task_func(self._tasks, task_id)
        if len(new_tasks) == len(self._tasks):
            return False
        self._tasks = new_tasks
        self._save()
        return True

    def list_tasks(self) -> List[Task]:
        return list(self._tasks)

    def find_tasks(self, keyword: str) -> List[Task]:
        return find_tasks_func(self._tasks, keyword)
