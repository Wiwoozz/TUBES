import pandas as pd
import numpy as np
import bokeh
from bokeh.layouts import layout, row, column, widgetbox, gridplot
from bokeh.plotting import figure, output_file, show
from bokeh.io import curdoc, show, output_notebook, output_file
from bokeh.models.tools import HoverTool
from bokeh.models import ColumnDataSource, HoverTool, CustomJS, Select, Slider, TextInput
from bokeh.models.widgets import Tabs, Panel
from bokeh.models import ColorPicker
from bokeh.models import RangeTool
output_notebook()


# read dataset
aces = pd.read_csv('data/ACES.csv')
aces.head(1)

aces['Date'] = pd.to_datetime(aces['Date'])
aces.dtypes

adro = pd.read_csv('data/ADRO.csv')
adro.head(1)

adro['Date'] = pd.to_datetime(adro['Date'])
adro.dtypes

akra = pd.read_csv('data/AKRA.csv')
akra.head(1)

akra['Date'] = pd.to_datetime(akra['Date'])
akra.dtypes

antm = pd.read_csv('data/ANTM.csv')
antm.head(1)

antm['Date'] = pd.to_datetime(antm['Date'])
antm.dtypes

# data source
data_source_aces = ColumnDataSource(aces)
data_source_adro = ColumnDataSource(adro)
data_source_akra = ColumnDataSource(akra)
data_source_antm = ColumnDataSource(antm)

"""#Open

"""

dates1 = np.array(aces['Date'])
fig1 = figure(x_axis_type='datetime',
              plot_height=400, plot_width=1000,
              title='Stock Market (Open)',
              x_axis_label='Year', y_axis_label='Open',
              x_range=(dates1[100], dates1[200]))

aces1 = fig1.line('Date', 'Open', legend_label='ACES',
                  color='red', line_width=2, source=data_source_aces)
adro1 = fig1.line('Date', 'Open', legend_label='ADRO',
                  color='yellow', line_width=2, source=data_source_adro)
akra1 = fig1.line('Date', 'Open', legend_label='AKRA',
                  color='green', line_width=2, source=data_source_akra)
antm1 = fig1.line('Date', 'Open', legend_label='ANTM',
                  color='blue', line_width=2, source=data_source_antm)

# input title
text1 = TextInput(title='Title Open', value='Stock Market (Open)')
# callbacks


def update_title(attrname, old, new):
    fig1.title.text = text1.value


text1.on_change('value', update_title)

# interaktif color
pickeraces1 = ColorPicker(title='set color ACES', default_size=100)
pickeraces1.js_link('color', aces1.glyph, 'line_color')

pickeradro1 = ColorPicker(title='set color ADRO', default_size=100)
pickeradro1.js_link('color', adro1.glyph, 'line_color')

pickerakra1 = ColorPicker(title='set color AKRA', default_size=100)
pickerakra1.js_link('color', akra1.glyph, 'line_color')

pickerantm1 = ColorPicker(title='set color ANTM', default_size=100)
pickerantm1.js_link('color', antm1.glyph, 'line_color')


tooltips = [('Date', '@Date{%F}'), ('Value', '@{Open}')]
formatters = {'@Date': 'datetime'}

curdoc().theme = 'dark_minimal'

fig1.add_tools(HoverTool(renderers=[aces1],
               tooltips=tooltips, formatters=formatters))
fig1.add_tools(HoverTool(renderers=[adro1],
               tooltips=tooltips, formatters=formatters))
fig1.add_tools(HoverTool(renderers=[akra1],
               tooltips=tooltips, formatters=formatters))
fig1.add_tools(HoverTool(renderers=[antm1],
               tooltips=tooltips, formatters=formatters))

fig1.legend.location = 'top_right'
fig1.legend.click_policy = 'hide'

layout1 = row(fig1, widgetbox(
    pickeraces1, pickeradro1, pickerakra1, pickerantm1))
# curdoc().add_root(layout1)

# show(layout1)

