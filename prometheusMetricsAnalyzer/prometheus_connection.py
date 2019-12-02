# importing the requests library 
import requests 

def get_prometheus_timeserie(prometheus_url,metric_name,start,end,step):
    
   PARAMS = {'step':step,'start':start,'end':end,'step':step} 
   prometheus_url_query =  prometheus_url + "/api/v1/query_range?query="
   # sending get request and saving the response as response object 
   r = requests.get(url = prometheus_url_query+metric_name, params = PARAMS) 
   #print(r.url)
   data = r.json() 
   #print(data)
  
   return data
