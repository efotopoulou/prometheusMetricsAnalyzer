import os

def st(prometheus_url,periods,metrics,step):
    print (os.getcwd()+"/static/results/simple_test.html")
    f = open(os.getcwd()+"/static/results/simple_test.html",'w')

    message = """<html>
    <head></head>
    <body><p>Hello World! This is a simple test</p></body>
    </html>"""

    f.write(message)
    f.close()
    return '/static/results/simple_test.html'
