import os
import json

class TaskManager:
    def __init__(self):
        self.file_path = 'tasks.json'
        self.load_tasks()

    def add_task(self):
        task = {
            'name': input('Task Name: ').strip(),
            'due_date': input('Due Date (YYYY-MM-DD): ').strip(),
            'priority': input('Priority (Low, Medium, High): ').strip().capitalize(),
            'duration': input('Duration (hours): ').strip(),
            'completed': False,
            'urgency': input('Is the task Urgent? (yes/no): ').strip().lower() == 'yes',
            'importance': input('Is the task Important? (yes/no): ').strip().lower() == 'yes'
        }
        quadrant = self.determine_quadrant(task['urgency'], task['importance'])
        self.quadrants[quadrant]['tasks'].append(task)
        print(f"Task added to quadrant {quadrant}")

    def determine_quadrant(self, urgency, importance):
        if urgency and importance:
            return 'I'
        elif not urgency and importance:
            return 'II'
        elif urgency and not importance:
            return 'III'
        else:
            return 'IV'

    def edit_task(self):
        name = input('Task name to edit: ')
        for quadrant, data in self.quadrants.items():
            for task in data['tasks']:
                if task['name'] == name:
                    task['name'] = input('New name (leave blank to keep): ') or task['name']
                    task['due_date'] = input('New Due Date (YYYY-MM-DD, leave blank to keep): ') or task['due_date']
                    task['priority'] = input('New Priority (Low, Medium, High, leave blank to keep): ').capitalize() or task['priority']
                    task['duration'] = input('New Duration (hours, leave blank to keep): ') or task['duration']
                    new_urgency = input('Is the task still Urgent? (yes/no): ').strip().lower() == 'yes'
                    new_importance = input('Is the task still Important? (yes/no): ').strip().lower() == 'yes'
                    new_quadrant = self.determine_quadrant(new_urgency, new_importance)
                    if quadrant != new_quadrant:
                        self.quadrants[new_quadrant]['tasks'].append(task)
                        data['tasks'].remove(task)
                        print(f"Task moved to quadrant {new_quadrant}")
                    print("Task updated.")
                    return
        print("Task not found.")

    def list_tasks(self):
        for quadrant, info in self.quadrants.items():
            print(f"\n{quadrant}: {info['description']}")
            for task in info['tasks']:
                status = "Completed" if task['completed'] else "Pending"
                print(f"- {task['name']} due on {task['due_date']} ({task['priority']}, {status})")

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.quadrants, file, indent=4)
        print("Tasks saved.")

    def load_tasks(self):
        try:
            with open(self.file_path, 'r') as file:
                self.quadrants = json.load(file)
        except FileNotFoundError:
            print("Initializing a new task list.")
            self.quadrants = {'I': {'description': 'Urgent and Important', 'tasks': []},
                              'II': {'description': 'Not Urgent but Important', 'tasks': []},
                              'III': {'description': 'Urgent but Not Important', 'tasks': []},
                              'IV': {'description': 'Neither Urgent nor Important', 'tasks': []}}
