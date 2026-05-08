class Task:
    tasks = []

    def __init__(self, name, time, status):
        self.name = name
        self.time = time
        self.status = status

    @classmethod
    def addTask(cls, name, time, status):
        task = cls(name, time, status)
        cls.tasks.append(task)
        return task

    @classmethod
    def getTasks(cls):
        return cls.tasks

    @classmethod
    def removeTask(cls, index):
        return cls.tasks.pop(index)

    def __str__(self):
        return f"Task: {self.name} | Time (hrs): {self.time} | Status: {self.status}"

    def __repr__(self):
        return self.__str__()


class Menu:
    def __init__(self):
        self.option = 0

    def ui(self):
        while self.option != 5:
            print("\n------------------------------------")
            print("Task Manager")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Remove Task")
            print("4. Edit Tasks")
            print("5. Exit")

            choice = input("Choose an option: ")
            if not choice.isdigit():
                print("Enter a valid integer.")
                continue

            self.option = int(choice)
            if self.option == 1:
                self.addTaskUi()
            elif self.option == 2:
                self.viewTasks()
            elif self.option == 3:
                self.removeTaskUi()
            elif self.option == 4:
                self.editTasks()
            elif self.option == 5:
                print("Exiting...")
            else:
                print("Enter a valid option.")

    def addTaskUi(self):
        name = input("Task name: ").strip()
        if not name:
            print("Task name cannot be empty.")
            return

        time_input = input("Time in hours: ")
        if not time_input.isdigit():
            print("Time must be a valid integer.")
            return

        status = input("Status: ").strip()
        if not status:
            status = "Pending"

        Task.addTask(name, int(time_input), status)
        print("Task added successfully.")

    def viewTasks(self):
        tasks = Task.getTasks()
        if not tasks:
            print("No tasks available.")
            return

        print("\nCurrent Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index}. {task}")
        



    def removeTaskUi(self):
        tasks = Task.getTasks()
        if not tasks:
            print("\n")
            print("No tasks available to remove.")
            return

        self.viewTasks()

        choice = input("Enter the task number to remove: ")
        if not choice.isdigit():
            print("\n")
            print("Enter a valid integer.")
            return

        index = int(choice)
        if index < 0 or index >= len(tasks):
            print("\n")           
            print("Invalid task number.")
            return

        removed = Task.removeTask(index)
        print("\n")
        print(f"Removed task: {removed.name}")
    
    def editTasks(self):
        tasks = Task.getTasks()
        self.viewTasks()

        if not tasks:
            return
        choice = input("Enter the task number to edit: ")

        if not choice.isdigit():
            print("\n")
            print("Enter a valid integer")

        index = int(choice) 
        if index < 0 or index >= len(tasks):
            print("\n")
            print("Invalid task number.")
            return
        
        print(tasks[index])
        
        choice = input("Enter what you want to edit: ")

        if not choice.isalpha():
            print("\n")
            print("Enter a valid field name:")
            self.editTasks()
        
        choice = choice.lower()
        if choice == "task":
            new_name = input("Enter new task name: ").strip()
            if not new_name:
                print("\n")
                print("Task name cannot be empty.")
                self.editTasks()
            tasks[index].name = new_name
            print("\n")
            print("Task name updated successfully.")
        elif choice == "time":
            new_time = input("Enter new time in hours: ").strip()
            if not new_time.isdigit():
                print("\n")
                print("Time must be a valid integer.")
                self.editTasks()
            tasks[index].time = int(new_time)
            print("\n")
            print("Task time updated successfully.")
        elif choice == "status":
            new_status = input("Enter new status: ").strip()
            if not new_status:
                tasks[index].status = "Pending"
            tasks[index].status = new_status
            print("\n")
            print("Task status updated successfully.")
        else:
            print("\n")
            print("Invalid field name. Please enter 'task', 'time', or 'status'.")
            self.editTasks()
        self.viewTasks()



def main():
    menu = Menu()
    menu.ui()


if __name__ == "__main__":
    main()
