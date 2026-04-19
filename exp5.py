print("--- Task List Manager ---\n")
tasks = ["Wakeup", "Breakfast", "College"]

# Display current tasks

print(f"Current Tasks: {tasks}")

print("\n Add new Task ---")
new_task = input("Enter new Task to Add:")
tasks.append(new_task)
print(f"Updated Tasks: {tasks}")

print("\n Remove a Task ---")
remove_task = input("Enter Task to Remove:")
tasks.remove(remove_task)
print(f"Updated Tasks: {tasks}")

print("\n Update a Task ---")
update_task = input("Enter Update Task:")
task_num= int(input("Enter Task Location to Update:"))
tasks.pop(task_num)
tasks.insert(task_num, update_task)

print (f"Updated Tasks: {tasks}")
tasks.sort()
print (f"Sorted Tasks: {tasks}")