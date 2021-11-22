import tkinter as tk
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import Checkbutton
from tkinter import BooleanVar
import matplotlib.pyplot as plt
from Plot import Plot
from PlotData import PlotData


class MainApplication(tk.Frame):
    """
    The main frame of the GUI

    This class is the main component of the GUI.
    Its main purpose is managing one plot and displaying useful information related to it.
    It contains several buttons, entries and a PlotData widget used to display data.

    Attributes
    ----------
    BTN_HEIGHT : 30
        The height value that is used for all the buttons inside this class
    BTN_WIDTH : 90
        The width value that is used for all the buttons inside this class
    parent :
        The parent window (or widget)
    plot : Plot
        The plot managed by this class
    plot_data : PlotData
        The widget that displays data related to the plot
    new_plot_btn : Button
        The "New plot" button that creates the plot managed by this class
    x_label : Label
        A lebel which contains the text "X: "
    x_entry : Entry
        An entry in which you can type the x coordinate value for a new point
    y_label : Label
        A lebel which contains the text "Y: "
    x_entry : Entry
        An entry in which you can type the y coordinate value for a new point
    add_point_btn : Button
        The "Add point" button, which adds a point to the plot
        only if the values inside x_entry and y_entry are numbers
    add_multiple_points_check : Checkbutton
        The "Add multiple points" check button,
        which lets you add points on the plot by clicking inside the coordinate system only if it is activated
    check_state : BooleanVar
        Stores the state of add_multiple_points_check check button.
    update_line_btn : Button
        The "Update line" button, which stretches the best fitting line to match the plot's coordinate system size

    Methods
    -------
    create_plot_data()
        Returns a PlotData widget which will store the points inside the plot
        and the alpha and beta coefficients of the best fitting line.
    reset_plot_data()
        Resets the data inside the plot_data widget (alpha=None, beta=None, all points are deleted).
    create_new_plot()
        Assigns a new Plot instance to the plot attribute.
    remove_closed_plot()
        Disconnects the on_click callback from the plot and assigns "None" to the plot attribute.
    new_plot_clb()
        A callback assigned to the new_plot_btn ("New plot") button
        It checks for already existing but closed plots, creates a new one
        and resets the data inside plot_data widget.
    create_new_plot_btn()
        Returns a new new_plot_btn ("New plot") button.
    create_x_label()
        Returns the "X: " label.
    create_x_entry()
        Returns the entry used to get the x coordinate value
        for the point added by the add_point_btn ("Add point") button.
    create_y_label()
        Returns the "Y: " label.
    create_y_entry()
        Returns the entry used to get the y coordinate value
        for the point added by the add_point_btn ("Add point") button.
    add_point_clb()
        A callback assigned to the add_point_btn ("Add point") button
        First of all, it checks if the values of x_entry and y_entry are numbers.
        If those values are numbers it adds a point to the plot and plot_data,
        otherwise prints a message in the console.
    create_add_point_btn()
        Returns a new add_point_btn ("Add point") button.
    add_multiple_points_clb()
        A callback assigned to the add_multiple_points_check ("Add multiple points") check button.
        It updates check_state everytime the check button changes its state.
    create_add_multiple_points_check()
        Returns a new add_multiple_points_check ("Add multiple points") check button.
    update_line_clb()
        A callback assigned to the update_line_btn ("Update line") button.
        It stretches the best fitting line to match the plot's coordinate system size.
    create_update_line_btn()
        Returns a new update_line_btn ("Update line") button.
    is_number(s)
        Returns True if the "s" string is a float number, False otherwise.
    """

    BTN_HEIGHT = 30
    BTN_WIDTH = 90

    def __init__(self, parent, **args):
        """
        Parameters
        ----------
        parent :
            The parent window (or widget)
        **args :
            A list of options used by the LabelFrame widget (bg, height, width, text, etc.),
            which are passed to the LabelFrame __init__ function.
        """
        super().__init__(parent, args)
        self.parent = parent

        self.plot = None
        self.plot_data = self.create_plot_data()

        self.new_plot_btn = self.create_new_plot_btn()

        self.x_label = self.create_x_label()
        self.x_entry = self.create_x_entry()
        self.y_label = self.create_y_label()
        self.y_entry = self.create_y_entry()

        self.add_point_btn = self.create_add_point_btn()
        self.add_multiple_points_check, self.check_state = self.create_add_multiple_points_check()
        self.update_line_btn = self.create_update_line_btn()

    def create_plot_data(self):
        plot_data = PlotData(self, height=PlotData.HEIGHT, width=PlotData.WIDTH, bg="white")
        plot_data["text"] = "Plot data: "
        plot_data.place(x=10, y=165)
        return plot_data

    def reset_plot_data(self):
        self.plot_data.reset()

    def create_new_plot(self):
        self.plot = Plot(self)
        self.plot.update_check_state(self.check_state.get())

    def remove_closed_plot(self):
        if self.plot is not None and not plt.fignum_exists(self.plot.fig.number):
            self.plot.disconnect_on_click_clb()
            self.plot = None

    def new_plot_clb(self):
        self.remove_closed_plot()
        self.create_new_plot()
        self.reset_plot_data()

    def create_new_plot_btn(self):
        new_plot_btn = Button(self, text="New plot", command=self.new_plot_clb, padx=5)
        new_plot_btn.place(x=10, y=10, height=MainApplication.BTN_HEIGHT, width=MainApplication.BTN_WIDTH)
        return new_plot_btn

    def create_x_label(self):
        x_label = Label(self, text="X: ", bg="white")
        x_label.place(x=110, y=50, height=MainApplication.BTN_HEIGHT)
        return x_label

    def create_x_entry(self):
        x_entry = Entry(self, width=10)
        x_entry.place(x=130, y=50, height=MainApplication.BTN_HEIGHT)
        return x_entry

    def create_y_label(self):
        y_label = Label(self, text="Y: ", bg="white")
        y_label.place(x=200, y=50, height=MainApplication.BTN_HEIGHT)
        return y_label

    def create_y_entry(self):
        y_entry = Entry(self, width=10)
        y_entry.place(x=220, y=50, height=MainApplication.BTN_HEIGHT)
        return y_entry

    def add_point_clb(self):
        strx = self.x_entry.get()
        stry = self.y_entry.get()
        self.x_entry.delete(0, len(strx))
        self.y_entry.delete(0, len(stry))

        if not self.is_number(strx) or not self.is_number(stry):
            print("Please type valid numbers")
        else:
            x = float(strx)
            y = float(stry)
            self.plot.add_point(x, y)

            plot_lin_reg = self.plot.lin_reg
            self.plot_data.update_data(x, y, plot_lin_reg.get_alpha(), plot_lin_reg.get_beta())

    def create_add_point_btn(self):
        add_point_btn = Button(self, text="Add point", command=self.add_point_clb, padx=5)
        add_point_btn.place(x=10, y=50, height=MainApplication.BTN_HEIGHT, width=MainApplication.BTN_WIDTH)
        return add_point_btn

    def add_multiple_points_clb(self):
        self.plot.update_check_state(self.check_state.get())

    def create_add_multiple_points_check(self):
        check_state = BooleanVar()
        add_multiple_points_check = Checkbutton(self, text="Add multiple points", bg="white", var=check_state,
                                                onvalue=1, offvalue=0, command=self.add_multiple_points_clb)
        add_multiple_points_check.place(x=10, y=90)
        return add_multiple_points_check, check_state

    def update_line_clb(self):
        if self.plot is not None:
            self.plot.update_best_fitting_line()

    def create_update_line_btn(self):
        update_line_btn = Button(self, text="Update line", command=self.update_line_clb)
        update_line_btn.place(x=10, y=125, height=MainApplication.BTN_HEIGHT, width=MainApplication.BTN_WIDTH)
        return update_line_btn

    @staticmethod
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
