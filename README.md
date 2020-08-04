# Linear-Regression-GUI
 
This is a GUI that I created in order to help for better visualization of simple linear regression.
I used matplotlib to make the plot which displays the points and the best-fitting line, while for creating the GUI I used tkinter widgets.
This is my first project in python, so every feedback regarding documenting python code, coding structure and coding techniques are really welcome.

## How to use

Run the "examples.py" file and the GUI should appear on your screen.
Then, press the "New plot" button and a new window (which should be named "Figure 1") will be created.
This window is where you can add points and see the best fitting line created automatically according to the Ordinary least squares (OLS) approximation method used in the simple linear regression model.
You can have only one plot window open at a time, so if you want to make a new plot window, you have to close the old one first.

Adding points to the plot can be done in 2 ways:
-type the coordinates of the new point in the two entries labeled with "X: ", and "Y: ", then press "Add point". This will work only if you typed 2 coordinates, and both are real-valued numbers (for example, "2", "17.831", "  3.0" will work, but "2 3" or "2,5" won't).
-click on the check near the "Add multiple points" label and then you can start adding points on the plot by clicking on it.
Note: if you add a point on the plot and it doesn't appear, it is probably because it was plotted outside of the current axes limits. What you have to do is resize the plot, which can be done using the four-arrows button inside the plot window (the fourth from left to right, located on the bottom of the window).

If you resize the plot window you might see that the best fitting line won't be as stretched as it can be, but this can be solved by clicking the "Update line" button, which will draw a new line with respect to the axes' limits.

Also, the coefficients of the best fitting line will be displayed in the plot data section at the bottom of the GUI window, as well as all the points displayed on the plot.

