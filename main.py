from os import system, name
import os.path

def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

def removeBlank():
    if todoList[0] == "":
        todoList.pop(0)

def listTodo():
    print("Your Tasky:")
    for i in range (0,len(todoList)):
            print(f"{i}: {todoList[i]}")

path = os.path.expanduser("~/tasky/todoList.txt").replace("\\", "/").replace('"', "")

if not(os.path.isdir(os.path.expanduser("~/tasky"))):
    os.makedirs(os.path.expanduser("~/tasky"))
if not(os.path.isfile(os.path.expanduser(path))):
    todoFile = open(os.path.expanduser(path), "w")

todoFile = open(os.path.expanduser(path), "r")
todoFile = todoFile.read()
todoList = todoFile.split(",")
run = True
removeBlank()

while run == True:
    clear()
    print("Welcome to Tasky!\n")
    action = input("What do you want to do?\n (L)ist: List your Tasky list\n (A)dd: Add to you Tasky list\n (R)emove: Remove item from your Tasky list\n (E)xit: Exit Tasky now\n>").lower().strip()
    if action == "list" or action == "l":
        clear()
        listTodo()
        input("Hit ENTER to continue!")

    elif action == "add" or action == "a":
        clear()
        listTodo()
        add = input("Add your Tasky\n>")
        if not(add) == "":
            todoFile = open(os.path.expanduser(path),"a")
            todoFile.write(f",{add}")
            todoFile = open(os.path.expanduser(path), "r")
            todoFile = todoFile.read()
            todoList = todoFile.split(",")
            removeBlank()
        else:
            clear()
            print("Did not add item to your Tasky because it was blank.")
            input("Hit ENTER to continue!")

    elif action == "remove" or action == "r":
        clear()
        listTodo()
        remove = input("\nWhich Tasky do you wish to remove? Write the number\n>")
        try:
            remove = int(remove)
            try:
                todoList.pop(remove)
                for i in range (0,len(todoList)):
                    print(f"- {todoList[i]}")
                todoFile = open(os.path.expanduser(path), "w")
                for i in range (0,len(todoList)-1):
                    todoFile.write(f"{todoList[i]},")
                todoFile.write(todoList[len(todoList)-1])
                todoFile.close()
            except IndexError:
                clear()
                print("You need to choose a number from the list!")
                input("Hit ENTER to continue!")
        except ValueError:
            clear()
            print("You need to choose a number from the list!")
            input("Hit ENTER to continue!")

    elif action == "exit" or action == "e":
        run = False
        clear()

    else:
        print("You need to choose one of the options!")
        input("Hit ENTER to continue!")