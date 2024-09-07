from tabulate import tabulate
import sys

def main():
    menu_data = [["W" , "Write tasks"], ["D", "Delete tasks"], ["V" ,"View tasks"], ["E" ,"Exit"]]      
    print(tabulate(menu_data, headers= ["Press"], tablefmt="github"))
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
    todo = []
    task = input("Enter task: ")
    todo.append(task)

def delete():
    ...

def view():
    ...

if __name__ == "__main__":
    main()