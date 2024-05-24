# data_model.py


class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def __str__(self):
        return f"{self.title} - {self.description} - Due: {self.due_date} - {'Completed' if self.completed else 'Not completed'}"
