import argparse
from pathlib import Path
from .service import TaskService
from .storage.json_storage import JsonStorage


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Task manager")
    sub = parser.add_subparsers(dest="command")

    add_p = sub.add_parser("add", help="add a task")
    add_p.add_argument("description")

    rm_p = sub.add_parser("remove", help="remove a task")
    rm_p.add_argument("task_id", type=int)

    sub.add_parser("list", help="list tasks")

    find_p = sub.add_parser("find", help="find tasks")
    find_p.add_argument("keyword")

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    storage = JsonStorage(Path("tasks.json"))
    service = TaskService(storage)

    if args.command == "add":
        task = service.add_task(args.description)
        print(f"Added task {task.id}: {task.description}")
    elif args.command == "remove":
        if service.remove_task(args.task_id):
            print(f"Removed task {args.task_id}")
        else:
            print(f"Task {args.task_id} not found")
    elif args.command == "list":
        for task in service.list_tasks():
            print(f"{task.id}: {task.description}")
    elif args.command == "find":
        for task in service.find_tasks(args.keyword):
            print(f"{task.id}: {task.description}")
    else:
        parser.print_help()
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
