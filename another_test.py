
# index = 0
# file = open("test.txt", "r", encoding="utf-8")
#
# for i in file:
#     index += 1
#
# print(index)



def show_task(task_num):
    with open("task.txt", "r", encoding="utf-8") as file:
        mylist = file.read().splitlines()
        if 0 < task_num <= len(mylist):
            print(mylist[task_num - 1])
        else:
            print("Такой задачи не существует.")

def add_task(task_text):
    with open("task.txt", "a", encoding="utf-8") as file:
        file.write(task_text + "\n")