select1 = figure(title='Stock Market (Open)',
                 plot_height=150,
                 plot_width=1000,
                 y_range=fig1.y_range,
                 x_axis_type='datetime',
                 tools='',
                 x_axis_label='Year',
                 y_axis_label='Open',
                 toolbar_location=None)
range_tool = RangeTool(x_range=fig1.x_range)
range_tool.overlay.fill_color = 'red'
range_tool.overlay.fill_alpha = .2

select1.line('Date', 'Low', color='red', line_width=2, source=data_source_aces)
select1.line('Date', 'Low', color='yellow',
             line_width=2, source=data_source_adro)
select1.line('Date', 'Low', color='green',
             line_width=2, source=data_source_akra)
select1.line('Date', 'Low', color='blue',
             line_width=2, source=data_source_antm)

# select1.ygrid.gird_line_color=None
select1.add_tools(range_tool)
select1.toolbar.active_multi = range_tool

layoutsatu = column(select1)
# show(layoutsatu)

grid1 = gridplot([[layout1], [layoutsatu]])
# show(grid1)

"""#High"""

dates2 = np.array(aces['Date'])
fig2 = figure(x_axis_type='datetime',
              plot_height=400, plot_width=1000,
              title='Stock Market (High)',
              x_axis_label='Year', y_axis_label='High',
              x_range=(dates2[100], dates2[200]))

aces2 = fig2.line('Date', 'High', legend_label='ACES',
                  color='red', line_width=2, source=data_source_aces)
adro2 = fig2.line('Date', 'High', legend_label='ADRO',
                  color='yellow', line_width=2, source=data_source_adro)
akra2 = fig2.line('Date', 'High', legend_label='AKRA',
                  color='green', line_width=2, source=data_source_akra)
antm2 = fig2.line('Date', 'High', legend_label='ANTM',
                  color='blue', line_width=2, source=data_source_antm)

# input title
text2 = TextInput(title='Title High', value='Stock Market (High)')
# callbacks


def update_title(attrname, old, new):
    fig2.title.text = text2.value


text2.on_change('value', update_title)

# interaktif color
pickeraces2 = ColorPicker(title='set color ACES', default_size=100)
pickeraces2.js_link('color', aces2.glyph, 'line_color')

pickeradro2 = ColorPicker(title='set color ADRO', default_size=100)
pickeradro2.js_link('color', adro2.glyph, 'line_color')

pickerakra2 = ColorPicker(title='set color AKRA', default_size=100)
pickerakra2.js_link('color', akra2.glyph, 'line_color')

pickerantm2 = ColorPicker(title='set color ANTM', default_size=100)
pickerantm2.js_link('color', antm2.glyph, 'line_color')


tooltips = [('Date', '@Date{%F}'), ('Value', '@{High}')]
formatters = {'@Date': 'datetime'}

curdoc().theme = 'dark_minimal'

fig2.add_tools(HoverTool(renderers=[aces2],
               tooltips=tooltips, formatters=formatters))
fig2.add_tools(HoverTool(renderers=[adro2],
               tooltips=tooltips, formatters=formatters))
fig2.add_tools(HoverTool(renderers=[akra2],
               tooltips=tooltips, formatters=formatters))
fig2.add_tools(HoverTool(renderers=[antm2],
               tooltips=tooltips, formatters=formatters))

fig2.legend.location = 'top_right'
fig2.legend.click_policy = 'hide'

layout2 = row(fig2, widgetbox(
    pickeraces2, pickeradro2, pickerakra2, pickerantm2))
# curdoc().add_root(layout2)

select2 = figure(title='Stock Market (High)',
                 plot_height=150,
                 plot_width=1000,
                 y_range=fig2.y_range,
                 x_axis_type='datetime',
                 tools='',
                 x_axis_label='Year',
                 y_axis_label='High',
                 toolbar_location=None)
range_tool = RangeTool(x_range=fig2.x_range)
range_tool.overlay.fill_color = 'red'
range_tool.overlay.fill_alpha = .2

select2.line('Date', 'Low', color='red', line_width=2, source=data_source_aces)
select2.line('Date', 'Low', color='yellow',
             line_width=2, source=data_source_adro)
