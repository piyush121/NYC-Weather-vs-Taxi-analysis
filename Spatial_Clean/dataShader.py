import datashader as ds
import datashader.transfer_functions as tf
from datashader.bokeh_ext import InteractiveImage
from datashader.colors import Hot, inferno

import pandas as pd
from bokeh.plotting import figure, output_notebook, show

output_notebook()

x_range=(-8250000,-8210000)
y_range=(5965000,5990000)
def base_plot(tools='pan,wheel_zoom,reset',plot_width=900, plot_height=600, **plot_args):
    p = figure(tools=tools, plot_width=int(900*1.5), plot_height=int(600*1.5),
        x_range=x_range, y_range=y_range, outline_line_color=None,
        min_border=0, min_border_left=0, min_border_right=0,
        min_border_top=0, min_border_bottom=0, **plot_args)
    
    p.axis.visible = False
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    return p
df = pd.read_csv('nyc_new.csv')

# **Projection & Aggregation Step:**
# Map each record as a point centered by the fields `x_col` and `y_col` to
# a 400x400 grid of bins, computing the mean of `z_col` for all records in
# each bin.
# **Transformation Step:**
# Interpolate the resulting means along a logarithmic color palette from
# "lightblue" to "darkblue"
def create_image(x_range, y_range, w, h):
    cvs = ds.Canvas(plot_width=w, plot_height=h, x_range=x_range, y_range=y_range)
    agg = cvs.points(df, 'pickup_longitude', 'pickup_latitude',  ds.count('passenger_count'))
    img = tf.interpolate(agg, cmap=Hot, how='eq_hist')
    return tf.dynspread(img, threshold=0.5, max_px=4)

p = base_plot(background_fill_color="black",responsive=True, plot_width=int(900*1.5), plot_height=int(600*1.5))
InteractiveImage(p, create_image)