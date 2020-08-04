from tkinter import *
from Plot import Point


class PlotData(LabelFrame):
    """
    A class used to represent data related to one plot

    This class inherits from LabelFrame so instances of this class are considered to be widgets.
    All the data stored inside an instance of this class is related to only one plot.
    This class' dataset consists of the following data related to the plot: points
    and alpha and beta coefficients of the best fitting line.
    The alpha and beta coefficients will be displayed as labels
    and the points will be displayed as entries inside a listbox.

    Attributes
    ----------
    HEIGHT : 300
        The height of a PlotData widget
    WIDTH : 350
        The width of a PlotData widget
    parent :
        The parent window (or widget)
    points : list
        The points of the plot
    alpha (default = None) : double
        The alpha coefficient of the best fitting line
    beta (default = None) : double
        The beta coefficient of the best fitting line
    alpha_label : Label
        A label which displays the value of alpha attribute
    beta_label : Label
        A label which displays the value of beta attribute
    points_label : Label
        A label which displays the number of points in the dataset
    points_list_box : ListBox
        The list box which contains the points in the dataset
    points_scrollbar : Scrollbar
        The scrollbar used to scroll through the points entries inside points_list_box

    Methods
    -------
    update_data(x, y, alpha, beta)
        Adds a new point and updates the alpha and beta attributes.
    add_point(x, y)
        Adds a new point to the data
    get_alpha()
        Returns the alpha attribute
    set_alpha(alpha)
        Updates the alpha attribute
    get_beta()
        Returns the beta attribute
    set_beta()
        Updates the beta attribute
    get_coef_string(coef)
        A static method which returns "undefined" if coef is None, str(coef) otherwise.
    create_alpha_label()
        Returns the label which displays the alpha attribute value
    update_alpha_label()
        Updates the value displayed in alpha_label
    create_beta_label()
        Returns the label which displays the beta attribute value
    update_beta_label()
        Updates the value displayed in beta_label
    create_points_label()
        Returns the label which displays the number of points in the dataset
    update_points_label()
        Updates the value displayed in points_label
    create_points_list_box()
        Returns the list box which contains the points
        and the scrollbar which is used to croll through the list box entries.
    reset()
        Resets the alpha and beta attributes' values to None
        and deletes all the points from the dataset and from the points list box.
    """

    HEIGHT = 300
    WIDTH = 350

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

        self.points = []
        self.alpha = None
        self.beta = None

        self.alpha_label = self.create_alpha_label()
        self.beta_label = self.create_beta_label()

        self.points_label = self.create_points_label()
        self.points_list_box, self.points_scrollbar = self.create_points_list_box()

    def update_data(self, x, y, alpha, beta):
        self.add_point(x, y)
        self.set_alpha(alpha)
        self.set_beta(beta)

    def add_point(self, x, y):
        self.points.append(Point(x, y))
        crt_len = len(self.points)
        self.points_list_box.insert(END, f"Point no.{crt_len}: ({x}, {y})")
        self.update_points_label()

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.update_alpha_label()

    def get_beta(self):
        return self.beta

    def set_beta(self, beta):
        self.beta = beta
        self.update_beta_label()

    @staticmethod
    def get_coef_string(coef):
        if coef is None:
            return "undefined"
        else:
            return coef

    def create_alpha_label(self):
        alpha_label = Label(self, text=f"Alpha: " + str(self.get_coef_string(self.alpha)), bg="white")
        alpha_label.place(x=5, y=5)
        return alpha_label

    def update_alpha_label(self):
        self.alpha_label["text"] = f"Alpha: " + str(self.get_coef_string(self.alpha))

    def create_beta_label(self):
        beta_label = Label(self, text=f"Beta: " + str(self.get_coef_string(self.beta)), bg="white")
        beta_label.place(x=5, y=25)
        return beta_label

    def update_beta_label(self):
        self.beta_label["text"] = f"Beta: " + str(self.get_coef_string(self.beta))

    def create_points_label(self):
        points_label = Label(self, text=f"There are {len(self.points)} points in this plot:", bg="white")
        points_label.place(x=5, y=55)
        return points_label

    def update_points_label(self):
        self.points_label["text"] = f"There are {len(self.points)} points in this plot:"

    def create_points_list_box(self):
        points_scrollbar = Scrollbar(self, orient=VERTICAL, width=16)
        points_scrollbar.place(x=310, y=75)

        points_list_box = Listbox(self, width=50, height=12, yscrollcommand=points_scrollbar.set)
        points_scrollbar.config(command=points_list_box.yview)

        points_list_box.place(x=5, y=75)
        return points_list_box, points_scrollbar

    def reset(self):
        self.points_list_box.delete(0, END)
        self.points = []
        self.update_points_label()
        self.set_alpha(None)
        self.set_beta(None)


if __name__ == "__main__":
    root = Tk()
    root.minsize(PlotData.WIDTH + 10, PlotData.HEIGHT + 10)

    PltData = PlotData(root, height=PlotData.HEIGHT, width=PlotData.WIDTH, text="Plot data: ")
    PltData.set_alpha(20)
    PltData.set_beta(1)
    for i in range(100):
        PltData.update_data(i, i, 0, 1)
    PltData.place(x=5, y=5)
    root.mainloop()
