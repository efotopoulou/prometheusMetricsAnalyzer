import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from sklearn.cluster import KMeans


def ln(prometheus_url,periods,metrics,step):

    message = """<html>
    <head></head>
    <body><p>This is a test analytics results page comming from prometheusMetricsAnalyzer python package</p></body>
    </html>"""

    return message

def kmeans(prometheus_url,periods,metrics,step):

    print('geia sou')
    for metric in metrics:
        response =requests.get(prometheus_url + '/api/v1/query_range', params={'query': metric,'start':'2021-09-19T07:00:00.781Z','end':'2021-09-19T13:00:00.781Z','step':'3m'})
    #response.content
    X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
    kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

    #Getting unique labels
    label = kmeans.labels_
    u_labels = np.unique(label)

    #plotting the results:
    for i in u_labels:
        plt.scatter(X[label == i , 0] , X[label == i , 1] , label = i)
    plt.legend()
    #plt.show()
    #plt.savefig('templates/foo.png')
    message = """<html>
    <head></head>
    <body><p>This is a linear regression analytics results page comming from prometheusMetricsAnalyzer python package</p>
    <img src="plot.png" alt="foo" width="500" height="600">
    </body>
    </html>"""

    return message,plt
