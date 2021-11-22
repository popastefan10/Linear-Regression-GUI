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


def refresh_plot_data():
    """
    Callback used to get the plot data and display it on the main app.
    """

    if MainApp.plot is not None:
        plot_points = MainApp.plot.points
        plot_lin_reg = MainApp.plot.lin_reg
        already_added_points = MainApp.plot_data.points

        for i in range(len(already_added_points), len(plot_points)):
            # Add only new points
            new_point = plot_points[i]
            MainApp.plot_data.update_data(new_point.x, new_point.y, 
                                          plot_lin_reg.get_alpha(), plot_lin_reg.get_beta())

    root.after(500, refresh_plot_data)


root.after(100, refresh_plot_data)
root.bind("<Configure>", on_resize)

root.mainloop()
