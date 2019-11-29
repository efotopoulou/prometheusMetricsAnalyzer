import os
import pandas as pd
#import prometheus_connection
import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt
#from sklearn.linear_model import LinearRegression


def ln(prometheus_url,periods,metrics,step):
    
#    print(metrics[1])
#   
#    for period in periods:
        #print (period['start'])
        #print (period['end'])
#        y_data = prometheus_connection.get_prometheus_timeserie(prometheus_url,metrics[0],period['start'],period['end'],step)
#        print("y_data")
#        print(y_data)
        
#    for period in periods:
#        print (period['start'])
#        print (period['end'])
#        x_data = prometheus_connection.get_prometheus_timeserie(prometheus_url,metrics[1],period['start'],period['end'],step)
#        print("x_data")
#        print(x_data)
    
#    y_dataframe = pd.DataFrame(y_data['data']['result'][0]['values']).astype(float)
#    y_dataframe.columns = ["timestamp", metrics[0]]
#    x_dataframe = pd.DataFrame(x_data['data']['result'][0]['values']).astype(float) 
#    x_dataframe.columns = ["timestamp", metrics[1]]
    
    #print(y_dataframe)
    #print(x_dataframe)
                               
#    dataframe = pd.merge(y_dataframe, x_dataframe)
#    print(dataframe)
    
#    model = LinearRegression()
    
    #sns.set(color_codes=True)
    ##sns.regplot(x=metrics[1], y=metrics[0], data=dataframe);
    ##sns_plot = sns.pairplot(dataframe, hue='species', size=2.5)
    #g = sns.lmplot(x=metrics[1], y=metrics[0],data=dataframe)
    #g.set(xlabel='independent xlabel', ylabel='dependent ylabel')
    #[plt.setp(ax.get_xticklabels(), rotation=90) for ax in g.axes.flat]
    #g.savefig(os.getcwd()+"/static/results/linear_regression_test.png");

    #print (os.getcwd()+"/static/results/linear_regression_test.html")
    #f = open(os.getcwd()+"/static/results/linear_regression_test.html",'w')

    # message = """<html>
    #<head></head>
    # <body><p><h3>This is a simple linear regression model</h3></p>
    # <p>between metrics:</p>
    # <ol style=\"list-style: none; font-size: 12px; line-height: 32px;\">
    # <li style=\"clear: both;\"><img style=\"float: left;\" src=\"/static/images/star.png\" alt=\"y_metric\" width="45\" /> <b>y axis metric:</b></br> """+metrics[0]+""" </li>
    # <li style=\"clear: both;\"><img style=\"float: left;\" src=\"/static/images/star.png\" alt=\"x_metric\" width="45\" /> <b>x axis metric:</b></br>"""+metrics[1]+""" </li>
    # </ol>
    # <img style=\"float: left;\" src=\"/static/results/linear_regression_test.png\" alt=\"liner_regression_result\" width="30%\" />
    # </body>
    # </html>"""

    #f.write(message)
    #f.close()
    #return '/static/results/linear_regression_test.html'
    return 'hello333!'
