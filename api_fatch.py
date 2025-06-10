import pandas as pd
import requests

url='https://api.freeapi.app/api/v1/public/randomproducts'
response= requests.get(url)
api_data=response.json()['data']['data']

df = pd.DataFrame(response.json()['data']['data'])[['id','title','category','brand','description','price','rating']]
df.to_csv('product_info.csv',index=False)