select2.line('Date', 'Low', color='green',
             line_width=2, source=data_source_akra)
select2.line('Date', 'Low', color='blue',
             line_width=2, source=data_source_antm)

# select2.ygrid.gird_line_color=None
select2.add_tools(range_tool)
select2.toolbar.active_multi = range_tool

layoutdua = column(select2)
# show(layoutdua)

grid2 = gridplot([[layout2], [layoutdua]])
# show(grid2)

"""#Low"""

dates3 = np.array(aces['Date'])
fig3 = figure(x_axis_type='datetime',
              plot_height=400, plot_width=1000,
              title='Stock Market (Low)',
              x_axis_label='Year', y_axis_label='Low',
              x_range=(dates3[100], dates3[200]))

aces3 = fig3.line('Date', 'Low', legend_label='ACES',
                  color='red', line_width=2, source=data_source_aces)
adro3 = fig3.line('Date', 'Low', legend_label='ADRO',
                  color='yellow', line_width=2, source=data_source_adro)
akra3 = fig3.line('Date', 'Low', legend_label='AKRA',
                  color='green', line_width=2, source=data_source_akra)
antm3 = fig3.line('Date', 'Low', legend_label='ANTM',
                  color='blue', line_width=2, source=data_source_antm)

# input title
text3 = TextInput(title='Title Low', value='Stock Market (Low)')
# callbacks


def update_title(attrname, old, new):
    fig3.title.text = text3.value


text3.on_change('value', update_title)

# interaktif color
pickeraces3 = ColorPicker(title='set color ACES', default_size=100)
pickeraces3.js_link('color', aces3.glyph, 'line_color')

pickeradro3 = ColorPicker(title='set color ADRO', default_size=100)
pickeradro3.js_link('color', adro3.glyph, 'line_color')

pickerakra3 = ColorPicker(title='set color AKRA', default_size=100)
pickerakra3.js_link('color', akra3.glyph, 'line_color')

pickerantm3 = ColorPicker(title='set color ANTM', default_size=100)
pickerantm3.js_link('color', antm3.glyph, 'line_color')


tooltips = [('Date', '@Date{%F}'), ('Value', '@{Low}')]
formatters = {'@Date': 'datetime'}

curdoc().theme = 'dark_minimal'

fig3.add_tools(HoverTool(renderers=[aces3],
               tooltips=tooltips, formatters=formatters))
fig3.add_tools(HoverTool(renderers=[adro3],
               tooltips=tooltips, formatters=formatters))
fig3.add_tools(HoverTool(renderers=[akra3],
               tooltips=tooltips, formatters=formatters))
fig3.add_tools(HoverTool(renderers=[antm3],
               tooltips=tooltips, formatters=formatters))

fig3.legend.location = 'top_right'
fig3.legend.click_policy = 'hide'

layout3 = row(fig3, widgetbox(
    pickeraces3, pickeradro3, pickerakra3, pickerantm3))
# curdoc().add_root(layout3)

select3 = figure(title='Stock Market (Low)',
                 plot_height=150,
                 plot_width=1000,
                 y_range=fig3.y_range,
                 x_axis_type='datetime',
                 tools='',
                 x_axis_label='Year',
                 y_axis_label='Low',
                 toolbar_location=None)
range_tool = RangeTool(x_range=fig3.x_range)
range_tool.overlay.fill_color = 'red'
range_tool.overlay.fill_alpha = .2

select3.line('Date', 'Low', color='red', line_width=2, source=data_source_aces)
select3.line('Date', 'Low', color='yellow',
             line_width=2, source=data_source_adro)
select3.line('Date', 'Low', color='green',
             line_width=2, source=data_source_akra)
select3.line('Date', 'Low', color='blue',
             line_width=2, source=data_source_antm)

# select3.ygrid.gird_line_color=None
select3.add_tools(range_tool)
select3.toolbar.active_multi = range_tool

layouttiga = column(select3)
# show(layouttiga)

grid3 = gridplot([[layout3], [layouttiga]])
# show(grid3)

