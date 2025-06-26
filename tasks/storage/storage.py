from abc import ABC, abstractmethod
from typing import List
from ..domain import Task


class StorageError(Exception):
    """Raised when persistence layer encounters an error."""


class TaskStorage(ABC):
    """Abstract storage interface."""

    @abstractmethod
    def load_tasks(self) -> List[Task]:
        pass

    @abstractmethod
    def save_tasks(self, tasks: List[Task]) -> None:
        pass
