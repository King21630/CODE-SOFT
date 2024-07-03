class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = "✓" if task["completed"] else "✗"
                print(f"{index}. [{status}] {task['task']}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task deleted.")
        else:
            print("Invalid task index.")

    def save_tasks(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks:
                f.write(f"{task['task']},{task['completed']}\n")
        print(f"Tasks saved to {filename}")

    def load_tasks(self, filename):
        self.tasks = []
        try:
            with open(filename, 'r') as f:
                for line in f:
                    task, completed = line.strip().split(',')
                    self.tasks.append({"task": task, "completed": bool(completed)})
            print(f"Tasks loaded from {filename}")
        except FileNotFoundError:
            print(f"Error: {filename} not found.")

def main():
    todo_list = ToDoList()
    filename = "tasks.txt"

    # Load tasks from file if file exists
    todo_list.load_tasks(filename)

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == '3':
            task_index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == '4':
            task_index = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == '5':
            todo_list.save_tasks(filename)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

    # Save tasks before exiting
    todo_list.save_tasks(filename)

if __name__ == "__main__":
    main()