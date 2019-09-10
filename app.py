from flask import Flask, render_template, request, redirect
import requests
import simplejson as json
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html, json_item
from dateutil.parser import parse
import os

app = Flask(__name__)

@app.route('/')
def index():
  return redirect('/index')

@app.route('/index', methods = ['GET', 'POST'])
def index2():
  if request.method == 'GET':
  	return render_template('index.html')
  else:
  	ticker = open('ticker.txt', 'w')
  	ticker.write(request.form['ticker'])
  	ticker.close()
  	return redirect('/graph')

@app.route('/graph')
def graph():
	
	return render_template('graph.html')


@app.route('/makeplot')
def makeplot():
	ticker = open('ticker.txt', 'r').read()

	h = requests.get('https://www.quandl.com/api/v3/datasets/WIKI/' + ticker + '/data.json?api_key=Qsspq9oLN8EGfAJzg93S&start_date=2008-10-01&end_date=2008-10-31').content
	h = json.loads(h)['dataset_data']['data']

	dates = []
	prices = []

	for ob in h:
		dates.append(ob[0])
		prices.append(ob[4])

	dates = [parse(x) for x in dates]

	title = 'Quandl Wiki EOD Stock Prices for ' + ticker + ' during October 2008 (The Great Recession!)'
	p = figure(x_axis_type = 'datetime', title = title)
	p.line(dates, prices, line_width = 2)
	p.xaxis.axis_label = 'Date'
	p.yaxis.axis_label = 'Closing Price'

	return json.dumps(json_item(p, 'myplot'))




if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)

