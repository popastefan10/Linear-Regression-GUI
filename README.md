# Linear-Regression-GUI
 
This is a GUI that I created in order to help improve visualization of simple linear regression.
I used Matplotlib to make the plot which displays the points and the best-fitting line, while for creating the GUI I used Tkinter widgets.
This is my first project in python, so every feedback regarding documenting python code, coding structure and coding techniques are really welcome.

## Requirements

In order to run the application, you need to have the following installed:
* Python 3
* NumPy
* Matplotlib
* Tkinter

## How to use

Run the _main.py_ file and the GUI should appear on your screen.
Then, click the _New plot_ button and a new window (which should be named _Figure 1_) will be created.
This window is where you can add points and see the best fitting line created automatically according to the Ordinary least squares (OLS) approximation method used in the simple linear regression model.
You can have only one plot window open at a time, so if you want to make a new plot window, you have to close the old one first.

![Start](https://user-images.githubusercontent.com/54329613/142879083-17ed1307-c3ef-44c2-903c-1b5d4fc651a9.png)

### Adding points

Adding points to the plot can be done in 2 ways:
1. type the coordinates of the new point in the two entries labeled with _X_, and _Y_, then click _Add point_. This will work only if you typed 2 coordinates, and both are real-valued numbers (for example, _X: 2 and Y: 17.831_ will work, but `X: 2 3 and Y:` or `X: 2,5 and Y: two` won't).
2. click on the check near the _Add multiple points_ label and then you can start adding points on the plot by clicking on it.

   **Note:** if you add a point on the plot and it doesn't appear, it is probably because it was plotted outside of the current axes limits. What you have to do is resize the plot, which can be done using the four-arrows button inside the plot window (the fourth from left to right, located on the bottom of the window).

### Updating the plot

If you resize the plot window you might see that the best fitting line won't be as stretched as it can be, but this can be solved by clicking the "Update line" button, which will draw a new line with respect to the axes' limits.

### Plot data

As you start adding points to the plot, their coordinates and the number of points you've added will appear on a panel. Above the points data you will be able to see the parameters of the best-fitting line, which has the equation `y=α*x+β`.

![Demo](https://user-images.githubusercontent.com/54329613/142885293-6fa4139f-2f96-4654-8b47-883dc167e409.png)


