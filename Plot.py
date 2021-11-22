from tkinter import Canvas
import matplotlib.pyplot as plt
import numpy as np
from LinearRegression import LinearRegression


class Point:
    """ A class used to represent a point

    It is mainly used to store the points inside the matplotlib plot.

    Attributes
    ----------
    x : double
        the x coordinate of the point
    y : double
        the y coordinate of the point

    Methods
    -------
    get_x()
        Returns the x attribute
    get_y()
        Returns the y attribute
    """

    def __init__(self, x, y):
        """
        Parameters
        ----------
        x : double
            the x coordinate of the point
        y : double
            the y coordinate of the point
        """
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Plot:
    """
    Class for matplotlib plots

    This class is used to store the matplotlib figure and axes instances,
    as well as the points plotted and linear regression useful data.

    Attributes
    ----------
    fig : matplotlib.figure.Figure
        The top level container for the plot (according to matplotlib documentation)
        This is basically the window which contains the plot.
    ax : matplotlib.axes.Axes
        The Axes contains most of the figure elements, and sets the coordinate system.
        This is basically the plot, which contains the coordinate system, the points, etc.
    parent : MainApplication
        A reference to the MainApplication object which created the plot
        This is used to enable access to the PlotData object inside the main app.
    check_state : bool
        This tells the plot whether to add a new point if you click on it or not.
    cid : int
        A connection id that can be used to disconnect the on_click callback from the figure (self.fig)
    points : list
        A list which stores all the Point objects displayed on the plot
    lin_reg : LinearRegression
        An object used to compute the alpha and beta coefficients of the best fitting line
        The best fitting line's equation is: y = alpha + beta * x.

    Methods
    -------
    get_alpha()
        Returns the alpha coefficient of the best fitting line.
    get_beta()
        Returns the beta coefficient of the best fitting line.
    add_point(x, y)
        Adds a new point on the plot.
    update_best_fitting_line()
        Updates the best fitting line coefficients and makes it fill the axes.
    delete_existing_lines()
        Deletes the previous drawn line(s).
    update_check_state(new_val)
        Updates the check_state attribute to new_val.
    on_click(event)
        Callback which handles mouse clicks on the figure
    disconnect_on_click_clb()
        Disconnects on_click callback from the figure.

    Note: I added docstrings only to the most important class methods for the sake of code simplicity.
    """

    def __init__(self, parent):
        """
        Parameters
        ----------
        parent : MainApplication
            A reference to the MainApplication object which created the plot
            This is used to enable access to the PlotData object inside the main app.
        """

        self.fig, self.ax = plt.subplots()
        plt.show(block=False)

        self.parent = parent

        self.check_state = False
        self.cid = self.fig.canvas.mpl_connect("button_press_event", self.on_click)

        self.points = []
        self.lin_reg = LinearRegression()

        self.ax.set(xlim=(-10, 10), ylim=(-10, 10))

    def get_alpha(self):
        return self.lin_reg.get_alpha()

    def get_beta(self):
        return self.lin_reg.get_beta()

    def add_point(self, x, y):
        self.points.append(Point(x, y))
        self.lin_reg.add_point(x, y)
        plt.scatter(x, y, color="red")
        plt.draw()

        if len(self.points) > 1:
            self.update_best_fitting_line()

    def update_best_fitting_line(self):
        a = self.lin_reg.get_alpha()
        b = self.lin_reg.get_beta()
        if a is None or b is None:
            return 
            
        xmin, xmax, ymin, ymax = plt.axis()
        x = np.arange(xmin - 1, xmax + 1, (xmax - xmin) / 50)
        y = a + b * x

        self.delete_existing_lines()
        plt.plot(x, y, color="blue")
        plt.draw()

    def delete_existing_lines(self):
        while len(self.ax.lines):
            self.ax.lines.pop()

    def update_check_state(self, new_val):
        self.check_state = new_val

    def on_click(self, event):
        """ Callback which handles mouse clicks on the figure

        If the "Add multiple points" check is activated you can add points on the plot by clicking inside the axes.
        This adds a point on the plot only if the left mouse button was clicked inside the axes.
        """

        if len(self.points) > 1:
            self.update_best_fitting_line()
        if self.check_state is True and event.button == 1 and event.xdata is not None and event.ydata is not None:
            self.add_point(event.xdata, event.ydata)
            # self.parent.plot_data.update_data(event.xdata, event.ydata,
            #                                   self.lin_reg.get_alpha(), self.lin_reg.get_beta())

    def disconnect_on_click_clb(self):
        """ Disconnects on_click callback from the figure.

        The callback should be disconnected from the figure when the plot is closed.
        """

        self.fig.canvas.mpl_disconnect(self.cid)
