from task_manager import TaskManager

def main():
    manager = TaskManager()
    while True:
        print("\n1. Add Task\n2. Edit Task\n3. Delete Task\n4. List Tasks\n5. Save Tasks\n6. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            manager.add_task()
        elif choice == '2':
            manager.edit_task()
        elif choice == '3':
            manager.delete_task()
        elif choice == '4':
            manager.list_tasks()
        elif choice == '5':
            manager.save_tasks()
        elif choice == '6':
            break
        else:
            print("Invalid option. Please choose a valid number.")

if __name__ == "__main__":
    main()
