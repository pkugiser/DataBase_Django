# coding=utf-8
import glob
import os
import datetime
import numpy as np
import matplotlib.pyplot as plt
from plotly.offline import plot
import plotly.graph_objs as go
#from mpl_toolkits.basemap import Basemap 
from matplotlib.patches import Polygon
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from snownlp import SnowNLP
import json
import re
import jieba
import jieba.analyse

#
#Emotion Analysis Function
#
def textEmotion(text):
	try:
		url = "https://api.prprpr.me/emotion/wenzhi?password=DIYgod&text={%s}" % quote(text)
		user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		req = Request(url, headers={'User-Agent': user_agent})
		data = urlopen(req).read().decode()
		json_str = json.loads(data)
		return json_str['positive']
	except Exception as e:
		print(e)


def pois(lt):
	lt = ''.join(lt)
	lt = re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%]", "", lt)
	result = jieba.analyse.extract_tags(lt, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
	trace1 = go.Scatter(
		x=[i[0] for i in result],
		y= [i[1] for i in result]
	)
	data = [trace1]
	layout = go.Layout(
		# autosize=False,
		# width=900,
		# height=500,

		xaxis=dict(
			autorange=True
		),
		yaxis=dict(
			autorange=True
		)
	)

	fig = go.Figure(data=data, layout=layout)
	plot_div = plot(fig,  include_plotlyjs=False, output_type='div')
	return plot_div


def plots(lt):
	trace1 = go.Scatter(
		x=[i+1 for i in range(len(lt))],
		# y=[textEmotion(re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%]", "", i)) for i in lt]
		y= [SnowNLP(re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%]", "", i)).sentiments for i in lt]
	)

	data = [trace1]
	layout = go.Layout(
		# autosize=False,
		# width=900,
		# height=500,

		xaxis=dict(
			autorange=True
		),
		yaxis=dict(
			autorange=True
		)
	)

	fig = go.Figure(data=data, layout=layout)
	plot_div = plot(fig,  include_plotlyjs=False, output_type='div')
	return plot_div
def plot1():
	x_data = ['北京','天津','河北', '山西','内蒙古','辽宁',\
	'吉林','黑龙江','上海','江苏','浙江',\
	'安徽','福建','江西','山东','河南',\
	'湖北',"湖南",'广东','广西','海南','重庆','四川','贵州'\
	'云南','西藏',"陕西",'甘肃','青海','宁夏'\
	'新疆', '台湾','香港',"澳门","其它", "海外"]
	trace1 = go.Bar(
		x=x_data,
		y=[32319,4414,3498,1913,1089,6479,1794,2651,186661,256497,54132,11707,13515,4528,8989,9094,11944,5010,40022,2897,1271,\
		4360,9769,1610,2033,365,5610,1171,226,312,1174,1263,1998,398,41220,16913]
	)

	data = [trace1]
	layout = go.Layout(
		# autosize=False,
		# width=900,
		# height=500,

		xaxis=dict(
			autorange=True
		),
		yaxis=dict(
			autorange=True
		)
	)

	fig = go.Figure(data=data, layout=layout)
	plot_div = plot(fig,  include_plotlyjs=False, output_type='div')
	return plot_div


def plot2():
	x_data = ['0-2h','2-4h', '4-6h','6-8h','8-10h','10-12h','12-14h','14-16h','16-18h','18-20h','20-22h','22-24h']
	trace1 = go.Scatter(
		x=x_data,
		y=[117983,33467,23471,101525,220874,289898,335334,320082,305274,372736,323773,266091]
	)

	data = [trace1]
	layout = go.Layout(
		# autosize=False,
		# width=900,
		# height=500,

		xaxis=dict(
			autorange=True
		),
		yaxis=dict(
			autorange=True
		)
	)

	fig = go.Figure(data=data, layout=layout)
	plot_div = plot(fig,  include_plotlyjs=False, output_type='div')
	return plot_div

def plots2(lt):
	x_data = ['0-2h','2-4h', '4-6h','6-8h','8-10h','10-12h','12-14h','14-16h','16-18h','18-20h','20-22h','22-24h']
	y_data=[0,0,0,0,0,0,0,0,0,0,0,0]
	for item in lt:
		time = item.split(" ")
		if time[3][0]=='0':
			if time[3][1] in "01":
				y_data[0]+=1
			elif  time[3][1] in "23":
				y_data[1] += 1
			elif time[3][1] in "45":
				y_data[2] += 1
			elif time[3][1] in "67":
				 y_data[3] += 1
			elif time[3][1] in "89":
				 y_data[4] += 1
		elif time[3][0]=='1':
			if time[3][1] in "01":
				y_data[5] += 1
			elif time[3][1] in "23":
				y_data[6] += 1
			elif time[3][1] in "45":
				y_data[7] += 1
			elif time[3][1] in "67":
				y_data[8] += 1
			elif time[3][1] in "89":
				y_data[9] += 1
		elif time[3][0]=='2':
			if time[3][1] in "01":
				y_data[10] += 1
			elif time[3][1] in "234":
				y_data[11] += 1
	trace1 = go.Scatter(
		x=x_data,
		y=y_data
	)
	data = [trace1]
	layout = go.Layout(
		# autosize=False,
		# width=900,
		# height=500,

		xaxis=dict(
			autorange=True
		),
		yaxis=dict(
			autorange=True
		)
	)

	fig = go.Figure(data=data, layout=layout)
	plot_div = plot(fig,  include_plotlyjs=False, output_type='div')
	return plot_div


if __name__ =="__main__":
	print(textEmotion("我恨你"))