"""#Close"""

dates4 = np.array(aces['Date'])
fig4 = figure(x_axis_type='datetime',
              plot_height=400, plot_width=1000,
              title='Stock Market (Close)',
              x_axis_label='Year', y_axis_label='Close',
              x_range=(dates4[100], dates4[200]))

aces4 = fig4.line('Date', 'Close', legend_label='ACES',
                  color='red', line_width=2, source=data_source_aces)
adro4 = fig4.line('Date', 'Close', legend_label='ADRO',
                  color='yellow', line_width=2, source=data_source_adro)
akra4 = fig4.line('Date', 'Close', legend_label='AKRA',
                  color='green', line_width=2, source=data_source_akra)
antm4 = fig4.line('Date', 'Close', legend_label='ANTM',
                  color='blue', line_width=2, source=data_source_antm)

# input title
text4 = TextInput(title='Title Close', value='Stock Market (Close)')
# callbacks


def update_title(attrname, old, new):
    fig4.title.text = text4.value


text4.on_change('value', update_title)

# interaktif color
pickeraces4 = ColorPicker(title='set color ACES', default_size=100)
pickeraces4.js_link('color', aces4.glyph, 'line_color')

pickeradro4 = ColorPicker(title='set color ADRO', default_size=100)
pickeradro4.js_link('color', adro4.glyph, 'line_color')

pickerakra4 = ColorPicker(title='set color AKRA', default_size=100)
pickerakra4.js_link('color', akra4.glyph, 'line_color')

pickerantm4 = ColorPicker(title='set color ANTM', default_size=100)
pickerantm4.js_link('color', antm4.glyph, 'line_color')


tooltips = [('Date', '@Date{%F}'), ('Value', '@{Close}')]
formatters = {'@Date': 'datetime'}

curdoc().theme = 'dark_minimal'

fig4.add_tools(HoverTool(renderers=[aces4],
               tooltips=tooltips, formatters=formatters))
fig4.add_tools(HoverTool(renderers=[adro4],
               tooltips=tooltips, formatters=formatters))
fig4.add_tools(HoverTool(renderers=[akra4],
               tooltips=tooltips, formatters=formatters))
fig4.add_tools(HoverTool(renderers=[antm4],
               tooltips=tooltips, formatters=formatters))

fig4.legend.location = 'top_right'
fig4.legend.click_policy = 'hide'

layout4 = row(fig4, widgetbox(
    pickeraces4, pickeradro4, pickerakra4, pickerantm4))
# curdoc().add_root(layout4)

select4 = figure(title='Stock Market (Close)',
                 plot_height=150,
                 plot_width=1000,
                 y_range=fig4.y_range,
                 x_axis_type='datetime',
                 tools='',
                 x_axis_label='Year',
                 y_axis_label='Close',
                 toolbar_location=None)
range_tool = RangeTool(x_range=fig4.x_range)
range_tool.overlay.fill_color = 'red'
range_tool.overlay.fill_alpha = .2

select4.line('Date', 'Close', color='red',
             line_width=2, source=data_source_aces)
select4.line('Date', 'Close', color='yellow',
             line_width=2, source=data_source_adro)
select4.line('Date', 'Close', color='green',
             line_width=2, source=data_source_akra)
select4.line('Date', 'Close', color='blue',
             line_width=2, source=data_source_antm)

# select4.ygrid.gird_line_color=None
select4.add_tools(range_tool)
select4.toolbar.active_multi = range_tool

layoutempat = column(select4)
# show(layoutempat)

grid4 = gridplot([[layout4], [layoutempat]])
# show(grid4)

"""#Volume"""

dates5 = np.array(aces['Date'])
fig5 = figure(x_axis_type='datetime',
              plot_height=400, plot_width=1000,
              title='Stock Market (Volume)',
              x_axis_label='Year', y_axis_label='Volume',
              x_range=(dates5[100], dates5[200]))

aces5 = fig5.line('Date', 'Volume', legend_label='ACES',
                  color='red', line_width=2, source=data_source_aces)
