from datetime import datetime

class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    def __str__(self):
        return f"{self.priority} | {self.timestamp} | {self.description}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority):
        new_task = Task(description=task, priority=priority)
        self.tasks.append(new_task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.priority} | {task.timestamp}  | {task.description}\n")

    def filter_tasks(self, selected_priority):
        return [task for task in self.tasks if task.priority == selected_priority] 
    
    def sort_tasks(self, key='priority'):
        if key == 'priority':
            self.tasks.sort(key=lambda x: x.priority)
        elif key == 'timestamp':
            self.tasks.sort(key=lambda x: datetime.strptime(x.timestamp, "%d-%m-%Y %H:%M:%S"))

    def read_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                self.tasks = []
                for line in lines:
                    parts = line.strip().split(' | ')
                    if len(parts) == 3:
                        priority, timestamp, description = parts
                        self.tasks.append(Task(description=description, priority=priority))
                    else:
                        print("Error: Invalid line format in the file.")
        except FileNotFoundError:
            print("Error: File not found.")