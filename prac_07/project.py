class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        date_format = self.start_date.strftime("%d/%m/%Y")
        return f"  {self.name}, start: {date_format}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, {self.completion_percentage}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return  self.start_date > other.start_date