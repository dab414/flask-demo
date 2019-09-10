import numpy as np
import requests
import simplejson as json
from bokeh.plotting import figure, show
from bokeh.resources import CDN
from bokeh.embed import file_html, json_item
from datetime import datetime 
from dateutil.parser import parse

h = requests.get('https://www.quandl.com/api/v3/datasets/WIKI/GOOG/data.json?api_key=Qsspq9oLN8EGfAJzg93S&start_date=2015-06-01&end_date=2015-06-30').content
h = json.loads(h)['dataset_data']['data']

dates = []
prices = []

for ob in h:
	dates.append(ob[0])
	prices.append(ob[4])

dates = [parse(x) for x in dates]

title = 'Quandl Wiki EOD Stock Prices for GOOG during October 2008'
p = figure(x_axis_type = 'datetime', title = title)
#p = figure(title = title)
p.line(dates, prices, line_width = 2)
#p.line([1,2,3,4], [5,6,7,8], line_width = 2)
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Closing Price'

print(dates)
print(prices)
print('\n')
print(len(dates) == len(prices))
show(p)