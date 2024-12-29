import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from datetime import datetime
from Task import TaskManager

def add_task():
    task = entry.get()
    priority = priority_var.get()
    if task:
        task_manager.add_task(task, priority)
        entry.delete(0, tk.END)
        update_tasks()

def remove_task():
    try:
        index = int(entry_remove.get()) - 1
        task_manager.remove_task(index)
        update_tasks()
    except ValueError:
        print("Error. ValueError.")
        pass

def update_tasks():
    tasks_text.delete(1.0, tk.END)
    for i, task in enumerate(task_manager.tasks, start=1):
        formatted_task = f"{i}. {task.priority} | {task.timestamp} | Task: {task.description} \n"
        tasks_text.insert(tk.END, formatted_task)

def save_to_file():
    filename = "E:\projekty_git\Computer_Science\year2\year2_Python\save.txt"
    task_manager.save_tasks(filename)
    update_tasks()

def read_from_file():
    filename = "E:\projekty_git\Computer_Science\year2\year2_Python\save.txt"
    task_manager.read_from_file(filename)
    update_tasks()

def update_scroll_region(event):
    tasks_text.yview_moveto(1)
    tasks_text.after(10, lambda: tasks_text.yview_moveto(0))

def update_filtered_tasks():
    selected_priority = selected_filter_var.get()
    if selected_priority == "All":
        update_tasks()
    else:
        filtered_tasks = task_manager.filter_tasks(selected_priority)
        update_display(filtered_tasks)

def update_display(tasks):
    tasks_text.delete(1.0, tk.END)
    for i, task in enumerate(tasks, start=1):
        formatted_task = f"{i}. {task.priority} | {task.timestamp} | Task: {task.description} \n"
        tasks_text.insert(tk.END, formatted_task)

def update_sorted_tasks():
    selected_sort_criteria = selected_sort_var.get().lower()
    task_manager.sort_tasks(key=selected_sort_criteria)
    update_tasks()


root = tk.Tk()
root.title("Task Manager")

task_manager = TaskManager()

main_frame = ctk.CTkFrame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

#pasek z logo
sidebar_frame = ctk.CTkFrame(main_frame, width=40, corner_radius=50, fg_color='white')  
sidebar_frame.grid(row=0, column=0, sticky="nsew")
sidebar_frame.grid_rowconfigure(0, weight=0)
sidebar_frame.pack(fill=tk.BOTH, expand=True)

logo_img = ctk.CTkImage(light_image=Image.open('E:\projekty_git\Computer_Science\year2\year2_Python\img_star.jpg').resize((60, 60)))
save_img = ctk.CTkImage(light_image=Image.open('E:\projekty_git\Computer_Science\year2\year2_Python\img_save.jpg').resize((60, 60)))
read_img = ctk.CTkImage(light_image=Image.open('E:\projekty_git\Computer_Science\year2\year2_Python\img_read.jpg').resize((60, 60)))

logo_label = ctk.CTkLabel(sidebar_frame, text="  T a s k   M a n a g e r", text_color="#5f246b", fg_color="white", image=logo_img, font=ctk.CTkFont(size=20, weight="bold"), compound="left")
logo_label.grid(row=0, column=0, padx=20, pady=(10, 10), sticky='nsew', columnspan=50)
logo_label.pack(fill=tk.BOTH, expand=True)

#gora
top_frame = ctk.CTkFrame(root)
top_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True) 

#wpisywanie
entry = tk.Entry(top_frame, width=40)
entry.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)

#piorytet
priority_var = tk.StringVar(root)
priority_var.set("Priority") 

priority_optionmenu = tk.OptionMenu(top_frame, priority_var, "Low *    ", "Medium **", "High *** ")
priority_optionmenu.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)

#guzik dodawanie
add_button = ctk.CTkButton(top_frame, text="*₊˚Add Task*₊˚", command=add_task, fg_color="#5f246b")
add_button.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)

#srodek
middle_frame = ctk.CTkFrame(root)
middle_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

#tablica wpisywanie
tasks_text = tk.Text(middle_frame, height=10, width=50)
tasks_text.columnconfigure(0, minsize=30) 
tasks_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#pasek przewijaniae
scrollbar = tk.Scrollbar(middle_frame, command=tasks_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tasks_text.config(yscrollcommand=scrollbar.set)

tasks_text.bind("<Configure>", update_scroll_region)

#dol
frame_filter = ctk.CTkFrame(root)
frame_filter.pack(padx=10, pady=5, fill=tk.BOTH, expand=True) 

#filtrowanie
selected_filter_var = tk.StringVar(root)
selected_filter_var.set("All") 

filter_optionmenu = tk.OptionMenu(frame_filter, selected_filter_var, "All", "Low *    ", "Medium **", "High *** ")
filter_optionmenu.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=False) 

filter_button = ctk.CTkButton(frame_filter, text="Filter Tasks", command=lambda: update_filtered_tasks())
filter_button.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True) 

#sortowanie
frame_sorting = ctk.CTkFrame(root)
frame_sorting.pack(padx=10, pady=5, fill=tk.BOTH, expand=True) 

selected_sort_var = tk.StringVar(root)
selected_sort_var.set("Timestamp")  

sort_optionmenu = tk.OptionMenu(frame_sorting, selected_sort_var, "Timestamp", "Priority")
sort_optionmenu.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=False)

sort_button = ctk.CTkButton(frame_sorting, text="Sort Tasks", command=lambda: update_sorted_tasks())
sort_button.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)

#dolny pasek
bottom_frame = ctk.CTkFrame(root)
bottom_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True) 

#guzik zapisywanie#
save_button = ctk.CTkButton(bottom_frame, text="Save to File", image=save_img, command=save_to_file)
save_button.pack(side=tk.LEFT,fill=tk.BOTH, expand=True, padx= 10) 

#guzik odczytywanie
read_button = ctk.CTkButton(bottom_frame, text="Read from File", image=read_img, command=read_from_file)
read_button.pack(side=tk.RIGHT,fill=tk.BOTH, expand=True)

#guzik usuwanie
entry_remove = tk.Entry(root, width=10)
entry_remove.pack(side=tk.LEFT,padx=10, pady=(10, 20),fill=tk.BOTH, expand=False)

remove_button = ctk.CTkButton(root, text="Remove Task by number", fg_color= 'black', text_color= 'white', command=remove_task)
remove_button.pack(side=tk.LEFT,padx=20, pady=(5, 20),fill=tk.BOTH, expand=True)

root.mainloop()