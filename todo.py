import json
import os.path

class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
    def asDictionary(self):
         return self.__dict__

task_list = []

def save_file():
    
    array_as_dict = []
    #to_write = json.dumps(task_list)
    for i in task_list:
        array_as_dict.append(i.asDictionary())
    with open("tasks.json", "w") as file_object:
             json.dump(array_as_dict, file_object)


def load_file():
    exists = os.path.exists("tasks.json")
    if exists == False:
        return
    else:
        with open("tasks.json","r") as file_object:
            old = json.load(file_object)
        for x in old:
            task_list.append(Task(x['name'], x['priority']))


def print_list():
    print("Current List:\n")
    for task in task_list:
        print(str(task_list.index(task) + 1) + ". " + task.name + ", Priority: " + task.priority)

load_file()
print("Welcome to your TODO list\n")


while True:
    
    print_list()
    print(" ")
    print("Main Menu\n")
    print("Press 1 to add task")
    print("Press 2 to delete task")
    print("Press 'q' to quit app\n")
    
    print(" ")
    choice = input("What would you like to do? ").lower()
    print(" ")
    
    if choice == 'q':
        save_file()
        print("Goodbye\n")
        break

    elif choice == '1':
        task = input("Enter task name: ")
        priority = input("Enter priority: ")
        task_list.append(Task(task,priority))
        print("Task succesfully added!\n")
   
    elif choice == '2':
        dTask = int(input("Enter the number of the task you would like to delete: ")) - 1
        del task_list[dTask]
        print("Task deleted!\n")
    
    else:
        print(" ")
        print('INVALID INPUT, PLEASE TRY AGAIN')
        
        

