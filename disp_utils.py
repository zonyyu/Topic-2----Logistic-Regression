import numpy as np
from bokeh.plotting import figure, show, output_notebook
from bokeh.layouts import row


x = np.array([1.4, 1.5, 1.56, 1.65, 1.63, 1.74, 1.92, 1.96, 2.04, 2.08])
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1])

line_x = np.arange(0.5, 2.5, 0.1)
line_y = 2 * line_x - 3.1

SHOW = True


def display_height_dataset(x=x, y=y):
    if SHOW:
        p = figure(width=600, height=300, y_range=(-0.2, 1.2), x_range=(0.5, 2.5), x_axis_label="Height (m)", y_axis_label="Enter NBA?", title="Enter NBA vs Height")
        p.circle(x, y)
        output_notebook()
    
        show(p)

def display_height_line1(x=x, y=y, line_x=line_x, line_y=line_y):
    if SHOW:
        p = figure(width=600, height=300, y_range=(-0.2, 1.2), x_range=(0.5, 2.5), x_axis_label="Height (m)", y_axis_label="Enter NBA?", title="Enter NBA vs Height")
        p.circle(x, y)
        p.line(line_x, line_y)
        p.line([1.8, 1.8], [-1, 2], color="orange")
        output_notebook()
        show(p)


x2 = np.array([1, 1.4, 1.5, 1.56, 1.65, 1.63, 1.74, 1.92, 1.96, 2.04, 2.08])
y2 = np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1])

line_x2 = np.arange(0.5, 2.5, 0.1)
line_y2 = 1.2 * line_x2 - 1.5

def display_height_line2(x=x2, y=y2, line_x=line_x2, line_y=line_y2):
    if SHOW:
        p = figure(width=600, height=300, y_range=(-0.2, 1.2), x_range=(0.5, 2.5), x_axis_label="Height (m)", y_axis_label="Enter NBA?", title="Enter NBA vs Height")
        p.circle(x, y)
        p.line(line_x, line_y)
        p.line([1.67, 1.67], [-1, 2], color="orange")
        output_notebook()
    
        show(p)


def display_func(func=None):

    if func is None:
        return 
    
    x = np.arange(-10, 10, 0.1)
    y_lin = x
    y_sig = func(x)
    p = figure(width=600, height=400, x_range=(-5, 5), y_range=(-2, 2), title="Sigmoid Function")
    p.line(x, y_lin, color="blue", legend_label="z")
    p.line(x, y_sig, color="red", legend_label="sigmoid(z)")
    p.legend.title="Activation Function"
    p.legend.location = "bottom_right"
    p.line([0, 0], [-100, 100], color="black")
    p.line([-100, 100], [0, 0], color="black")
    p.xaxis.visible = True
    p.yaxis.visible = True
    output_notebook()
    if SHOW:
        show(p)


def disp_convex():
    """
    plots a convex and a non convex function side by side
    """
    x = np.arange(-10, 10, 0.1)
    y1 = 0.5*(x)**2
    y2 = 0.005*(x+5)*(x + 2)**2 *(x)*(x - 3)*(x - 4) + 5
    p = figure(width=400, height=300, title="Convex Function")
    p.line(x, y1)
    p2 = figure(width=400, height=300, y_range=(-2, 10), title="Non-Convex Function")
    p2.line(x, y2)
    r = row(p, p2)
    output_notebook()
    show(r)





   