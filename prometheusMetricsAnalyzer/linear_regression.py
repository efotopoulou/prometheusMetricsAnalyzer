import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from sklearn.linear_model import LinearRegression
import json

def ln(prometheus_url,periods,metrics,step):
    periods = periods[0]
    #print(periods['start'])
    endpoint = prometheus_url + '/api/v1/query_range'
    dataset = np.empty((0))
    for metric in metrics:
        response =requests.get(endpoint, params={'query': metric,'start':periods['start'],'end':periods['end'],'step':step})
        y = json.loads(response.content)
        values = y["data"]["result"][0]["values"]
        np_values = np.array(values)
        np_values = np.delete(np_values,0,1)
        if len(dataset)==0:
            dataset = np_values
        else:
            dataset = np.hstack((dataset, np_values))

        #print(dataset)

    x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
    y = np.array([5, 20, 14, 32, 22, 38])
    model = LinearRegression().fit(x, y)
    plt.scatter(x, y,color='g')
    plt.plot(x, model.predict(x),color='k')


    message = """<html>
    <head></head>
    <body><p>This is a linear regression analytics results page comming from prometheusMetricsAnalyzer python package</p>
    <img src="plot.png" alt="foo" width="500" height="600">
    </body>
    </html>"""

    return message,plt
