from tabulate import tabulate
import sys, csv

def main():
    print("\n--------MENU---------")
    menu_data = [["W" , "Write tasks"], ["D", "Delete tasks"], ["V" ,"View tasks"], ["E" ,"Exit"]]      
    print(tabulate(menu_data, headers= ["Press"], tablefmt="grid"))
    task = input("\n")

    if task == "W":
        write()
    elif task == "D":
        delete()
    elif task == "V":
        view()
    elif task == "E":
        sys.exit("Exiting...")
    else:
        raise ValueError("\033[31mNot an option\033[0m")  # \033[0m is resetting the colors

def write():
    while True:
        print("\nSelect category:\n")
        category_data = [[1, "Personal"], [2, "Work"], [3, "Urgent"], [4, "Entertainment"], [5, "Menu"]]
        print(tabulate(category_data, headers=["S.no", "Category"], tablefmt="grid"))
        category = input("\n")

        if category == "1":  #comparing with strings bcz input returns a string
            write_personal()
        elif category == "2":
            write_work()
        elif category == "3":
            write_urgent()
        elif category == "4":
            write_entertainment()
        elif category == "5":
            main()
        else:
            #here incase you raise a value error, then you'll have to write the print and input statements 
            #again (becz raising an error ends the program)
            print(f"\033[31m\nInvaid: {category} is not an option\033[0m")  
        
def write_personal():
    personal = []
    print("\nPress \"M\" anytime for menu\n")
    while True:
        task = input("Task: ")
        if task == "M":
            main()
        else:
            due_date = input("Due Date/time: ")    
            with open("Personal.csv", "w", newline= '') as file:   # "w" deletes the previous content in csv file, while "a" appen to the end
                writer = csv.DictWriter(file, fieldnames=["Task", "Due Date"])
                writer.writeheader()

                personal.append({"Task": task, "Due Date": due_date})

                for row in personal:  #dictwriter is not iterable, here we are iterating through a list 
                    writer.writerow(row)  # writerow function only writes a dictionary, not a list

def write_work():
    work = []
    print("\nPress \"M\" anytime for menu\n")
    while True:
        task = input("Task: ")
        if task == "M":
            main()
        else:
            due_date = input("Due Date/time: ") 
            with open("Personal.csv", "w", newline= '') as file:   # "w" deletes the previous content in csv file, while "a" appen to the end
                writer = csv.DictWriter(file, fieldnames=["Task", "Due Date"])
                writer.writeheader()

                work.append({"Task": task, "Due Date": due_date})

                for row in work:  #dictwriter is not iterable, here we are iterating through a list 
                    writer.writerow(row)  # writerow function only writes a dictionary, not a list

def write_urgent():
    urgent = []
    print("\nPress \"M\" anytime for menu\n")
    while True:
        task = input("Task: ")
        if task == "M":
            main()
        else:
            due_date = input("Due Date/time: ")    
            with open("Personal.csv", "w", newline= '') as file:   # "w" deletes the previous content in csv file, while "a" appen to the end
                writer = csv.DictWriter(file, fieldnames=["Task", "Due Date"])
                writer.writeheader()

                urgent.append({"Task": task, "Due Date": due_date})

                for row in urgent:  #dictwriter is not iterable, here we are iterating through a list 
                    writer.writerow(row)  # writerow function only writes a dictionary, not a list

def write_entertainment():
    entertainment = []
    print("\nPress \"M\" anytime for menu\n")
    while True:
        task = input("Task: ")
        if task == "M":
            main()
        else:
            due_date = input("Due Date/time: ")    
            with open("Personal.csv", "w", newline= '') as file:   # "w" deletes the previous content in csv file, while "a" appen to the end
                writer = csv.DictWriter(file, fieldnames=["Task", "Due Date"])
                writer.writeheader()

                entertainment.append({"Task": task, "Due Date": due_date})

                for row in entertainment:  #dictwriter is not iterable, here we are iterating through a list 
                    writer.writerow(row)  # writerow function only writes a dictionary, not a list

def delete():
    ...



def view():
    ...

if __name__ == "__main__":
    main()