import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from sklearn.cluster import KMeans


def test(prometheus_url,periods,metrics,step):

    message = """<html>
    <head></head>
    <body><p>This is a test analytics results page comming from prometheusMetricsAnalyzer python package</p></body>
    </html>"""

    return message
