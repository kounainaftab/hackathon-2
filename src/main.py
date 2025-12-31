#!/usr/bin/env python3
"""
Main entry point for the Todo Python Console App.

This application provides a command-line interface for managing tasks.
It follows the specifications outlined in the project constitution and specs.
"""

from todo import TodoManager
from commands.add_command import add_task_with_options
from commands.update_command import update_task_with_options
from commands.list_command import list_tasks_with_options
from commands.complete_command import complete_task_with_recurrence


def main():
    """Main function to run the Todo application."""
    print("Welcome to the Todo Python Console App!")
    print("Type 'help' for available commands or 'exit' to quit.")

    app = TodoManager()
    
    while True:
        try:
            command = input("\n> ").strip().split()
            
            if not command:
                continue
                
            cmd = command[0].lower()
            
            if cmd == "exit":
                print("Goodbye!")
                break
            elif cmd == "help":
                print_help()
            elif cmd == "add":
                # Use the new add command module
                add_task_with_options(app, command[1:])
            elif cmd == "list":
                app.list_tasks()
            elif cmd == "delete":
                if len(command) != 2:
                    print("Usage: delete <id>")
                else:
                    try:
                        task_id = int(command[1])
                        app.delete_task(task_id)
                    except ValueError:
                        print("Invalid task ID. Please provide a number.")
            elif cmd == "update":
                # Use the new update command module
                update_task_with_options(app, command[1:])
            elif cmd == "complete":
                # Use the new complete command module
                complete_task_with_recurrence(app, command[1:])
            elif cmd == "list":
                # Use the new list command module
                list_tasks_with_options(app, command[1:])
            else:
                print(f"Unknown command: {cmd}. Type 'help' for available commands.")
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break


def print_help():
    """Print available commands and their usage."""
    print("\nAvailable commands:")
    print("  add <title> [-d description] [-p priority] [-t tags] [--due-date YYYY-MM-DD] [--recurrence daily|weekly|monthly]")
    print("                                           - Add a new task with optional due date and recurrence")
    print("  delete <id>                              - Delete a task by ID")
    print("  update <id> [-t title] [-d description] [-p priority] [--tags tag1 tag2...] [--due-date YYYY-MM-DD] [--recurrence daily|weekly|monthly]")
    print("                                           - Update a task's properties")
    print("  list                                     - List all tasks")
    print("  list --search <keyword>                  - Search tasks by keyword")
    print("  list --filter status=<pending/completed> - Filter tasks by completion status")
    print("  list --filter priority=<High/Medium/Low> - Filter tasks by priority")
    print("  list --filter tag=<tagname>              - Filter tasks by tag")
    print("  list --filter due-status=<overdue/due-today/upcoming> - Filter tasks by due date status")
    print("  list --sort <priority/title/created/due-date> - Sort tasks by specified field")
    print("  list --desc                              - Use with --sort for descending order")
    print("  complete <id>                            - Mark a task as complete/incomplete (creates new instance for recurring tasks)")
    print("  help                                     - Show this help message")
    print("  exit                                     - Exit the application")


if __name__ == "__main__":
    main()