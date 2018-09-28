import json
import datetime
import os.path

pool_tables = []

class PoolTable:
    def __init__(self, id_number, occupied, start_time, end_time):
        self.id_number = id_number
        self.occupied = occupied
        self.end_time = end_time
        self.start_time = start_time
    
    def isOccupied(self):
        if self.occupied == False:
            return "UNOCCUPIED"
        else:
            return "OCCUPIED"
            
    def asDictionary(self):
        return self.__dict__

def load_file():
    exists = os.path.exists("pooltables.json")
    if exists == False:
        initialize_tables()
        return
    else:
        with open("pooltables.json","r") as file_object:
            try:
                old = json.load(file_object)
            except ValueError:
                initialize_tables()
                return
        for x in old:
            pool_tables.append(PoolTable(x['id_number'], x['occupied'], x['start_time'], x['end_time']))


def add_to_report(num):
    with open("pool_table_report.txt","a") as report:
        report.write(str("Table " + str(pool_tables[num].id_number) + ": " + str(pool_tables[num].start_time) + " - " + str(pool_tables[num].end_time) + "\n"))
        

def save_file():
    array_as_dict = []
    for i in pool_tables:
        array_as_dict.append(i.asDictionary())
    with open("pooltables.json", "w") as file_object:
             json.dump(array_as_dict, file_object, indent = 2)

def occupy_table(num):
    if pool_tables[num].occupied == False:
        pool_tables[num].occupied = True
        pool_tables[num].start_time = str(datetime.datetime.now().strftime("%H:%M"))
    else:
        print("ERROR TABLE IS ALREADY OCCUPIED")
    return

def open_table(num):
    if pool_tables[num].occupied == True:
        pool_tables[num].occupied = False
        pool_tables[num].end_time = str(datetime.datetime.now().strftime("%H:%M"))
        add_to_report(num)
        save_file()
    else:
        print("ERROR TABLE IS ALREADY OPENED")
    return

def print_occupied_tables():
    for table in pool_tables:
        if table.occupied == True:
            print("Table " + str(table.id_number) + ": " + table.isOccupied() + " Time Occupied: " + str(table.start_time) + " - " + str(datetime.datetime.now().strftime("%H:%M")))
    print(" ")

def print_unoccupied_tables():
    for table in pool_tables:
        if table.occupied == False:
            print("Table " + str(table.id_number) + ": " + table.isOccupied())
    print(" ")

def initialize_tables():
    del pool_tables[:]
    for i in range(1,13):
        pool_tables.append(PoolTable(i, False, None, None))

def print_tables():
    for table in pool_tables:
        if table.occupied == False:
            print("Table " + str(table.id_number) + ": " + table.isOccupied())
        else:
            print("Table " + str(table.id_number) + ": " + table.isOccupied() + " Time Occupied: " + str(table.start_time) + " - " + str(datetime.datetime.now().strftime("%H:%M")))
    print(" ")

print(" ")
print("Welcome to the UC-Underground Pool Table Management App")
load_file()

while True:
    print(" ")
    print("Menu:\n")
    print("Press 'V' to view status of all pool tables")
    print("Press 'U' to show only UNOCCUPIED tables")
    print("Press 'O' to show only OCCUPIED tables")
    print("Press 'R' to reserve a table")
    print("Press 'L' to mark a table as UNOCCUPIED")
    print("Press 'X' to reset all tables")
    print("Press 'Q' to exit application")
    print(" ")

    choice = input("What would you like to do? ").lower()
    print(" ")

    if choice == 'q':
        print("Goodbye\n")
        save_file()
        break

    elif choice == 'v':
        print_tables()

    elif choice == 'x':
        confirm = input("Are you sure you eant to reset all tables? y/n: ").lower()
        if confirm == 'y':
            initialize_tables()
        elif confirm == 'n':
            pass

    elif choice == 'u':
        print_unoccupied_tables()

    elif choice == 'o':
        print_occupied_tables()

    elif choice == 'r':
        print_unoccupied_tables()
        try:
            table_num = int(input("Enter the table number to reserve: ")) - 1
            occupy_table(table_num)
            print(" ")
        except ValueError:
            print(" ")
            print("ERROR, NOT AN INTEGER")

    elif choice == 'l':
        print_occupied_tables()
        try:
            table_num = int(input("Enter the table number to mark as open: ")) - 1
            open_table(table_num)
            print(" ")
        except ValueError:
            print(" ")
            print("ERROR, NOT AN INTEGER")

    else:
        print(" ")
        print("Invalid Input, please try again.\n")
        
