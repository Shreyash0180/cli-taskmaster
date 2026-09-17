import sys
import os
# Add project root to path so we can import src as a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from colorama import init, Fore, Style
from src.storage import initialize_storage
from src.auth import login, register
from src.tasks import add_task, get_user_tasks, delete_task, update_task_status
from src.analytics import generate_report

init(autoreset=True)

def print_header(text):
    print(f"\n{Fore.CYAN}{Style.BRIGHT}=== {text} ==={Style.RESET_ALL}")

def main_menu():
    print_header("Welcome to CLI TaskMaster")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    return input("Select an option: ")

def user_menu(username):
    while True:
        print_header(f"Dashboard - {username}")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. View Analytics")
        print("6. Logout")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            tasks = get_user_tasks(username)
            if not tasks:
                print(f"{Fore.YELLOW}No tasks found.")
            else:
                for t in tasks:
                    color = Fore.GREEN if t['status'] == 'Completed' else Fore.YELLOW
                    print(f"[{t['task_id']}] {t['title']} (Priority: {t['priority']}) - {color}{t['status']}")
        elif choice == '2':
            title = input("Task title: ")
            desc = input("Task description: ")
            priority = input("Priority (High/Medium/Low): ") or "Medium"
            success, msg = add_task(username, title, desc, priority)
            print(f"{Fore.GREEN if success else Fore.RED}{msg}")
        elif choice == '3':
            task_id = input("Enter Task ID: ")
            status = input("New Status (Completed/Pending): ")
            success, msg = update_task_status(username, task_id, status)
            print(f"{Fore.GREEN if success else Fore.RED}{msg}")
        elif choice == '4':
            task_id = input("Enter Task ID: ")
            success, msg = delete_task(username, task_id)
            print(f"{Fore.GREEN if success else Fore.RED}{msg}")
        elif choice == '5':
            report = generate_report(username)
            print(f"Total Tasks: {report['total']}")
            print(f"Completed: {report['completed']}")
            print(f"Pending: {report['pending']}")
            print(f"Completion Rate: {report['completion_rate']}")
        elif choice == '6':
            print("Logged out.")
            break
        else:
            print(f"{Fore.RED}Invalid option.")

def run():
    initialize_storage()
    while True:
        choice = main_menu()
        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            success, msg = login(username, password)
            print(f"{Fore.GREEN if success else Fore.RED}{msg}")
            if success:
                user_menu(username)
        elif choice == '2':
            username = input("Username: ")
            password = input("Password: ")
            success, msg = register(username, password)
            print(f"{Fore.GREEN if success else Fore.RED}{msg}")
        elif choice == '3':
            print("Exiting. Goodbye!")
            sys.exit(0)
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.")

if __name__ == "__main__":
    run()
