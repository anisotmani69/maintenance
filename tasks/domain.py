from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Task:
    id: int
    description: str


def next_task_id(tasks: List['Task']) -> int:
    """Return the next task id based on current tasks."""
    return max((task.id for task in tasks), default=0) + 1


def add_task(tasks: List['Task'], description: str) -> List['Task']:
    """Return a new task list with a task added."""
    task = Task(id=next_task_id(tasks), description=description)
    return tasks + [task]


def remove_task(tasks: List['Task'], task_id: int) -> List['Task']:
    """Return a new task list with the task removed if present."""
    return [t for t in tasks if t.id != task_id]


def find_tasks(tasks: List['Task'], keyword: str) -> List['Task']:
    """Return tasks containing keyword."""
    keyword = keyword.lower()
    return [t for t in tasks if keyword in t.description.lower()]