adro5 = fig5.line('Date', 'Volume', legend_label='ADRO',
                  color='yellow', line_width=2, source=data_source_adro)
akra5 = fig5.line('Date', 'Volume', legend_label='AKRA',
                  color='green', line_width=2, source=data_source_akra)
antm5 = fig5.line('Date', 'Volume', legend_label='ANTM',
                  color='blue', line_width=2, source=data_source_antm)

# input title
text5 = TextInput(title='Title Volume', value='Stock Market (Volume)')
# callbacks


def update_title(attrname, old, new):
    fig5.title.text = text5.value


text5.on_change('value', update_title)


# interaktif color
pickeraces5 = ColorPicker(title='set color ACES', default_size=100)
pickeraces5.js_link('color', aces5.glyph, 'line_color')

pickeradro5 = ColorPicker(title='set color ADRO', default_size=100)
pickeradro5.js_link('color', adro5.glyph, 'line_color')

pickerakra5 = ColorPicker(title='set color AKRA', default_size=100)
pickerakra5.js_link('color', akra5.glyph, 'line_color')

pickerantm5 = ColorPicker(title='set color ANTM', default_size=100)
pickerantm5.js_link('color', antm5.glyph, 'line_color')


tooltips = [('Date', '@Date{%F}'), ('Value', '@{Volume}')]
formatters = {'@Date': 'datetime'}

curdoc().theme = 'dark_minimal'

fig5.add_tools(HoverTool(renderers=[aces5],
               tooltips=tooltips, formatters=formatters))
fig5.add_tools(HoverTool(renderers=[adro5],
               tooltips=tooltips, formatters=formatters))
fig5.add_tools(HoverTool(renderers=[akra5],
               tooltips=tooltips, formatters=formatters))
fig5.add_tools(HoverTool(renderers=[antm5],
               tooltips=tooltips, formatters=formatters))

fig5.legend.location = 'top_right'
fig5.legend.click_policy = 'hide'

layout5 = row(fig5, widgetbox(
    pickeraces5, pickeradro5, pickerakra5, pickerantm5))
# curdoc().add_root(layout5)

select5 = figure(title='Stock Market (Volume)',
                 plot_height=150,
                 plot_width=1000,
                 y_range=fig5.y_range,
                 x_axis_type='datetime',
                 tools='',
                 x_axis_label='Year',
                 y_axis_label='Volume',
                 toolbar_location=None)
range_tool = RangeTool(x_range=fig5.x_range)
range_tool.overlay.fill_color = 'red'
range_tool.overlay.fill_alpha = .2

select5.line('Date', 'Volume', color='red',
             line_width=2, source=data_source_aces)
select5.line('Date', 'Volume', color='yellow',
             line_width=2, source=data_source_adro)
select5.line('Date', 'Volume', color='green',
             line_width=2, source=data_source_akra)
select5.line('Date', 'Volume', color='blue',
             line_width=2, source=data_source_antm)

# select5.ygrid.gird_line_color=None
select5.add_tools(range_tool)
select5.toolbar.active_multi = range_tool

layoutlima = column(select5)
# show(layoutlima)

grid5 = gridplot([[layout5], [layoutlima]])
# show(grid5)

"""#Final Show"""

tab_open = Panel(child=grid1, title='Open')
tab_high = Panel(child=grid2, title='High')
tab_low = Panel(child=grid3, title='Low')
tab_close = Panel(child=grid4, title='Close')
tab_volume = Panel(child=grid5, title='Volume')


output_file('hasil2.html')

inputs1 = column(text1)
inputs2 = column(text2)
inputs3 = column(text3)
inputs4 = column(text4)
inputs5 = column(text5)
tabs = Tabs(tabs=[tab_open, tab_high, tab_low, tab_close, tab_volume])

curdoc().add_root(row(inputs1, inputs2, inputs3, width=250))
curdoc().add_root(row(inputs4, inputs5, width=250))
curdoc().add_root(column(tabs))
# curdoc().add_root(column(inputs5, width=500))
curdoc().title = 'Stock Market'
# show(tabs)
