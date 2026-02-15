check_list = ["task1","task2","task3","task4","task5","task6","task7"]
complete_list = []
incomplete_list = []
for task in check_list:
    if task in ["task1","task3","task5","task7"]:
        complete_list.append(task)
    else:
        incomplete_list.append(task)

print("Checklist for the day:", check_list)
print("Completed tasks list:", complete_list)
print("Incomplte tasks list:", incomplete_list)