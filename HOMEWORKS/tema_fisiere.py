import datetime

# POSSIBLE_CATEGORIES = ["curs", "cumparaturi", "munca", "cadouri"]


def insert_categories():
    category = input("Enter your task category: ")
    while True:
        if category.upper() == "STOP":
            break

        # if category in POSSIBLE_CATEGORIES:
        with open("categories.csv", "a") as f:
            f.write(category + "\n")

        category = input("Enter your task category: ")


def get_data_from_csv_file(file_name):
    with open(file_name, "r") as f:
        data = f.readlines()
    data = [elem[:-1].split(',') for elem in data]

    return data


def insert_tasks():
    valid = True
    while True:
        task = input("Enter your task: (after finishing, type 'STOP') ")
        if task.upper() == "STOP":
            break
        deadline = input("Enter deadline (format DD.MM.YYYY HH:MM): ")
        try:
            deadline = datetime.datetime.strptime(deadline, "%d.%m.%Y %H:%M")
            now = datetime.datetime.now()
            if deadline < now:
                print("Incorrect date")
                valid = False
        except:
            print("Incorrect date")
            valid = False

        person = input("Who's responsable for the task? ")
        category = input("Category for task: ")
        with open("categories.csv", "r") as f:
            possible_categories = f.readlines()
            # new_list = []
            # for i in possible_categories:
            #     new_list.append(i[:-1])
            # possible_categories = new_list
            possible_categories = [i[:-1] for i in possible_categories]
        if category not in possible_categories:
            print("Category does not exist")
            valid = False

        if valid:
            with open("tasks.csv", "a") as f:
                f.write(f"{task},{deadline},{person},{category}\n")

        else:
            print("Your task wasn't added to the file")


def list_tasks():
    tasks = get_data_from_csv_file("tasks.csv")
#     with open("tasks.csv", "r") as f:
#         tasks = f.readlines()
    # tasks = [i[:-1] for i in tasks]
    # res_task = []
    # for elem in tasks:
    #     res_task.append(elem.split(","))

    # tasks = [elem[:-1].split(',') for elem in tasks]

    tasks = sorted(tasks, key=lambda x: x[3])
    print(tasks)

# --------


menu_options = {

    1: 'Insert Categories',
    2: 'Insert tasks',
    3: 'List tasks',
    4: 'TASK: Ascending Sort',
    5: 'TASK: Descending Sort',
    6: 'DATE: Ascending Sort',
    7: 'DATE: Descending Sort',
    8: 'RESPONSABLE PERSON: Ascending sort',
    9: 'RESPONSABLE PERSON: Descending sort',
    10: 'CATEGORY: Ascending Sort',
    11: 'CATEGORY: Descending Sort',
    12: 'EXIT'
}


def print_menu():
    for key in menu_options:
        print(key, '--', menu_options[key])


def option1():
    print("Handle option 'Insert Categories")
    insert_categories()


def option2():
    print("Handle option 'Insert Tasks"'')
    insert_tasks()


def option3():
    print('Handle option "List Tasks"')
    list_tasks()


def option4():
    print('Handle option "TASK: Ascending Sort"')
    ascending_task()


def option5():
    print('Handle option "TASK: Descending Sort"')
    descending_task()


def option6():
    print('Handle option "DATE: Ascending Sort"')
    ascending_data()


def option7():
    print('Handle option "Date: Descending Sort"')
    descending_data()


def option8():
    print('Handle option "RESPONSABLE PERSON: Ascending sort"')
    ascending_responsable_person()


def option9():
    print('Handle option "RESPONSABLE PERSON: Descending sort"')
    descending_responsable_person()


def option10():
    print('Handle option "CATEGORY: Ascending Sort"')
    ascending_category()


def option11():
    print('Handle option "CATEGORY: Descending Sort"')
    descending_category()


def option12():
    print("EXIT")


def handle_menu():
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
            # printu
            # call functia care face treaba
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            option6()
        elif option == 7:
            option7()
        elif option == 8:
            option8()
        elif option == 9:
            option9()
        elif option == 10:
            option10()
        elif option == 11:
            option11()
        elif option == 12:
            option12()

            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 12.')


def bubble_sort(tasks, index):
    for i in range(0, len(tasks)-1):
        for j in range(i+1, len(tasks)):
            if tasks[i][index] > tasks[j][index]:
                tasks[i], tasks[j] = tasks[j], tasks[i]
    return tasks


def ascending_task():
    tasks = get_data_from_csv_file("tasks.csv")
    # tasks.sort()
    tasks = bubble_sort(tasks, 0)
    print(tasks)


def descending_task():
    tasks = get_data_from_csv_file("tasks.csv")
    # tasks.sort(reverse=True)
    tasks = list(reversed(bubble_sort(tasks, 0)))
    print(tasks)


def ascending_data():
    tasks = get_data_from_csv_file("tasks.csv")
    tasks = bubble_sort(tasks, 1)

    # def second_elem(elem):
    #     return elem[1]

#    data.sort(key = second_elem)
#    data.sort(key=lambda x: x[1])
#     for i in range(0, len(tasks)-1):
#         for j in range(i+1, len(tasks)):
#             if tasks[i][1] > tasks[j][1]:
#                 tasks[i], tasks[j] = tasks[j], tasks[i]

    print(tasks)


def descending_data():
    tasks = get_data_from_csv_file("tasks.csv")
    tasks = bubble_sort(tasks, 1)
    tasks = list(reversed(tasks))
    print(tasks)


def ascending_responsable_person():
    tasks = get_data_from_csv_file("tasks.csv")
    tasks = bubble_sort(tasks, 2)
    print(tasks)


def descending_responsable_person():
    tasks = get_data_from_csv_file("tasks.csv")
    tasks = bubble_sort(tasks, 2)
    tasks = list(reversed(tasks))
    print(tasks)


def ascending_category():
    tasks = get_data_from_csv_file("tasks.csv")
    tasks = bubble_sort(tasks, 3)
    print(tasks)


def descending_category():
    tasks = get_data_from_csv_file("tasks.csv")
    tasks = bubble_sort(tasks, 3)
    tasks = list(reversed(tasks))
    print(tasks)



def main():
    print_menu()
    handle_menu()


if __name__ == "__main__":
    main()
