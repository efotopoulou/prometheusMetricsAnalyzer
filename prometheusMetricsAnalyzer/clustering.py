import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from sklearn.cluster import KMeans
import json

def kmeans(prometheus_url,periods,metrics,step):

    #periods":[{"start":"2021-09-19T07:00:00.781Z","end":"2021-09-19T13:00:00.781Z"}]
    periods = periods[0]
    print(periods['start'])
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

        print(dataset)

    #X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
    kmeans = KMeans(n_clusters=2, random_state=0).fit(dataset)

    #Getting unique labels
    label = kmeans.labels_
    u_labels = np.unique(label)

    #plotting the results:
    for i in u_labels:
        plt.scatter(dataset[label == i , 0] , dataset[label == i , 1] , label = i)
    #plt.legend()
    #plt.show()
    #plt.savefig('templates/foo.png')
    message = """<html>
    <head></head>
    <body><p>This is a linear regression analytics results page comming from prometheusMetricsAnalyzer python package</p>
    <img src="plot.png" alt="foo" width="500" height="600">
    </body>
    </html>"""

    return message,plt
