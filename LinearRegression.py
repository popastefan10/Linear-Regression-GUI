class LinearRegression:
    """

    This class stores a points dataset and has utility functions for the linear regression model.
    This is a simple linear regression model , where y = f(x).
    I used Ordinary least squares (OLS) method for estimating the the unknown parameters (alpha and beta).
    For reference: https://en.wikipedia.org/wiki/Ordinary_least_squares

    Attributes
    ----------
    alpha (default = None) : double
        The alpha coefficient of the best fitting line
    beta (default = None) : double
        The beta coefficient of the best fitting line
        Both coefficients will be set to None aren't at least 2 points in the dataset.
        The best fitting line's equation is: y = alpha + beta * x.
    n (default = 0) : int
        The number of points in the dataset
    sx (default = 0) : double
        Sum of x coordinates for all the points in the dataset
    sy (default = 0) : double
        Sum of y coordinates for all the points in the dataset
    sxy (default = 0) : double
        Sum of x * y for all the points in the dataset
    sx2 (default = 0) : double
        Sum of x squared for all points in the dataset

    # Note: I used sx, sy, sxy and sx2 attributes in order to minimize the number of calculations
    required to compute alpha and beta when a new point is added to the dataset.

    Methods
    -------
    update_coef()
        Updates the alpha and beta attributes.
    get_alpha()
        Returns the alpha attribute.
    get_beta()
        Returns the beta attribute.
    add_point(x, y)
        Adds a new point to the dataset.
    del_point(x, y)
        Deletes a (hopefully existing) point from the dataset.

    """

    def __init__(self):
        self.alpha = None
        self.beta = None
        self.n = 0

        self.sx = 0
        self.sy = 0
        self.sxy = 0
        self.sx2 = 0

    def update_coef(self):
        num = self.sxy - self.sx * self.sy / self.n
        den = self.sx2 - self.sx * self.sx / self.n
        self.beta = num / den

        xmed = self.sx / self.n
        ymed = self.sy / self.n
        self.alpha = ymed - self.beta * xmed

    def get_alpha(self):
        return self.alpha

    def get_beta(self):
        return self.beta

    def add_point(self, x, y):
        """ Adds a new point to the dataset.

        Parameters
        ----------
        x : double
            The x coordinate of the new point
        y : double
            The y coordinate of the new point
        """
        self.n += 1
        self.sx += x
        self.sy += y
        self.sxy += x * y
        self.sx2 += x * x

        if self.n > 1:
            self.update_coef()

    def del_point(self, x, y):
        """ Deletes a (hopefully existing) point from the dataset.

        It is assumed that there already is a point with the coordinates x and y in the dataset
        before this function is called.

        Parameters
        ----------
        x : double
            x coordinate of the point to be deleted
        y : double
            y coordinate of the point to be deleted
        """
        if self.n == 0:
            return False

        self.n -= 1
        self.sx -= x
        self.sy -= y
        self.sxy -= x * y
        self.sx2 -= x * x
        return True


if __name__ == "__main__":
    lin_reg = LinearRegression()

    pts = [
        [12.39999962,	11.19999981],
        [14.30000019,	12.5],
        [14.5,	12.69999981],
        [14.89999962,	13.10000038],
        [16.10000038,	14.10000038],
        [16.89999962,	14.80000019],
        [16.5,	14.39999962],
        [15.39999962,	13.39999962],
        [17,	14.89999962],
        [17.89999962,	15.60000038],
        [18.79999924,	16.39999962],
        [20.29999924,	17.70000076],
        [22.39999962,	19.60000038],
        [19.39999962,	16.89999962],
        [15.5,	14],
        [16.70000076,	14.60000038],
        [17.29999924,	15.10000038],
        [18.39999962,	16.10000038],
        [19.20000076,	16.79999924],
        [17.39999962,	15.19999981],
        [19.5,	17],
        [19.70000076,	17.20000076],
        [21.20000076,	18.60000038]
        ]

    for point in pts:
        lin_reg.add_point(point[0], point[1])

    print(f"y = {lin_reg.get_alpha()} + {lin_reg.get_beta()} * x")
