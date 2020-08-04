from MainApp import MainApplication
from tkinter import Tk

root = Tk()
root.title("Linear regression in python")
min_root_width = 400
min_root_height = 500
root.minsize(min_root_width, min_root_height)

root.update()
MainApp = MainApplication(root, width=root.winfo_width(), height=root.winfo_height(), bg="white")
MainApp.grid_propagate(0)
MainApp.grid(row=0, column=0)


def on_resize(event):
    """
    Callback used to resize MainApp when the master window is resized.
    """

    new_width = max(event.width, min_root_width)
    new_height = max(event.height, min_root_height)
    MainApp["width"] = new_width
    MainApp["height"] = new_height


root.bind("<Configure>", on_resize)

root.mainloop()
